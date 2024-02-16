"""
ShearFix Calculation Class
"""
from .column_profile import ColumnProfile
from .column_layout import ColumnLayout
from .slab import Slab
from .reinforcement import Reinforcement, ReoLayer
from .opening import Opening
from .loading import Loading
from .enumerations import DesignCode, Region, ReoInputMode, ReoDirection
from typing import Union


class Calculation:
    """
    Class for collating all inputs to a ShearFix calculation
    """
    def __init__(self, name: str, floor: str,
                 design_code: DesignCode, region: Region,
                 column_profile: ColumnProfile,
                 slab: Slab,
                 loading: Loading,
                 column_layout: ColumnLayout = ColumnLayout(),
                 openings: Union[None, list[Opening]] = None,
                 reinforcement: Reinforcement = Reinforcement(ReoInputMode.LAYERS,
                                                              [ReoLayer(ReoDirection.HORIZONTAL),
                                                               ReoLayer(ReoDirection.VERTICAL)])):
        self.name = name
        self.design_code = design_code
        self.region = region
        self.floor = floor
        self.column_reference = 1
        self.num_columns = 1
        self.column_profile = column_profile
        self.column_layout = column_layout
        self.slab = slab
        self.openings = openings
        self.reinforcement = reinforcement
        self.loading = loading

    def parameter_dict(self):
        return {'ColumnReference': str(self.column_reference),
                'FloorLevel': str(self.floor),
                'ColumnCount': str(self.num_columns),
                'Location': str(self.column_layout.layout_type),
                'Shape': str(self.column_profile.shape)}
