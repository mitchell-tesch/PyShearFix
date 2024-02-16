"""
ShearFix Main Class
"""

import xml.etree.ElementTree as ET
from pyshearfix.calculation import Calculation
from pyshearfix.enumerations import ReoInputMode
from pyshearfix.ec2_annex import Ec2Annex

# ShearFix Constants
SHEARFIX_VERSION = "6.2.2.0"
XML_ENCODING = 'ISO-8859-1'


class ShearFix:
    """Class for generating a ShearFix project"""
    def __init__(self, project_name: str, designer: str, project_number: str, ec2_annex: Ec2Annex = Ec2Annex()):
        self.project_name = project_name
        self.designer = designer
        self.project_number = project_number
        self.calculations: list[Calculation] = []
        self.ec2_annex = ec2_annex

    def add_calculation(self, calculation: Calculation):
        self.calculations.append(calculation)

    def write_asfx_file(self, file_path: str):
        # xml document root
        root = ET.Element('DOCUMENT')

        # document header
        header = ET.SubElement(root, 'HEADER')
        ET.SubElement(header, 'Version', ShearFix=SHEARFIX_VERSION)
        project = ET.SubElement(header, 'Project')
        ET.SubElement(project, 'BP_0', value=self.project_name)
        ET.SubElement(project, 'BP_1', value='')
        ET.SubElement(project, 'BP_2', value='')
        ET.SubElement(project, 'Adr_0', value=self.designer)
        ET.SubElement(project, 'Adr_1', value='')
        ET.SubElement(project, 'PrNr', value=self.project_number)

        # add individual calculations
        calculations = ET.SubElement(root, 'CALCULATION_LIST')
        for calc in self.calculations:
            # calculation
            sf_calc = ET.SubElement(calculations, 'ShearFix_CALCULATION')
            ET.SubElement(sf_calc, 'Text', value=calc.name)
            ET.SubElement(sf_calc, 'DesignCode', value=str(calc.design_code))
            ET.SubElement(sf_calc, 'Region', value=str(calc.region))

            # column
            column = ET.SubElement(sf_calc, 'Column')
            self._dict_to_elements(calc.parameter_dict(), column)
            # column > shape
            shape = ET.SubElement(column, 'Shape')
            shape.text = calc.column_profile.shape
            geometry = ET.SubElement(column, calc.column_profile.shape)
            self._dict_to_value_elements(calc.column_profile.geometry, geometry)
            # colum > edge
            if calc.column_layout:
                edge = ET.SubElement(column, 'Edge')
                self._dict_to_elements(calc.column_layout.edge_parameter_dict(), edge)
                self._dict_to_value_elements(calc.column_layout.edge_geometry, edge)

            # slab
            slab = ET.SubElement(sf_calc, 'Slab')
            # slab > concrete grade
            self._dict_to_elements(calc.slab.parameter_dict(), slab)
            # slab > thickness
            slab_thickness = ET.SubElement(slab, 'Thickness')
            self._dict_to_value_elements(calc.slab.thick_parameter_dict(), slab_thickness)
            self._dict_to_value_elements(calc.slab.thick_value_dict(), slab_thickness)
            self._dict_to_value_elements(calc.slab.cover_value_dict(), slab)
            # slab > pre-compression
            pre_compression = ET.SubElement(slab, 'PreCompression')
            self._dict_to_value_elements(calc.slab.pre_comp_parameter_dict(), pre_compression)
            self._dict_to_value_elements(calc.slab.pre_comp_value_dict(), pre_compression)

            # openings
            openings = ET.SubElement(sf_calc, 'Openings')
            rect_openings = ET.SubElement(openings, 'RectangularOpenings')
            circ_openings = ET.SubElement(openings, 'CircularOpenings')
            if calc.openings:
                for opening in calc.openings:
                    if opening.is_rectangular:
                        open_el = ET.SubElement(rect_openings, 'RectangularOpening')
                    else:
                        open_el = ET.SubElement(circ_openings, 'CircularOpening')
                    self._dict_to_elements(opening.parameter_dict(), open_el)
                    center = ET.SubElement(open_el, 'Center')
                    self._dict_to_value_elements(opening.setout_value_dict(), center)
                    self._dict_to_value_elements(opening.size_value_dict(), open_el)

            # reinforcement
            reinforcement = ET.SubElement(sf_calc, 'Reinforcement')
            self._dict_to_elements(calc.reinforcement.parameter_dict(), reinforcement)
            if calc.reinforcement.input_mode == ReoInputMode.RATIO:
                reo_ratio = ET.SubElement(reinforcement, 'RatioHeight')
                self._dict_to_elements(calc.reinforcement.detail.parameter_dict(), reo_ratio)
                self._dict_to_value_elements(calc.reinforcement.detail.value_dict(), reo_ratio)
            else:
                layers = ET.SubElement(reinforcement, 'Layers')
                self._dict_to_elements(calc.reinforcement.layers_parameter_dict(), layers)
                layers_inner = ET.SubElement(layers, 'Layers')
                for reo_layer in calc.reinforcement.detail:
                    layer = ET.SubElement(layers_inner, 'ReinforcementLayer')
                    self._dict_to_elements(reo_layer.parameter_dict(), layer)
                    self._dict_to_value_elements(reo_layer.value_dict(), layer)

            # loading
            loading = ET.SubElement(sf_calc, 'Loading')
            self._dict_to_elements(calc.loading.parameter_dict(), loading)
            self._dict_to_value_elements(calc.loading.actions_value_dict(), loading)

        # Ec2 Annex Parameters
        ec2 = ET.SubElement(root, 'AnnexEc2')
        ec2_parameters = ET.SubElement(ec2, 'NationalAnnexParametersEC2')
        self._dict_to_elements(self.ec2_annex.parameter_dict(), ec2_parameters)

        # compile tree and write
        tree = ET.ElementTree(root)
        ET.indent(tree, space="  ", level=0)
        tree.write(file_path, encoding=XML_ENCODING, xml_declaration=True)

    @staticmethod
    def _dict_to_value_elements(value_dict, parent_element):
        for key, value in value_dict.items():
            element = ET.SubElement(parent_element, key)
            element_value = ET.SubElement(element, 'Value')
            element_value.text = str(value)

    @staticmethod
    def _dict_to_elements(element_dict, parent_element):
        for key, value in element_dict.items():
            element = ET.SubElement(parent_element, key)
            element.text = str(value)
