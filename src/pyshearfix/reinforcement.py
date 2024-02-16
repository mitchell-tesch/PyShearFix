"""
Slab Reinforcement Class and classes containing slab reinforcement details
"""
from pyshearfix.enumerations import ReoInputMode, ReoDirection, ReoLayerInputMode
from typing import Union


class ReoLayer:
    """
    Class for specifying a slab reinforcement layer
    """
    def __init__(self, direction: ReoDirection,
                 bar_diameter: int = 16,
                 num_bars: int = 0,
                 spacing: int = 300):
        self.direction = direction
        self.bar_diameter = bar_diameter / 1_000
        self.num_bars = num_bars
        self.spacing = spacing / 1_000

    @classmethod
    def from_num_bars(cls, direction, bar_diameter, num_bars):
        return cls(direction=direction, bar_diameter=bar_diameter, num_bars=num_bars)

    @classmethod
    def from_spacing(cls, direction, bar_diameter, spacing):
        return cls(direction=direction, bar_diameter=bar_diameter, spacing=spacing)

    def parameter_dict(self):
        return {'Direction': str(self.direction),
                'NumberOfBarsPerMeter': str(self.num_bars)}

    def value_dict(self):
        return {'BarDiameter': str(self.bar_diameter),
                'Spacing': str(self.spacing)}


class ReoRatio:
    """
    Class for specifying slab reinforcement ratio
    """
    def __init__(self,
                 ratio: float,
                 effective_depth: int):
        self.ratio = ratio
        self.effective_depth = effective_depth / 1_000

    def parameter_dict(self):
        return {'ReinforcementRatio': str(self.ratio)}

    def value_dict(self):
        return {'EffectiveHeight': str(self.effective_depth)}


class Reinforcement:
    """
    Class for specifying slab reinforcement for ShearFix calculation
    """
    def __init__(self, input_mode: ReoInputMode,
                 reinforcement: Union[ReoRatio, list[ReoLayer]],
                 layer_mode: ReoLayerInputMode = ReoLayerInputMode.SPACING):
        self.input_mode = input_mode
        self.detail = reinforcement
        self.layer_mode = layer_mode

    def parameter_dict(self):
        return {'InputMode': str(self.input_mode)}

    def layers_parameter_dict(self):
        return {'InputMode': str(self.layer_mode)}
