"""
File: weathergui.py
Role: XP Ninja BONUS — GUI-style bar chart for 3-day humidity forecast using Matplotlib. 📊💧
Uses:
  • matplotlib (Tkinter backend pops a window) 🪟
  • pytz + datetime for day labels 🗓️
  • pyowm for data (5-day / 3h forecast) 🌤️
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Dict, Iterable, List, Sequence, Tuple

import matplotlib.pyplot as plt
import pytz
from pyowm import OWM

# ---------------------- Data wrangling 🔧 ----------------------
def _three_day_humidity(owm: OWM, place: str, *, tzname: str | None = None) -> Tuple[List[str], List[int]]:
    """Return (day_labels, humidities) for the next 3 calendar days at place. 🧮
    We compute mean humidity per day from 3h forecast buckets.
    """
    fc = owm.weather_manager().forecast_at_place(place, "3h")
    forecast = fc.forecast
    weathers = getattr(forecast, "weathers", [])
    if not weathers:
        return [], []

    # Determine timezone (best effort): if tzname provided use it, else local tz. 🌍
    tz = pytz.timezone(tzname) if tzname else datetime.now().astimezone().tzinfo

    # Group humidities by local calendar day
    groups: Dict[Tuple[int, int, int], List[int]] = defaultdict(list)
    for w in weathers:
        # PyOWM Weather: reference_time('date') -> datetime (UTC)
        utc_dt = w.reference_time("date")
        if utc_dt.tzinfo is None:
            utc_dt = utc_dt.replace(tzinfo=timezone.utc)
        local_dt = utc_dt.astimezone(tz)
        key = (local_dt.year, local_dt.month, local_dt.day)
        groups[key].append(int(w.humidity))

    # Pick today and the next two days
    today_local = datetime.now(tz).date()
    days = [today_local + timedelta(days=i) for i in range(3)]
    labels: List[str] = [d.strftime("%a %d %b") for d in days]
    values: List[int] = []
    for d in days:
        key = (d.year, d.month, d.day)
        vals = groups.get(key, [])
        values.append(int(round(sum(vals) / len(vals))) if vals else 0)
    return labels, values


# ---------------------- Plot functions 🎨 ----------------------
def init_plot(ax: plt.Axes, city_label: str) -> None:
    """Initialize y-label and title per spec. 🏷️"""
    ax.set_ylabel("Humidity (%)")
    ax.set_title(f"3-Day Humidity Forecast — {city_label}")


def plot_temperatures(ax: plt.Axes, labels: Sequence[str], humidities: Sequence[int]) -> List[plt.Rectangle]:
    """Despite the name, we plot HUMIDITY bars as per the Ninja brief. 💧📊"""
    bars = ax.bar(labels, humidities)
    ax.set_ylim(0, max(100, max(humidities or [0]) + 10))
    return list(bars)


def write_humidity_on_bar_chart(ax: plt.Axes, bars: Sequence[plt.Rectangle], humidities: Sequence[int]) -> None:
    """Annotate bars with %RH. ✍️"""
    for rect, val in zip(bars, humidities):
        ax.text(rect.get_x() + rect.get_width() / 2.0, rect.get_height() + 1, f"{val}%", ha="center", va="bottom")


def show_humidity_chart(owm: OWM, place: str, tzname: str | None = None) -> None:
    """Fetch, prep, and plot the humidity forecast. 🖼️"""
    labels, values = _three_day_humidity(owm, place, tzname=tzname)
    if not labels:
        print("No forecast data available to plot.")
        return
    fig, ax = plt.subplots(figsize=(7, 4))
    init_plot(ax, place)
    bars = plot_temperatures(ax, labels, values)
    write_humidity_on_bar_chart(ax, bars, values)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import os
    key = os.getenv("OWM_API_KEY")
    if not key:
        raise SystemExit("Set OWM_API_KEY to your OpenWeatherMap API key.")
    owm = OWM(key)
    city = input("City for humidity chart (e.g., 'Paris,FR'): ").strip() or "Paris,FR"
    show_humidity_chart(owm, city)
