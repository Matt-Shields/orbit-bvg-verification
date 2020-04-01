"""
Compare ORBIT results with BVG Guide to Offshore Wind Farm

Matt Shields
"""

import os

import yaml
import pandas as pd
import matplotlib.pyplot as plt

import ORBIT
from ORBIT import ProjectManager
print(f"Using ORBIT version {ORBIT.__version__}.")

from orbit_config import phases, config
from bvg_library import bvg_bos, bvg_install, bvg_components

def run_comparison():
    orbit_proj = instantiate_orbit()
    costs = pd.DataFrame()
    _orbit_costs = pd.Series(orbit_proj.phase_costs, name='orbit')
    _bvg_costs = pd.Series(bvg_components, name='bvg')

    costs = pd.concat([costs, _orbit_costs, _bvg_costs], axis=1, sort="False")
    costs['rel_err'] = costs.apply(lambda row: (row.iloc[1] - row.iloc[0]) / row.iloc[0] * 100, axis=1)
    print(costs)

def instantiate_orbit():
    ProjectManager.compile_input_dict(phases)
    path = os.path.join(os.getcwd(), "..\general_library")
    ORBIT_project = ProjectManager(config, weather=None, library_path=path)
    ORBIT_project.run_project()
    print('OSS', ORBIT_project._phases["OffshoreSubstationDesign"].design_result)
    return ORBIT_project

if __name__ == "__main__":
    run_comparison()