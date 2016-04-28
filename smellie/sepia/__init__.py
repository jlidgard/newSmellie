'''
This package gives a python API to a subset of the Sepia provided C-software documented HERE. 
Not all of the functions are exposed, and there has been two critical modifications:
`sepia.slm.set_pulse_parameters` has the bPulseMode parameter hard coded to 1:using bPulseMode = 0 means continuous laser light that could damage the laser head. And the trigger frequency mode is hard coded to 6 - external 
triggering (from the ni box). The sepia box has an internal trigger that runs
at MHz

You don't want to change those..
'''
