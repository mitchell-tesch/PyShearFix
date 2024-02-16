"""
Loading Class
"""
from pyshearfix.enumerations import EccFactorMode


class Loading:
    """
    Class for specifying column loading for a ShearFix calculation
    """
    def __init__(self, shear: float,
                 moment_x: float = 0.0, moment_y: float = 0.0,
                 apply_min_moment: bool = True,
                 ecc_factor_mode: EccFactorMode = EccFactorMode.DEFAULT,
                 ecc_factor: float = 1.4):
        self.ecc_factor_mode = ecc_factor_mode
        self.ecc_factor = ecc_factor
        self.apply_min_moment = apply_min_moment
        self.moment_x = moment_x * 1_000
        self.moment_y = moment_y * 1_000
        self.shear = shear * 1_000

    def parameter_dict(self):
        return {'LoadIncreaseFactor': str(self.ecc_factor),
                'LoadIncreaseFactorInput': self.ecc_factor_mode,
                'ApplyMinimumMoments': str(self.apply_min_moment).lower()}

    def actions_value_dict(self):
        return {"MomentHorizontal": self.moment_x,
                "MomentVertical": self.moment_y,
                "ShearLoad": self.shear}
