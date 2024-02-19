"""
Column Profile Class
"""


class ColumnProfile:
    """
    Class for specifying the profile of a column for a ShearFix calculation
    """
    def __init__(self, width: float, height: float = 0.):
        if not height:
            self.shape = "Circular"
            self.geometry = {'Diameter': width / 1_000}
        else:
            self.shape = "Rectangular"
            self.geometry = {'Width': width / 1_000, 'Height': height / 1_000}
