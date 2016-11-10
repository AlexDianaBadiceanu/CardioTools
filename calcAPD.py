#!/usr/bin/env python
#Script used on waveform data to determine the duration of 
#action potentials. APDs are computed as the time point of 
#maximal upstroke velocity (dV/dt)max minus the time point of 
#x% repolarization of the membrane potential (APDx).  
import numpy as np

#function used to compute APD
#takes in a file containing the waveform and
#the percent of repolarization desired
def calculate_apd (data_file, perc):

    data = np.loadtxt(data_file)            # format: %f %f \n (time voltage)
    time = data[:,0]                          # time
    Vm = data[:,1]                          # transmembrane potential

    ### find the activation time
    idmax = 0
    dvmax = 0.0
    dt = time[1] - time[0]
    size = len(Vm)-1

    for i in xrange(size):
        dv = Vm[i+1] - Vm[i]
        if (dv > dvmax):
            dvmax = dv/dt
            idmax = i

    act_time = time[idmax]

    amp = np.max(Vm) - np.min(Vm)           # find the AP amplitude

    #### find the repolarization time
    vchk = amp*(1.0-perc) + np.min(Vm)
    stop = False
    for i in xrange(size):
        dv = Vm[i+1] - Vm[i]
        if ((dv<0.) and (Vm[i] < vchk) and (not stop)):
            rep_time = time[i]
            stop = True

    APD = np.abs(rep_time - act_time)       # calculate APD

    print 'APD %d   ' % (perc*100),
    print '%08.4f ms' % APD
    return APD

if __name__ == "__main__":

    import doctest
    doctest.testmod()

    
#For most experiments we require APDs for multiple % repolarization
#Therefore, the script shows APDs from 50 to 95%
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

