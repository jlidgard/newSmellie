'''
This package gives a python API to a subset of the Sepia provided C-software documented HERE. 
Not all of the functions are exposed, and there has been one critical modification:
`sepia.slm.set_pulse_parameters` has the bPulseMode paramter hard coded to 1:
using bPulseMode = 0 means continuous laser light that could damage the laser
head. You don't want to change that
'''
