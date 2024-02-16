"""
Slab Opening Class
"""


class Opening:
    """
    Class for specifying slab openings for a ShearFix calculation
    """
    def __init__(self, position_x: float, position_y: float, width: float, height: float = 0.):
        self.x = position_x / 1_000
        self.y = position_y / 1_000
        self.z = 0.
        self.width = width / 1_000
        self.height = height / 1_000
        self.is_rectangular = False
        if height:
            self.is_rectangular = True

    def parameter_dict(self):
        if self.is_rectangular:
            return {'Shape': 'Rectangular'}
        return {'Shape': 'Circular'}

    def setout_value_dict(self):
        return {'X': self.x, 'Y': self.y, 'Z': self.z}

    def size_value_dict(self):
        if self.is_rectangular:
            return {'Width': str(self.width),
                    'Height': str(self.height)}
        return {'Diameter': str(self.width)}
