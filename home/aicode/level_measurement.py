import numpy as np
from numpy import asarray
import math


def sholder_level_func(mask_np,image_mask_width,numpydata):
    messurment_location = int((int(mask_np[5][1])+int(mask_np[6][1]))/2)
    start_condition = 0
    
    for i in range(0,image_mask_width-5):
        current_location_value = abs(numpydata[messurment_location][i])
        #print("current_location_value",current_location_value)
        if current_location_value > 0:
            if start_condition == 0:
                start_mes = i
                start_condition = 1

        if current_location_value < 1 and abs(numpydata[messurment_location][i+1]) < 1 and abs(numpydata[messurment_location][i+2])<1:
            if start_condition == 1:
                end_mes = i
                start_condition = start_condition+1
    messurment_value = end_mes-start_mes

    return messurment_location,messurment_value,start_mes,end_mes
    
    
def Chest_level_func(mask_np,image_mask_width,numpydata,chest_persentage):
    upper_level = (int(mask_np[5][1])+int(mask_np[6][1]))/2
    lower_level = (int(mask_np[11][1])+int(mask_np[12][1]))/2

    messurment_location = int((abs(lower_level-upper_level)*chest_persentage)+upper_level)

    start_condition = 0
    for i in range(0,image_mask_width-5):
        current_location_value = abs(numpydata[messurment_location][i])
        if current_location_value > 0:
            if start_condition == 0:
                start_mes = i
                start_condition = 1

        if current_location_value < 1 and abs(numpydata[messurment_location][i+1]) < 1 and abs(numpydata[messurment_location][i+2])< 1:
            if start_condition == 1:
                end_mes = i
                start_condition = start_condition+1

    messurment_value = end_mes-start_mes
                        
    return messurment_location,messurment_value,start_mes,end_mes
    
    
    
def Waist_level_func(mask_np,image_mask_width,numpydata,Waist_persentage):
    upper_level = (int(mask_np[5][1])+int(mask_np[6][1]))/2
    lower_level = (int(mask_np[11][1])+int(mask_np[12][1]))/2

    messurment_location = int((abs(lower_level-upper_level)*Waist_persentage)+upper_level)

    start_condition = 0
    for i in range(0,image_mask_width-5):
        current_location_value = abs(numpydata[messurment_location][i])
        if current_location_value > 0:
            if start_condition == 0:
                start_mes = i
                start_condition = 1


        if current_location_value < 1 and abs(numpydata[messurment_location][i+1]) < 1 and abs(numpydata[messurment_location][i+2])< 1:
            if start_condition == 1:
                end_mes = i
                start_condition = start_condition+1

    messurment_value = end_mes-start_mes
                        
    return messurment_location,messurment_value,start_mes,end_mes   
    
    
def Hips_level_func(mask_np,image_mask_width,numpydata):
    
    lower_level = (int(mask_np[11][1])+int(mask_np[12][1]))/2

    messurment_location = int(lower_level)

    start_condition = 0
    for i in range(0,image_mask_width - 5):
        current_location_value = abs(numpydata[messurment_location][i])
        if current_location_value > 0:
            if start_condition == 0:
                start_mes = i
                start_condition = 1

        if current_location_value < 1 and abs(numpydata[messurment_location][i+1]) < 1 and abs(numpydata[messurment_location][i+2])< 1:
            if start_condition == 1:
                end_mes = i
                start_condition = start_condition+1
    messurment_value = end_mes-start_mes
                        
    return messurment_location,messurment_value,start_mes,end_mes  


def Inseem_length_func(mask_np):
    
    hipps_knee_length_1 =math.sqrt((((mask_np[11][1])-(mask_np[13][1]))**2)+(((mask_np[11][0])-(mask_np[13][0]))**2))
    knee_ankle_length_1 =math.sqrt((((mask_np[15][1])-(mask_np[13][1]))**2)+(((mask_np[15][0])-(mask_np[13][0]))**2))
    Inseem_length_1 = hipps_knee_length_1+knee_ankle_length_1

    hipps_knee_length_2 =math.sqrt((((mask_np[12][1])-(mask_np[14][1]))**2)+(((mask_np[12][0])-(mask_np[14][0]))**2))
    knee_ankle_length_2 =math.sqrt((((mask_np[16][1])-(mask_np[14][1]))**2)+(((mask_np[16][0])-(mask_np[14][0]))**2))
    Inseem_length_2 = hipps_knee_length_2+knee_ankle_length_2
                        
    return Inseem_length_1,Inseem_length_2
    
    
def Arms_length_func(mask_np):
    
    sholder_elbow_length_1 =math.sqrt((((mask_np[5][1])-(mask_np[7][1]))**2)+(((mask_np[5][0])-(mask_np[7][0]))**2))
    elbow_weist_length_1 =math.sqrt((((mask_np[9][1])-(mask_np[7][1]))**2)+(((mask_np[9][0])-(mask_np[7][0]))**2))
    arm_length_1 = sholder_elbow_length_1+elbow_weist_length_1

    sholder_elbow_length_2 =math.sqrt((((mask_np[6][1])-(mask_np[8][1]))**2)+(((mask_np[6][0])-(mask_np[8][0]))**2))
    elbow_weist_length_2 =math.sqrt((((mask_np[10][1])-(mask_np[8][1]))**2)+(((mask_np[10][0])-(mask_np[8][0]))**2))
    arm_length_2 = sholder_elbow_length_2+elbow_weist_length_2
                        
    return arm_length_1,arm_length_2
    
    
    