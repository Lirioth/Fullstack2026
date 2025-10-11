
"""
⏱️ Page Load Timer — Measure full response time with requests + time

- Goal: Return how long a web page takes to fully download (headers + body). 🌐
- Method: Perform a GET request with streaming and read the entire body to completion. ✅
- Extras: Clean API, helpful emojis in comments, neutral tone. ✨
"""

from __future__ import annotations

import time
from typing import Dict, Iterable, List, Tuple
from statistics import mean, pstdev
from urllib.parse import urlsplit

import requests

# 🌍 Default test targets (CLI can override)
DEFAULT_URLS: Tuple[str, ...] = (
    "https://www.google.com",
    "https://www.ynet.co.il",
    "https://www.imdb.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
)

# 🧰 Small helper: ensure URLs are complete (add https:// if missing)
def normalize_url(url: str) -> str:
    parts = urlsplit(url)
    if not parts.scheme:
        return "https://" + url
    return url

def measure_load_time(url: str, timeout: int = 15, verify: bool = True) -> Dict:
    """Measure full download time for a single URL. ⏲️

    The measurement starts just before the request and ends
    after the *entire* response body has been consumed. 🧃

    Args:
        url: Target address (scheme optional; https assumed if missing).
        timeout: Per-request timeout in seconds.
        verify: TLS certificate verification (keep True unless debugging).

    Returns:
        dict with fields:
            - url (str)
            - elapsed_s (float)
            - status (int | None)
            - bytes (int)
            - ok (bool)
            - error (str | None)
    """
    target = normalize_url(url)
    t0 = time.perf_counter()  # 🎬 start the stopwatch
    try:
        # 🤝 Use a short-lived Session to benefit from connection pooling if reused.
        with requests.Session() as s:
            # 📥 stream=True lets us explicitly read the whole body to completion.
            with s.get(target, stream=True, timeout=timeout, verify=verify) as resp:
                resp.raise_for_status()
                total = 0
                # 🚚 Read the entire payload in chunks to ensure full download time is measured.
                for chunk in resp.iter_content(chunk_size=65536):
                    if chunk:
                        total += len(chunk)
        elapsed = time.perf_counter() - t0  # 🛎️ stop
        return {
            "url": target,
            "elapsed_s": elapsed,
            "status": resp.status_code,
            "bytes": total,
            "ok": True,
            "error": None,
        }
    except Exception as e:
        elapsed = time.perf_counter() - t0  # even failures have a duration
        return {
            "url": target,
            "elapsed_s": elapsed,
            "status": None,
            "bytes": 0,
            "ok": False,
            "error": str(e),
        }

def benchmark(urls: Iterable[str], attempts: int = 3, timeout: int = 15, verify: bool = True) -> Dict[str, Dict]:
    """Run multiple attempts per URL and summarize results. 📊

    Returns a dict keyed by URL with per-attempt times and summary stats.
    """
    report: Dict[str, Dict] = {}
    for raw_url in urls:
        tgt = normalize_url(raw_url)
        times: List[float] = []
        bytes_read: List[int] = []
        errors: List[str] = []
        statuses: List[int] = []

        for _ in range(max(1, attempts)):
            r = measure_load_time(tgt, timeout=timeout, verify=verify)
            if r["ok"]:
                times.append(r["elapsed_s"])
                bytes_read.append(r["bytes"])
                statuses.append(r.get("status") or 0)
            else:
                errors.append(r["error"])

        if times:
            report[tgt] = {
                "attempts": len(times),
                "times_s": times,
                "min_s": min(times),
                "avg_s": mean(times),
                "max_s": max(times),
                "stdev_s": pstdev(times) if len(times) > 1 else 0.0,
                "status_samples": statuses[:5],
                "bytes_samples": bytes_read[:5],
                "errors": errors,
            }
        else:
            report[tgt] = {
                "attempts": 0,
                "times_s": [],
                "min_s": None,
                "avg_s": None,
                "max_s": None,
                "stdev_s": None,
                "status_samples": [],
                "bytes_samples": [],
                "errors": errors or ["All attempts failed"],
            }
    return report
