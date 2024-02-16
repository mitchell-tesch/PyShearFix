"""
Column Profile Class
"""


class ColumnProfile:
    """
    Class for specifying the profile of a column for a ShearFix calculation
    """
    def __init__(self, width, height=0):
        if height == 0:
            self.shape = "Circular"
            self.geometry = {'Diameter': width/1000}
        else:
            self.shape = "Rectangular"
            self.geometry = {'Width': width/1000, 'Height': height/1000}
