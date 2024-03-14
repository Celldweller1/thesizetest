#import streamlit as st
import os
import numpy as np
import cv2
import numpy as np
from ultralytics import YOLO
import time
import json
from .size_messurment_all import size_messurment_func
from .results_post_processing import level_cm_front, level_cm_side
current_dir = os.getcwd()

# Define the relative path to the "aicode" directory from the current directory
aicode_relative_path = os.path.join(current_dir,'home','aicode','input_data.json')
print(aicode_relative_path)
with open(aicode_relative_path, 'r') as file:
    input_data = json.load(file)


def main_measurement_loop(User_hight,video_path_front,video_path_side):
    
    
    #User_hight = input_data['User_hight_cm']
    name = input_data['User_name']
    #video_path_front = input_data['video_front_location'] 
    #video_path_side = input_data['video_side_location'] 
    shrink_factor = input_data['shrink_factor_value'] 
    
    
    cap = cv2.VideoCapture(video_path_front)
    

    if not cap.isOpened():
        print("Unable to access the camera.")
        return
        
    

    width  = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)    
    print("\n Video size",height, "X", width)
    print("\n Video fram per second",fps,"\n ")
    
    
    
    input_value = 350 # testing value for printing
    
    if User_hight <=0:
        User_hight =10
    print("\n The user hight is",User_hight,"\n ")
    
    seq_model_path = input_data['seq_model_path']
    pose_model_path  = input_data['pose_model_path']
    
    chest_persentage,Waist_persentage = input_data['chest_persentage'],input_data['Waist_persentage']
    
    model = YOLO(seq_model_path)
    model_pose = YOLO(pose_model_path)

 #Calculation is started
    # Record Front imaeg data
    # Mes_1 : sholder level,Mes_2 : Chest,Mes_3 : Waist , Mes_4 : Hipps, Mes_5 : Inseem_1, Mes_6 : Inseem_2, Mes_7 : arm_1, Mes_8 : arm_2, human _ length, cm_value_factor, user hight array
    width_mes_1_front, width_mes_2_front, width_mes_3_front, width_mes_4_front, inseem_mes_5_front, inseem_mes_6_front, arm_mes_7_front, arm_mes_8_front, length_man_9_front, cm_value_factor_10_front, User_hight_array_11_front  = [],[],[],[],[],[],[],[],[],[],[]
    # Record Side imaeg data
    width_mes_1_side,width_mes_2_side,width_mes_3_side,width_mes_4_side,inseem_mes_5_side,inseem_mes_6_side,arm_mes_7_side,arm_mes_8_side,length_man_9_side,cm_value_factor_10_side,User_hight_array_11_side = [],[],[],[],[],[],[],[],[],[],[]
    
    
    calculation_frames = 2
    
    start_time = time.time()
    
    cap.release() # Releases webcam or capture device


    front_one_time = 1
    side_one_time = 1
    final_one_time = 1

    Front_screen_time,Front_data_time,Side_screen_time,Side_data_time = input_data['Front_screen'],input_data['Front_data'],input_data['Side_screen'],input_data['Side_data']
    
    #FRONT measurement 
    cap = cv2.VideoCapture(video_path_front)
    counter = 0
    while True:
        #print("counter  ", counter)
        ret, frame = cap.read()
        frame_out,width_mes_1_front,width_mes_2_front,width_mes_3_front,width_mes_4_front,inseem_mes_5_front,inseem_mes_6_front,arm_mes_7_front,arm_mes_8_front,length_man_9_front,cm_value_factor_10_front,User_hight_array_11_front = size_messurment_func(chest_persentage,Waist_persentage,counter,calculation_frames,frame,name,input_value,width,height,fps,User_hight,model,model_pose,width_mes_1_front,width_mes_2_front,width_mes_3_front,width_mes_4_front,inseem_mes_5_front,inseem_mes_6_front,arm_mes_7_front,arm_mes_8_front,length_man_9_front,cm_value_factor_10_front,User_hight_array_11_front)
        
        if not ret:
            print("End of front video.")
            break 

        counter += 1
    cap.release()   

            
    #SIDE measurement
    cap = cv2.VideoCapture(video_path_side)
    counter = 0
    while True:   
        ret, frame = cap.read()
        frame_out,width_mes_1_side,width_mes_2_side,width_mes_3_side,width_mes_4_side,inseem_mes_5_side,inseem_mes_6_side,arm_mes_7_side,arm_mes_8_side,length_man_9_side,cm_value_factor_10_side,User_hight_array_11_side = size_messurment_func(chest_persentage,Waist_persentage,counter,calculation_frames,frame,name,input_value,width,height,fps,User_hight,model,model_pose,width_mes_1_side,width_mes_2_side,width_mes_3_side,width_mes_4_side,inseem_mes_5_side,inseem_mes_6_side,arm_mes_7_side,arm_mes_8_side,length_man_9_side,cm_value_factor_10_side,User_hight_array_11_side)
            
        if not ret:
            print("End of front video.")
            break 
        
        counter += 1
    cap.release() # Releases webcam or capture device

            
            

    Intial_per = input_data['Intial_pef_results']
    Final_per = input_data['Final_pef_results']
    circumference_factor = input_data['circumference_factor']
    
    Intial_buffer_front = int(Intial_per*len(arm_mes_7_front))
    final_buffer_front =  int(Final_per*len(arm_mes_7_front))
    
    
    cm_value_factor_10_front_eq =  [x * shrink_factor for x in cm_value_factor_10_front]
    sholder_level_cm_front,Chest_cm_front,Waist_cm_front,Hipps_cm_front,Inseem_1_cm_front,Inseem_2_cm_front,arm_1_cm_front,arm_2_cm_front = level_cm_front(cm_value_factor_10_front_eq,width_mes_1_front,width_mes_2_front,width_mes_3_front,width_mes_4_front,inseem_mes_5_front,inseem_mes_6_front,arm_mes_7_front,arm_mes_8_front)

    Intial_buffer_side = int(Intial_per*len(arm_mes_7_side))
    final_buffer_side =  int(Final_per*len(arm_mes_7_side))
    
    #cm_value_factor_10_side_eq = np.full(len(cm_value_factor_10_side), np.mean(cm_value_factor_10_front))
    cm_value_factor_10_side_eq =  [x * shrink_factor for x in cm_value_factor_10_side]

    sholder_level_cm_side,Chest_cm_side,Waist_cm_side,Hipps_cm_side,Inseem_1_cm_side,Inseem_2_cm_side,arm_1_cm_side,arm_2_cm_side  =  level_cm_side(cm_value_factor_10_side_eq,width_mes_1_side,width_mes_2_side,width_mes_3_side,width_mes_4_side,inseem_mes_5_side,inseem_mes_6_side,arm_mes_7_side,arm_mes_8_side)
    
            
            
    Chest_cm_circumference = circumference_factor * (2*np.mean(Chest_cm_front[Intial_buffer_front:final_buffer_front])+2*np.mean(Chest_cm_side[Intial_buffer_side:final_buffer_side]))
    print('Chest_cm_circumference', Chest_cm_circumference)
     
    Waist_cm_circumference = circumference_factor * (2*np.mean(Waist_cm_front[Intial_buffer_front:final_buffer_front])+2*np.mean(Waist_cm_side[Intial_buffer_side:final_buffer_side]))
    print('Waist_cm_circumference', Waist_cm_circumference)
    
    Hipps_cm_circumference = circumference_factor * (2*np.mean(Hipps_cm_front[Intial_buffer_front:final_buffer_front])+2*np.mean(Hipps_cm_side[Intial_buffer_side:final_buffer_side]))
    print('Hipps_cm_circumference', Hipps_cm_circumference)
    
    Inseem_arr = np.array([np.mean(Inseem_1_cm_front[Intial_buffer_front:final_buffer_front]), np.mean(Inseem_2_cm_front[Intial_buffer_front:final_buffer_front])])
    print('Inseem  ', Inseem_arr.mean()/shrink_factor)
    Inseem_final_value = Inseem_arr.mean()/shrink_factor
    
    arm_arr = np.array([np.mean(arm_1_cm_front[Intial_buffer_front:final_buffer_front]),np.mean(arm_2_cm_front[Intial_buffer_front:final_buffer_front])])
    print('arm length  ', arm_arr.mean()/shrink_factor)
    arm_final_value = arm_arr.mean()/shrink_factor
    
    return(Chest_cm_circumference,Waist_cm_circumference,Hipps_cm_circumference,Inseem_final_value,arm_final_value)
