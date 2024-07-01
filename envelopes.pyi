from typing import Literal

type EnvelopesKind = Literal['Position', 'Color', 'Sound']

class EnvPoints:
    time: int
    curve: Literal['Step', 'Linear', 'Slow', 'Fast', 'Smooth', 'Bezier']
    x: float
    a: float
    def new(self, pos: int) -> EnvPoints:
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...

class Envelopes:
    name: str
    points: EnvPoints
    def __len__(self) -> int:
        ...
    def kind(self) -> EnvelopesKind:
        ...
    def new(self, kind: EnvelopesKind) -> Envelopes:
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...
