from setuptools import setup
import os

setup(name = "smellie",
      version = "1.0.1",
      description = "SNODROP smellie h/w control server",
      author= "Luca Cavalli, Jack Dunger, Chris Jones, Jeff Lidgard and Krishanu Majumdar",
      maintainer = "Jack Dunger, Jeff Lidgard",
      author_email = "jack.dunger@physics.ox.ac.uk",
      packages = ["smellie", "sepia", 
                  "server", "daqmx"], 
      py_modules = ["config"],
      install_requires = ["pyserial", "hiredis", "LabJackPython", "numpy"]
      )
