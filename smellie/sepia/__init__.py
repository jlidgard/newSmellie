"""
This package gives a python API to a subset of the PicoQuant provided C-software documented HERE. 
Not all of the functions are exposed, and there have been two critical modifications:
(1) `sepia.slm.set_pulse_parameters` has the bPulseMode parameter hard-coded to 1 ( = pulsed mode), since using bPulseMode = 0 (continuous mode) could damage the laser head.
(2) the frequency mode is hard-coded to 6 ( = triggering off the rising edge of an external trigger signal), since using the internal SEPIA trigger signals at MHz rate could damage the detector.
You don't want to change these.
"""
