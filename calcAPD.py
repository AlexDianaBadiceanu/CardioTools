#!/usr/bin/env python

import numpy as np

def calculate_apd (data_file, perc):

    data = np.loadtxt(data_file)            # format: %f %f \n (time voltage)
    tm = data[:,0]                          # time
    vm = data[:,1]                          # transmembrane potential

    ### find the activation time
    idmax = 0
    dvmax = 0.0
    dt = tm[1] - tm[0]
    size = len(vm)-1

    for i in xrange(size):
        dv = vm[i+1] - vm[i]
        if (dv > dvmax):
            dvmax = dv/dt
            idmax = i

    act_time = tm[idmax]

    amp = np.max(vm) - np.min(vm)           # find the AP amplitude

    #### find the repolarization time
    vchk = amp*(1.0-perc) + np.min(vm)
    stop = False
    for i in xrange(size):
        dv = vm[i+1] - vm[i]
        if ((dv<0.) and (vm[i] < vchk) and (not stop)):
            rep_time = tm[i]
            stop = True

    apd = np.abs(rep_time - act_time)       # calculate APD

    print 'APD %d   ' % (perc*100),
    print '%08.4f ms' % apd
    return apd

if __name__ == "__main__":

    import doctest
    doctest.testmod()

calculate_apd ("test.dat", 0.95)
calculate_apd ("test.dat", 0.9)
calculate_apd ("test.dat", 0.85)
calculate_apd ("test.dat", 0.8)
calculate_apd ("test.dat", 0.75)
calculate_apd ("test.dat", 0.7)
calculate_apd ("test.dat", 0.65)
calculate_apd ("test.dat", 0.6)
calculate_apd ("test.dat", 0.55)
calculate_apd ("test.dat", 0.5)

