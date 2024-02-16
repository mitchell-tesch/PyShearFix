"""
Slab Class
"""
from pyshearfix.enumerations import SlabStepDirection, SlabStepSurface


class Slab:
    """
    Class for specifying all slab inputs for a ShearFix calculation
    """
    def __init__(self, thickness: int, concrete_grade: int, top_cover: int, bottom_cover: int,
                 use_avg_pre_compression: bool = True,
                 avg_pre_compression: int = 0,
                 x_pre_compression: float = 0., y_pre_compression: float = 0.,
                 vertical_pre_stress: float = 0.,
                 step_direction: SlabStepDirection = SlabStepDirection.VERTICAL,
                 step_surface: SlabStepSurface = SlabStepSurface.BOTTOM,
                 step_thickness: float = 0., step_distance: float = 0.):
        self.concrete_grade = concrete_grade

        if step_thickness == 0:
            self.is_constant = True
        else:
            self.is_constant = False

        self.step_direction = step_direction
        self.step_surface = step_surface

        self.thickness = thickness / 1_000
        self.step_thickness = step_thickness / 1_000
        self.step_distance = step_distance / 1_000

        self.top_cover = top_cover / 1_000
        self.bottom_cover = bottom_cover / 1_000

        self.use_avg_pre_compression = use_avg_pre_compression

        self.avg_pre_compression = avg_pre_compression
        self.x_pre_compression = x_pre_compression
        self.y_pre_compression = y_pre_compression
        self.vertical_pre_stress = vertical_pre_stress

    def parameter_dict(self):
        return {'ConcreteGrade': str(self.concrete_grade)}

    def thick_parameter_dict(self):
        return {'IsConstant': str(self.is_constant).lower(),
                'Direction': str(self.step_direction),
                'StepSurface': str(self.step_surface)}

    def thick_value_dict(self):
        return {'Constant': self.thickness,
                'Thickness1': self.thickness,
                'Thickness2': self.step_thickness,
                'DistanceCeiling': self.step_distance}

    def cover_value_dict(self):
        return {'TopConcreteCover': self.top_cover,
                'BottomConcreteCover': self.bottom_cover}

    def pre_comp_value_dict(self):
        return {'PreCompression': self.avg_pre_compression,
                'PreCompressionX': self.x_pre_compression,
                'PreCompressionY': self.y_pre_compression,
                'PreCompressionV': self.vertical_pre_stress}

    def pre_comp_parameter_dict(self):
        return {'IsSp': str(self.use_avg_pre_compression).lower()}
