class Cell:
    x : int
    y : int
    left_wall : bool
    bottom_wall : bool
    items : list

class LastCell(Cell):
    right_wall : bool
    top_wall: bool