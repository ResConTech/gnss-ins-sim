""" run_sim.py runs the simulator with IMU parameters specfied in this file."""

import os
import sys
import math
from ANSI_color import *
from gnss_ins_sim.sim import imu_model
from gnss_ins_sim.sim import ins_sim
from config import config

config = config()

motion_def_path = os.path.abspath('.//motion_files/motion_IMU_Path_{}.csv')
fs = 100.0          # IMU sample frequency
fs_gps = 10.0       # GPS sample frequency
fs_mag = fs         # magnetometer sample frequency, not used for now

def test_path_gen(motion_profile):
    '''
    test only path generation in Sim.
    '''
    #### choose a built-in IMU model, typical for IMU381
    imu_err = 'high-accuracy'
    # generate GPS and magnetometer data
    imu = imu_model.IMU(accuracy=imu_err, axis=9, gps=True)

    #### start simulation
    sim = ins_sim.Sim([fs, fs_gps, fs_mag],
                    motion_profile, 
                    ref_frame=0,
                    imu=imu,
                    mode=None,
                    env=None,
                    algorithm=None)
    sim.run(1)
    # Save simulation data.
    if(not(config.IMU_RC_PATH == "")):
        sim.results(config.IMU_RC_PATH)
    if(not(config.EKF_PATH == "")):
        sim.results(config.EKF_PATH)

    sim.results("sim_results")

    # plot data, 3d plot of reference positoin, 2d plots of gyro and accel
    sim.plot(['ref_att_quat','ref_vel','ref_accel','ref_pos', 'gyro', 'accel', 'ref_att_euler'])

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        motion_profile = sys.argv[1]
        test_path_gen(motion_profile)
    else:
        print("{}Please specify a motion profile.{}".format(WARNING, ENDC))
        print("(e.g. {}python3 run_sim.py motion_profiles/your_motion_path.csv{})".format(BOLD, ENDC))
    
    
