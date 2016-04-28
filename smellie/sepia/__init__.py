"""
This package gives a python API to a subset of the PicoQuant provided C-software documented HERE. 
Not all of the functions are exposed, and there has been one critical modification:
`sepia.slm.set_pulse_parameters` has the bPulseMode parameter hard-coded to 1 ( = pulsed mode), 
since using bPulseMode = 0 (continuous mode) could damage the laser head. You don't want to change this.
"""
