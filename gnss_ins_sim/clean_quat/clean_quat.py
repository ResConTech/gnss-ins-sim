'''
Used to fix discontinuties in quaternion data.
'''

__author__ = "Hayden Gray"

import numpy as np
from matplotlib import pyplot as plot

# Reference : https://apps.dtic.mil/sti/pdfs/AD1043624.pdf
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