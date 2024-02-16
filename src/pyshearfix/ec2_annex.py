"""
Eurocode 2 Annex Parameter Class
"""


class Ec2Annex:
    """
    Class for specifying EuroCode 2 Annex parameters for ShearFix
    """
    def __init__(self, beta_corner_column=1.5, beta_edge_column=1.4, beta_internal_column=1.15,
                 c_rdc=0.18, v_min=0.035, k1=0.1, v_rd_max=0.5, k_max_v_rdc=2, k_distance=1.5,
                 shear_rail_min_length=True):
        self.beta_corner_column = beta_corner_column
        self.beta_edge_column = beta_edge_column
        self.beta_internal_column = beta_internal_column
        self.c_rdc = c_rdc
        self.v_min = v_min
        self.k1 = k1
        self.v_rd_max = v_rd_max
        self.k_max_v_rdc = k_max_v_rdc
        self.k_distance = k_distance
        self.shear_rail_min_length = shear_rail_min_length

    def parameter_dict(self):
        return {'BetaCornerColumn': str(self.beta_corner_column),
                'BetaEdgeColumn': str(self.beta_edge_column),
                'BetaInternalColumn': str(self.beta_internal_column),
                'CrdCFactor': str(self.c_rdc),
                'FactorOfDistance': str(self.k_distance),
                'K1Factor': str(self.k1),
                'VMinFactor': str(self.v_min),
                'VRdMaxFactor': str(self.v_rd_max),
                'KmaxVRdcFactor': str(self.k_max_v_rdc),
                'RailMinLengthFromColumnFace': str(self.shear_rail_min_length).lower()}
