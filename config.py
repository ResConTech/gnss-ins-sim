""" config.py configuration parameters for the simulator"""

import os
from ANSI_color import *

class config():
 
    def __init__(self):
        self.user = os.getlogin()
        
        imu_rc_path = "/home/{}/rescon/IMU_RC/sim_data".format(self.user)
        if(os.path.exists(imu_rc_path)):
            self.IMU_RC_PATH = imu_rc_path
        else:
            print("{}Could not find path: {}. Is the IMU_RC repository installed?{}".format(WARNING,imu_rc_path,ENDC))
            self.IMU_RC_PATH = ""

        ekf_path = "/home/{}/rescon/EKF/sim_data".format(self.user)
        if(os.path.exists(ekf_path)):
            self.EKF_PATH = ekf_path
        else:
            print("{}Could not find path: {}. Is the EKF repository installed?{}".format(WARNING,ekf_path,ENDC))
            self.EKF_PATH = ""
