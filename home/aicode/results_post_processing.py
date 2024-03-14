import numpy as np
import numpy as np
from numpy import asarray


def level_cm_front(cm_value_factor_10_front,width_mes_1_front,width_mes_2_front,width_mes_3_front,width_mes_4_front,inseem_mes_5_front,inseem_mes_6_front,arm_mes_7_front,arm_mes_8_front):

    sholder_level_cm_front = np.array(width_mes_1_front) * np.array(cm_value_factor_10_front)
    Chest_cm_front = np.array(width_mes_2_front) * np.array(cm_value_factor_10_front)
    Waist_cm_front = np.array(width_mes_3_front) * np.array(cm_value_factor_10_front)
    Hipps_cm_front = np.array(width_mes_4_front) * np.array(cm_value_factor_10_front)
    Inseem_1_cm_front = np.array(inseem_mes_5_front) * np.array(cm_value_factor_10_front)
    Inseem_2_cm_front = np.array(inseem_mes_6_front) * np.array(cm_value_factor_10_front)
    arm_1_cm_front = np.array(arm_mes_7_front) * np.array(cm_value_factor_10_front)
    arm_2_cm_front = np.array(arm_mes_8_front) * np.array(cm_value_factor_10_front)
                        
    return sholder_level_cm_front,Chest_cm_front,Waist_cm_front,Hipps_cm_front,Inseem_1_cm_front,Inseem_2_cm_front,arm_1_cm_front,arm_2_cm_front
    
    

def level_cm_side(cm_value_factor_10_side,width_mes_1_side,width_mes_2_side,width_mes_3_side,width_mes_4_side,inseem_mes_5_side,inseem_mes_6_side,arm_mes_7_side,arm_mes_8_side):

    sholder_level_cm_side = np.array(width_mes_1_side) * np.array(cm_value_factor_10_side)
    Chest_cm_side = np.array(width_mes_2_side) * np.array(cm_value_factor_10_side)
    Waist_cm_side = np.array(width_mes_3_side) * np.array(cm_value_factor_10_side)
    Hipps_cm_side = np.array(width_mes_4_side) * np.array(cm_value_factor_10_side)
    Inseem_1_cm_side = np.array(inseem_mes_5_side) * np.array(cm_value_factor_10_side)
    Inseem_2_cm_side = np.array(inseem_mes_6_side) * np.array(cm_value_factor_10_side)
    arm_1_cm_side = np.array(arm_mes_7_side) * np.array(cm_value_factor_10_side)
    arm_2_cm_side = np.array(arm_mes_8_side) * np.array(cm_value_factor_10_side)
                        
    return sholder_level_cm_side,Chest_cm_side,Waist_cm_side,Hipps_cm_side,Inseem_1_cm_side,Inseem_2_cm_side,arm_1_cm_side,arm_2_cm_side