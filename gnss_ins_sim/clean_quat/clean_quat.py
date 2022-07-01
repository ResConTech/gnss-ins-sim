'''
Used to fix discontinuties in quaternion data.
'''

__author__ = "Hayden Gray"

import numpy as np
from matplotlib import pyplot as plot

#ref_att_quat_file = "sim_results/ref_att_quat.csv"

#ref_quat = np.loadtxt(ref_att_quat_file, delimiter=',', skiprows=1)

#plot.figure()
#plot.plot(ref_quat)

# Thank you army research laboratory: https://apps.dtic.mil/sti/pdfs/AD1043624.pdf
def clean(ref_quat):
    clean_quat = np.zeros(ref_quat.shape)
    clean_quat[0] = ref_quat[0]
    for i in range(1,ref_quat.shape[0]):  # For every orientation at each time step.
        prev_q = clean_quat[i - 1]
        curr_q = ref_quat[i]
        if((prev_q[0]*curr_q[0] + prev_q[1]*curr_q[1] + prev_q[2]*curr_q[2] + prev_q[3]*curr_q[3]) < 0):
            clean_quat[i] = (-1 * ref_quat[i])
        else:
            clean_quat[i] = ref_quat[i]

    return clean_quat

# Just for looking at the plots.
#plot.figure()
#plot.plot(clean_quat)
#plot.show()

# Add an empty row at the beginning so that np code in other scripts isnt broken. (skiprows = 1)
# dummy_row = np.zeros((1,4))     
# clean_quat = np.concatenate((dummy_row, clean_quat))
# np.savetxt("sim_results/ref_att_quat.csv", clean_quat, fmt='%f', delimiter=',')     # Overwrite ref_att_quat.csv