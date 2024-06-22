# -*- coding: utf-8 -*-
"""Setup file for Common Robot Interface.
"""

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="common-robot-interface",
    version="2024.6",
    description="Common Robot Interface",
    license="GPLv3",
    long_description=long_description,
    authors="John Lloyd, Nathan Lepora, Wenrui Guo",
    author_emaila="j.lloyd@bristol.ac.uk, n.lepora@bristol.ac.uk, yv23708@bristol.ac.uk",
    url="https://github.com/wenruigou/common-robot-interface",
    packages=["cri", "cri.abb", "cri.ur", "cri.ur.rtde", "cri.dobot", "cri.dobot.mg400",  "cri.dobot.cr", "cri.dobot.magician", "cri.dummy", "cri.franka", "cri.sim", "cri.sim.utils"],
	package_data={'cri.ur': ['rtde_config.xml'],
            "cri.dobot.magician": ['DobotDll.dll',"msvcp120.dll","msvcr120.dll","Qt5Core.dll","Qt5Network.dll","Qt5SerialPort.dll"]},
    install_requires=["numpy", "transforms3d"]
)