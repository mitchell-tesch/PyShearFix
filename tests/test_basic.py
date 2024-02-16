from pyshearfix import (ShearFix, Calculation,
                        ColumnProfile, ColumnLayout,
                        Slab, Opening,
                        Reinforcement, ReoLayer, ReoRatio,
                        Loading, DesignCode, Region,
                        ReoInputMode, ReoDirection)

shear_fix_file = ShearFix('test_project', 'engibeer', '8888')

calculation_1 = Calculation(name='first_calculation',
                            floor='test_floor',
                            design_code=DesignCode.ACI318,
                            region=Region.AUS,
                            column_profile=ColumnProfile(600, 300),
                            slab=Slab(250, 40, 30, 30),
                            loading=Loading(100, 20, 30),
                            openings=[Opening(1000, 400, 300),
                                      Opening(-500, -1000, 200, 300)])

shear_fix_file.add_calculation(calculation_1)

shear_fix_file.write_asfx_file('test_basic.asfx')
