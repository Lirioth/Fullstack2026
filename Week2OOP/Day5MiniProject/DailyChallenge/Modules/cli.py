
"""
🖥️ CLI for Page Load Timer

Example:
    python cli.py --urls google.com ynet.co.il imdb.com --attempts 3 --timeout 10
"""
from __future__ import annotations

import argparse
import json
from typing import List
from pathlib import Path

from timer import benchmark, DEFAULT_URLS

def fmt_s(x):
    return "-" if x is None else f"{x:.3f}s"

def main():
    ap = argparse.ArgumentParser(description="Measure full page load time (requests + time). ⏱️🌐")
    ap.add_argument("--urls", nargs="*", default=list(DEFAULT_URLS), help="URLs to test (scheme optional).")
    ap.add_argument("--attempts", type=int, default=3, help="Attempts per URL (default: 3)." )
    ap.add_argument("--timeout", type=int, default=15, help="Per-request timeout in seconds (default: 15)." )
    ap.add_argument("--no-verify", action="store_true", help="Disable TLS verification (not recommended)." )
    ap.add_argument("--json-out", type=Path, default=None, help="Path to write JSON results." )
    args = ap.parse_args()

    rep = benchmark(args.urls, attempts=args.attempts, timeout=args.timeout, verify=not args.no_verify)

    # 🧾 Pretty print table
    print("\n📊 Page Load Benchmark Results\n")
    header = f"{'URL':<35} | {'min':>8} | {'avg':>8} | {'max':>8} | {'σ':>6} | {'n':>3} | samples"
    print(header)
    print("-" * len(header))
    for url, r in rep.items():
        line = f"{url[:35]:<35} | {fmt_s(r['min_s']):>8} | {fmt_s(r['avg_s']):>8} | {fmt_s(r['max_s']):>8} | {('' if r['stdev_s'] is None else f'{r['stdev_s']:.3f}s'):>6} | {r['attempts']:>3} | {', '.join(f'{t:.3f}s' for t in r['times_s'][:5])}"
        print(line)
        if r['errors']:
            print(f"   ⚠️  Errors: {r['errors']}")
    print()

    if args.json_out:
        args.json_out.write_text(json.dumps(rep, indent=2), encoding="utf-8")
        print(f"💾 Saved JSON to: {args.json_out}")

if __name__ == "__main__":
    main()
