"""
Column Layout Class
"""
from pyshearfix.enumerations import LayoutType, EdgePosition


class ColumnLayout:
    """
    Class for specification of column position on slab and edge details for a ShearFix calculation
    """
    def __init__(self, layout_type: LayoutType = LayoutType.INTERNAL,
                 edge_position: EdgePosition = EdgePosition.NONE,
                 edge_dist_x: float = 0, edge_dist_y: float = 0):
        self.layout_type = layout_type
        self.edge_position = edge_position
        self.edge_geometry = {'Horizontal': edge_dist_x/1000,
                              'Vertical': edge_dist_y/1000}

    def edge_parameter_dict(self):
        return {'EdgePosition': str(self.edge_position)}
