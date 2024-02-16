"""
All String Enumerations for ShearFix Options
"""
from enum import StrEnum


class DesignCode(StrEnum):
    AS3600 = 'AS3600'
    ACI318 = 'ACI318'
    EC2 = 'EC2UK'


class Region(StrEnum):
    AUS = 'Australia'
    UK = 'UnitedKingdom'


class LayoutType(StrEnum):
    INTERNAL = 'Internal'
    EDGE = 'Edge'
    CORNER = 'Corner'
    RE_CORNER = 'ReentrantCorner'


class EdgePosition(StrEnum):
    NONE = 'None'
    UP = 'Up'
    LEFT = 'Left'
    DOWN = 'Down'
    RIGHT = 'Right'
    UP_LEFT = 'Up Left'
    UP_RIGHT = 'Up Right'
    DOWN_LEFT = 'Down Left'
    DOWN_RIGHT = 'Down Right'


class EccFactorMode(StrEnum):
    DEFAULT = 'Default'
    CALCULATED = 'Calculated'
    INPUT = 'Input'


class SlabStepDirection(StrEnum):
    VERTICAL = 'Vertical'
    HORIZONTAL = 'Horizontal'


class SlabStepSurface(StrEnum):
    TOP = 'Top'
    BOTTOM = 'Bottom'


class ReoInputMode(StrEnum):
    LAYERS = 'DirectionLayers'
    RATIO = 'EffectiveHeight'


class ReoLayerInputMode(StrEnum):
    QTY = 'NumberOfBarsPerMeter'
    SPACING = 'Spacing'


class ReoDirection(StrEnum):
    HORIZONTAL = 'Horizontal'
    VERTICAL = 'Vertical'
