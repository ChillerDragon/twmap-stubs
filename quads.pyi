from typing import Optional


class Quads:
    position: tuple
    corners: list
    colors: list
    texture_coords: list
    position_env: Optional[int]
    position_env_offset: int
    color_env: Optional[int]
    color_env_offset: int
    def new(self, pos_x: float, pos_y: float, width: float, height: float) -> Quads:
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...
