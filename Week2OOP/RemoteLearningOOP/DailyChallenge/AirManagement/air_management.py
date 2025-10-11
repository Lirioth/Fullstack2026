
"""
✈️ Air Management System — Minimal OOP Implementation
----------------------------------------------------
Classes: Airline, Airplane, Flight, Airport
- Each airplane can fly at most once per calendar day. 📅
- All future lists are kept sorted by date. 🗂️
- Neutral tone; friendly comments with emojis. ✨
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass(slots=True)
class Airline:
    """Airline company. 🛫"""
    id: str  # Two-letter code, e.g., "AA"
    name: str
    planes: List['Airplane'] = field(default_factory=list)

@dataclass(slots=True)
class Flight:
    """Single-day flight. 🧾"""
    date: date
    destination: 'Airport'
    origin: 'Airport'
    plane: 'Airplane'
    id: str = field(init=False)

    def __post_init__(self) -> None:
        self.id = f"{self.destination.city}-{self.plane.company.id}-{self.date.isoformat()}"  # 🆔

    def take_off(self) -> None:
        """Plane leaves origin. 🚀"""
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)
        self.origin._remove_departure(self)

    def land(self) -> None:
        """Plane arrives at destination. 🛬"""
        self.plane.current_location = self.destination
        if self.plane not in self.destination.planes:
            self.destination.planes.append(self.plane)
        self.destination._remove_arrival(self)

@dataclass(slots=True)
class Airplane:
    """Aircraft (max one flight per day). 🛩️"""
    id: int
    current_location: 'Airport'
    company: Airline
    next_flights: List[Flight] = field(default_factory=list)

    def location_on_date(self, d: date) -> 'Airport':
        """Airport at the **start** of day d. 🌅"""
        loc = self.current_location
        for fl in sorted(self.next_flights, key=lambda f: f.date):
            if fl.date < d:
                loc = fl.destination
            else:
                break
        return loc

    def has_flight_on(self, d: date) -> bool:
        return any(fl.date == d for fl in self.next_flights)

    def available_on_date(self, d: date, location: 'Airport') -> bool:
        return (self.location_on_date(d) is location) and (not self.has_flight_on(d))

    def schedule(self, fl: Flight) -> None:
        self.next_flights.append(fl)
        self.next_flights.sort(key=lambda f: f.date)

    def fly(self, destination: 'Airport') -> Optional[Flight]:
        """Execute earliest scheduled flight to `destination`. 🕹️"""
        matches = [fl for fl in self.next_flights if fl.destination is destination]
        if not matches:
            return None
        fl = sorted(matches, key=lambda f: f.date)[0]
        fl.take_off()
        fl.land()
        self.next_flights = [f for f in self.next_flights if f is not fl]
        return fl

@dataclass(slots=True)
class Airport:
    """Airport with schedules. 🗺️"""
    city: str
    planes: List[Airplane] = field(default_factory=list)
    scheduled_departures: List[Flight] = field(default_factory=list)
    scheduled_arrivals: List[Flight] = field(default_factory=list)

    def _sort_schedules(self) -> None:
        self.scheduled_departures.sort(key=lambda f: f.date)
        self.scheduled_arrivals.sort(key=lambda f: f.date)

    def _remove_departure(self, fl: Flight) -> None:
        self.scheduled_departures = [f for f in self.scheduled_departures if f is not fl]

    def _remove_arrival(self, fl: Flight) -> None:
        self.scheduled_arrivals = [f for f in self.scheduled_arrivals if f is not fl]

    def schedule_flight(self, destination: 'Airport', d: date, *, airline: Optional[Airline] = None) -> Optional[Flight]:
        """Find available plane at this airport at start of day `d` and schedule. 📅📝"""
        # Candidates: planes whose start-of-day location is here and no flight today
        # Search across all known planes: those currently parked here plus any belonging to airlines
        # registered at this airport via planes list.
        candidates: List[Airplane] = []
        # Start with planes we currently see at this airport
        seen: set[int] = set()
        for pl in self.planes:
            if airline and pl.company is not airline:
                continue
            if id(pl) in seen:
                continue
            seen.add(id(pl))
            if pl.available_on_date(d, self):
                candidates.append(pl)
        # Also scan planes parked elsewhere but that will be here by d (after prior flights)
        for ap in _GLOBAL_AIRPORTS:
            for pl in ap.planes:
                if id(pl) in seen:
                    continue
                if airline and pl.company is not airline:
                    continue
                seen.add(id(pl))
                if pl.location_on_date(d) is self and (not pl.has_flight_on(d)):
                    candidates.append(pl)

        if not candidates:
            return None

        plane = sorted(candidates, key=lambda p: p.id)[0]
        fl = Flight(date=d, destination=destination, origin=self, plane=plane)
        plane.schedule(fl)
        self.scheduled_departures.append(fl)
        destination.scheduled_arrivals.append(fl)
        self._sort_schedules()
        destination._sort_schedules()
        return fl

    def info(self, start_date: date, end_date: date) -> List[str]:
        lines: List[str] = []
        for fl in self.scheduled_departures:
            if start_date <= fl.date <= end_date:
                lines.append(f"{fl.date.isoformat()} | {fl.id} | {fl.origin.city} → {fl.destination.city} | Plane #{fl.plane.id} ({fl.plane.company.id})")
        return lines

# Global registry to help discovery in schedule_flight (simple)
_GLOBAL_AIRPORTS: List[Airport] = []

def register_airports(*airports: Airport) -> None:
    for a in airports:
        if a not in _GLOBAL_AIRPORTS:
            _GLOBAL_AIRPORTS.append(a)

if __name__ == "__main__":
    # Tiny demo 🧪
    from datetime import date as _d

    ar = Airline("AR", "Ariel Air")
    nx = Airline("NX", "Neon Express")

    tlv = Airport("TLV")
    lhr = Airport("LHR")
    cdg = Airport("CDG")
    register_airports(tlv, lhr, cdg)

    p1 = Airplane(101, tlv, ar)
    p2 = Airplane(202, tlv, nx)
    p3 = Airplane(303, lhr, ar)
    ar.planes.extend([p1, p3])
    nx.planes.append(p2)
    tlv.planes.extend([p1, p2])
    lhr.planes.append(p3)

    # Schedule flights
    tlv.schedule_flight(lhr, _d(2025, 10, 12))
    tlv.schedule_flight(cdg, _d(2025, 10, 13), airline=nx)
    lhr.schedule_flight(tlv, _d(2025, 10, 12), airline=ar)

    print("📋 TLV departures 2025-10-10..2025-10-15:")
    for line in tlv.info(_d(2025, 10, 10), _d(2025, 10, 15)):
        print(" ", line)

    executed = p1.fly(lhr)
    if executed:
        print(f"\n🛬 Executed: {executed.id} | Plane now at: {p1.current_location.city}")
        print("TLV on-ground:", [pl.id for pl in tlv.planes])
        print("LHR on-ground:", [pl.id for pl in lhr.planes])
