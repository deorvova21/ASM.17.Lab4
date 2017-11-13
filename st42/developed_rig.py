from .drilling_rig import *

class Developed_rig(Drilling_rig):
    def __init__(self):
        super().__init__()
        self._source_nation = None
        self._colour = None
