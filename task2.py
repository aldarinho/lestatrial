Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
>>> class Oar:
...     def __init__(self, side: str):
...         self.side = side  # 'left' or 'right'
... 
...     def row(self):
...         return f"Rowing with {self.side} oar"
... 
... class Anchor:
...     def __init__(self):
...         self.dropped = False
... 
...     def drop(self):
...         self.dropped = True
... 
...     def raise_anchor(self):
...         self.dropped = False
... 
...     def is_dropped(self):
...         return self.dropped
... 
... class Boat:
...     def __init__(self):
...         self.left_oar = Oar("left")
...         self.right_oar = Oar("right")
...         self.anchor = Anchor()
...         self.position = [0, 0]  # x, y
...         self.direction = 0  # Degrees
... 
...     def row_both(self):
...         if self.anchor.is_dropped():
...             return "Cannot move, anchor is dropped"
...         self.position[1] += 1
...         return "Moved forward"
... 
...     def row_left(self):
...         if self.anchor.is_dropped():
...             return "Cannot move, anchor is dropped"
        self.direction -= 10
        return "Turned right"

    def row_right(self):
        if self.anchor.is_dropped():
            return "Cannot move, anchor is dropped"
        self.direction += 10
        return "Turned left"

    def drop_anchor(self):
        self.anchor.drop()
        return "Anchor dropped"

    def raise_anchor(self):
        self.anchor.raise_anchor()
        return "Anchor raised"

    def status(self):
        return {
            "position": self.position,
            "direction": self.direction,
            "anchor_dropped": self.anchor.is_dropped()
