import xlwings as xw
import pyshearfix as sf

VERSION = '0.5a'

WB_SHEET = 'Main'
WB_PROJECT_NUM_RANGE = 'B2'
WB_PROJECT_NAME_RANGE = 'B3'
WB_DESIGNER_RANGE = 'B4'
WB_FILE_RANGE = 'B5'
WB_REGION_RANGE = 'B6'
WB_DATA_START_RANGE = 'A11:Q11'

MOCK_WB_FILE = 'ShearFixBatch.xlsx'


def main():
    wb = xw.Book.caller()
    print('\nReading input data...', end='')
    sf_conf, sf_in_data = read_wb(wb)
    print('done.')
    print('\nBuilding ShearFix file...', end='')
    # build shearfix definition
    shearfix = create_shearfix(sf_conf)
    # add shearfix calculations
    shearfix = add_shearfix_calcs(shearfix, sf_in_data)
    # write shearfix file
    shearfix.write_asfx_file(sf_conf['file'])
    print('done.')


def read_wb(wb: xw.Book):
    sheet = wb.sheets[WB_SHEET]
    sf_conf = {'project_num': sheet.range(WB_PROJECT_NUM_RANGE).value,
               'project_name': sheet.range(WB_PROJECT_NAME_RANGE).value,
               'designer': sheet.range(WB_DESIGNER_RANGE).value,
               'file': sheet.range(WB_FILE_RANGE).value,
               'region': sheet.range(WB_REGION_RANGE).value}
    sf_in_data = sheet.range(WB_DATA_START_RANGE).options(ndim=2, expand='down').value
    return sf_conf, sf_in_data


def create_shearfix(sf_conf) -> sf.ShearFix:
    return sf.ShearFix(sf_conf['project_name'],
                       sf_conf['designer'],
                       sf_conf['project_num'],
                       sf.Region(sf_conf['region']))


def add_shearfix_calcs(shearfix: sf.ShearFix, sf_in_data) -> sf.ShearFix:
    for calc_data in sf_in_data:
        # build design code definition
        design_code = sf.DesignCode(calc_data[1])
        # build column profile definition
        column_profile = sf.ColumnProfile(width=calc_data[4], height=calc_data[5])
        # clean slab inputs
        avg_pre_comp = calc_data[13]
        if avg_pre_comp:
            is_avg_pre_comp = True
            lat_pre_comp = 0.
            long_pre_comp = 0.
        else:
            is_avg_pre_comp = False
            avg_pre_comp = 0.
            lat_pre_comp = calc_data[14]
            long_pre_comp = calc_data[15]
        vert_pre_comp = calc_data[16]
        if not vert_pre_comp:
            vert_pre_comp = 0.
        # build slab definition
        slab = sf.Slab(thickness=calc_data[9], concrete_grade=int(calc_data[10]),
                       top_cover=calc_data[11], bottom_cover=calc_data[12],
                       use_avg_pre_compression=is_avg_pre_comp, avg_pre_compression=avg_pre_comp,
                       x_pre_compression=lat_pre_comp, y_pre_compression=long_pre_comp,
                       vertical_pre_stress=vert_pre_comp)
        # clean loading inputs
        moment_x = calc_data[7]
        if not moment_x:
            moment_x = 0.
        moment_y = calc_data[8]
        if not moment_y:
            moment_y = 0.
        # build loading definition
        loading = sf.Loading(shear=calc_data[6], moment_x=moment_x, moment_y=moment_y,
                             ecc_factor_mode=sf.EccFactorMode.CALCULATED)
        # add calculation
        shearfix.add_calculation(sf.Calculation(name=calc_data[0], floor=calc_data[3], design_code=design_code,
                                                column_profile=column_profile, slab=slab, loading=loading))
    return shearfix


if __name__ == '__main__':
    xw.Book(MOCK_WB_FILE).set_mock_caller()
    main()
