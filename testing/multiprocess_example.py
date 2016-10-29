import time,logging,numpy
from multiprocessing.pool import ThreadPool
from smellie import power_meter, ni_trigger_generator

def measure_power(power_n,time_delay):
    power_entries = numpy.array([])
    power_ranges = numpy.array([])

    for x in range(power_n+1):
        power = pm.get_power()
        power_entries = numpy.append(power_entries, power )
        power_ranges = numpy.append(power_ranges, pm.get_power_range() )
        time.sleep(time_delay)

    power_mean = numpy.mean(power_entries)
    power_sd = numpy.std(power_entries)
    power_range = numpy.amax(power_ranges) 

    return power_mean, power_sd, power_range

if __name__ == "__main__":
    pm = power_meter.PowerMeter()
    ni = ni_trigger_generator.TriggerGenerator()
    pm.port_open()

    pool = ThreadPool(processes=1)

    measure_power_args = (10,0.01)
    n_pulses = 10000
    repetition_rate = 10000 #Hz

    for i in range(3):
        async_measure_power = pool.apply_async(measure_power, measure_power_args)
        ni.generate_triggers(n_pulses, repetition_rate, 'PQ')
        power_mean, power_sd, power_range = async_measure_power.get()
        print i,power_mean, power_sd, power_range
 
    pm.port_close() 