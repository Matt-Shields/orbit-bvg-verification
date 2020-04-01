phases = [
    # Substructures
    'MonopileDesign',
    'MonopileInstallation',
    'ScourProtectionDesign',
    # 'ScourProtectionInstallation',

    # Turbines
    # 'TurbineInstallation',

    # Electrical
    'ArraySystemDesign',
    # 'ArrayCableInstallation',
    'ExportSystemDesign',
    # 'ExportCableInstallation',
    # 'OffshoreSubstationInstallation'
]

config = {
    # Site/plant - all from 2018 cost of wind energy review
    'site': {
        'depth': 30,
        'distance': 60,
        'distance_to_landfall': 60,
        'distance_to_beach': 0,
        'distance_to_interconnection': 9,
        'mean_windspeed': 10
    },

    'plant': {
        'layout': 'grid',  # Closest ORBIT default to Beiter et al
        'num_turbines': 100,  # Results in 600 MW plant
        'row_spacing': 7,  # From Beiter et al
        'turbine_spacing': 7,  # From Beiter et al
        'substation_distance': 1  # ORBIT default
    },

    'port': {  # ORBIT defaults
        'num_cranes': 1,
        'monthly_rate': 2000000,
        "name": "Green Port"
    },

    # Turbine and BOS components
    'turbine': '10MW_generic',  # Basis for 2018 COWER

    'monopile_design': {  # Mean values from ORCA
        'monopile_steel_cost': 2250,
        'tp_steel_cost': 3230
    },

    ##### Required inputs (no defaults)
    'scour_protection_design': {
        'cost_per_tonne': 40
    },
    'array_system_design': {
        'cables': ['XLPE_300mm_33kV', 'XLPE_800mm_33kV']  # ORCA cables.  Specific specs from JDR datasheets
    },
    'export_system_design': {
        'cables': 'XLPE_1000mm_220kV',
        'percent_added_length': 0
    },

    'substation_design': {
        'num_substations': 2
    },

    # Phase specific configurations
    'MonopileInstallation': {
        'wtiv': 'example_wtiv',

    },

    'TurbineInstallation': {
        'wtiv': 'example_wtiv',
    },

    'ArrayCableInstallation': {
        'array_cable_install_vessel': 'example_cable_lay_vessel',
    },

    'ExportCableInstallation': {
        'export_cable_install_vessel': 'example_cable_lay_vessel',
    },

    'OffshoreSubstationInstallation': {
        "num_feeders": 1,
        "feeder": "oss_2xfeeder",  # Need larger feeder capacity
        "oss_install_vessel": 'example_wtiv',
    },

    'ScourProtectionInstallation': {
        'spi_vessel': 'example_scour_protection_vessel',
    },

    # Phases
    'design_phases': [
        'MonopileDesign',
        'ScourProtectionDesign',
        'ArraySystemDesign',
        'ExportSystemDesign',
        'OffshoreSubstationDesign'
    ],
    'install_phases': [
        'MonopileInstallation',  # Updated dates
        'ScourProtectionInstallation',  # Placed at the end of the monopile installation
        'TurbineInstallation',
        'ArrayCableInstallation',
        'ExportCableInstallation',
        'OffshoreSubstationInstallation']
        # 'MonopileInstallation': '07/01/2016',  # Updated dates
        # 'ScourProtectionInstallation': '07/01/2016',  # Placed at the end of the monopile installation
        # 'TurbineInstallation': '07/01/2016',
        # 'ArrayCableInstallation': '07/01/2016',
        # 'ExportCableInstallation': '07/01/2016',
        # 'OffshoreSubstationInstallation': '07/01/2016'
    # }
}
