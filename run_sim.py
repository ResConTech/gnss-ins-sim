""" run_sim.py runs the simulator with IMU parameters specfied in this file."""

import os
import math
from gnss_ins_sim.sim import imu_model
from gnss_ins_sim.sim import ins_sim
from config import config

config = config()

PROFILE_INDEX = 15

motion_def_path = os.path.abspath('.//motion_files/motion_IMU_Path_{}.csv')
fs = 100.0          # IMU sample frequency
fs_gps = 10.0       # GPS sample frequency
fs_mag = fs         # magnetometer sample frequency, not used for now

def test_path_gen():
    '''
    test only path generation in Sim.
    '''
    #### choose a built-in IMU model, typical for IMU381
    imu_err = 'mid-accuracy'
    # generate GPS and magnetometer data
    imu = imu_model.IMU(accuracy=imu_err, axis=9, gps=True)

    #### start simulation
    sim = ins_sim.Sim([fs, fs_gps, fs_mag],
                      motion_def_path.format(PROFILE_INDEX),
                      ref_frame=1,
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

    # plot data, 3d plot of reference positoin, 2d plots of gyro and accel
    sim.plot(['ref_att_euler','ref_vel','ref_accel','ref_pos', 'gyro', 'accel', 'ref_att_euler'])

if __name__ == '__main__':
    test_path_gen()
