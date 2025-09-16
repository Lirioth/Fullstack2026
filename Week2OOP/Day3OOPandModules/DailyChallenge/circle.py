import math

class Circle:
    # you can pass radius OR diameter
    def __init__(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("give radius or diameter")
        if radius is not None and diameter is not None:
            raise ValueError("give only one: radius OR diameter")
        if diameter is not None:
            radius = float(diameter) / 2
        self.radius = float(radius)

    # property for radius (keep positive)
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        r = float(value)
        if r <= 0:
            raise ValueError("radius must be > 0")
        self._radius = r

    # diameter is derived from radius (and can set it too)
    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        d = float(value)
        if d <= 0:
            raise ValueError("diameter must be > 0")
        self._radius = d / 2

    # compute area
    def area(self):
        return math.pi * (self.radius ** 2)

    # nice text to print the circle
    def __str__(self):
        return f"Circle(r={self.radius:.2f}, d={self.diameter:.2f})"

    # for debug, same as str here
    def __repr__(self):
        return str(self)

    # add two circles -> new circle with sum of radii
    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("can only add Circle + Circle")
        return Circle(radius=self.radius + other.radius)

    # equal if same radius
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    # smaller/bigger based on radius (allows sorting)
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius


# quick demo (noob style)
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=8)   # radius = 4
    print("c1:", c1)
    print("c2:", c2)
    print("c1 area:", round(c1.area(), 2))
    print("c2 area:", round(c2.area(), 2))

    # add
    c3 = c1 + c2
    print("c3 = c1 + c2:", c3)

    # compare
    print("c1 > c2:", c1 > c2)
    print("c1 == c2:", c1 == c2)

    # sort
    circles = [c1, c2, c3, Circle(radius=1), Circle(diameter=20)]
    circles.sort()  # uses __lt__
    print("sorted by radius:", [round(c.radius, 2) for c in circles])
