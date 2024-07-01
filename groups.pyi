from .layers import Layers

class Groups:
    layers: Layers
    offset_x: float
    offset_y: float
    parallax_x: float
    parallax_y: float
    clipping: bool
    clip_x: float
    clip_y: float
    clip_width: float
    clip_height: float
    def new(self) -> Groups:
        ...
    def new_physics(self) -> Groups:
        ...
    def is_physics_group(self) -> bool:
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...
