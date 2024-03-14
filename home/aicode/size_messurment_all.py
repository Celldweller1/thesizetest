import numpy as np
import cv2
import numpy as np
from PIL import Image
from numpy import asarray

from .level_measurement import sholder_level_func, Chest_level_func, Waist_level_func, Hips_level_func, Inseem_length_func, Arms_length_func 
from .user_hight_factor import cm_factor_func


def size_messurment_func(chest_persentage,Waist_persentage,counter,calculation_frames,frame,name,input_value,width,height,fps,User_hight,model,model_pose,width_mes_1,width_mes_2,width_mes_3,width_mes_4,inseem_mes_5,inseem_mes_6,arm_mes_7,arm_mes_8,length_man_9,cm_value_factor_10,User_hight_array_11):
    data_arr_names = ['sholder_level','Chest','Waist','Hipps','Inseem_1','Inseem_2','arm_1','arm_2','human_length','cm_value_factor_10','User_hight']
    
    if counter % calculation_frames == 0:
                    checks_number = 0
                    
                    # seg estimation
                    try:
                        istance_results = model.predict(source = frame, save=False, classes = [0])
                    
                        istance_result = istance_results[0]
                        masks = istance_result.masks
                        mask1 = masks[0]
                        mask1 = mask1.cpu()
                        mask = mask1.data[0].numpy()
                        polygon = mask1.xy[0]
                        pts=  np.array(polygon, np.int32)
                        isClosed = True 
                        color = (0, 0, 255)
                        thickness = 2
                        cv2.polylines(frame, [pts],isClosed, color, thickness)
                    except:
                        print("seg not detected")
                        
                    
                    # pose estimation
                    try:
                        results_pose = model_pose.predict(source = frame, save=False, classes = [0])
                        masks = results_pose[0].keypoints
                        masks = masks.cpu()
                        mask_np = masks.data[0].numpy()
                    except:
                        print("pos not detected")
                    
                    
                    
                    # write messurment estimation
                    try:
                    
                        font = cv2.FONT_HERSHEY_SIMPLEX

                        mask_img = Image.fromarray(mask, "I")
                        newsize = (width, height)
                        mask_img = mask_img.resize(newsize)
                        numpydata = asarray(mask_img)
                        image_mask_width = numpydata.shape[1]
                        
                        #print("image_mask_width", image_mask_width)
                        #print("mask_np", mask_np)
                        #print("numpydata", numpydata)

                        ### location of sholder level #
                        messurment_location,messurment_value,start_mes,end_mes = sholder_level_func(mask_np,image_mask_width,numpydata)
                        #print("messurment_location", messurment_location)
                        #print("messurment_value", messurment_value)
                        #print("start_mes", start_mes)
                        #print("end_mes", end_mes)

                        #print(mask_np[5][1])
                        cv2.line(frame,(0, int(messurment_location)),(width, int(messurment_location)),(0,0,0),2)
                        width_mes_1_value = messurment_value
                        checks_number += 1
                        input_text = str(messurment_value)
                        cv2.putText(frame,input_text,(0, int(messurment_location)), font,1,(0,0,0),2)
                        cv2.line(frame,(int(start_mes), 0),(int(start_mes), height),(0,0,0),2)
                        cv2.line(frame,(int(end_mes), 0),(int(end_mes), height),(0,0,0),2)


                        #Chest #
                        messurment_location,messurment_value,start_mes,end_mes = Chest_level_func(mask_np,image_mask_width,numpydata,chest_persentage)
                        cv2.line(frame,(0, int(messurment_location)),(width, int(messurment_location)),(255,0,0),2)
                        width_mes_2_value = messurment_value
                        checks_number += 1
                        input_text = str(messurment_value)
                        cv2.putText(frame,input_text,(0, int(messurment_location)), font,1,(255,0,0),2)
                        cv2.line(frame,(int(start_mes), 0),(int(start_mes), height),(255,0,0),2)
                        cv2.line(frame,(int(end_mes), 0),(int(end_mes), height),(255,0,0),2)


                        #Waist
                        messurment_location,messurment_value,start_mes,end_mes = Waist_level_func(mask_np,image_mask_width,numpydata,Waist_persentage)
                        cv2.line(frame,(0, int(messurment_location)),(width, int(messurment_location)),(0,255,0),2)
                        width_mes_3_value = messurment_value
                        checks_number += 1
                        input_text = str(messurment_value)
                        cv2.putText(frame,input_text,(0, int(messurment_location)), font,1,(0,255,0),2)
                        cv2.line(frame,(int(start_mes), 0),(int(start_mes), height),(0,255,0),2)
                        cv2.line(frame,(int(end_mes), 0),(int(end_mes), height),(0,255,0),2)


                        #Hips
                        messurment_location,messurment_value,start_mes,end_mes = Hips_level_func(mask_np,image_mask_width,numpydata)
                        #print(mask_np[5][1])
                        cv2.line(frame,(0, int(messurment_location)),(width, int(messurment_location)),(0,0,255),2)
                        width_mes_4_value = messurment_value
                        checks_number += 1
                        input_text = str(messurment_value)
                        cv2.putText(frame,input_text,(0, int(messurment_location)), font,1,(0,0,255),2)
                        cv2.line(frame,(int(start_mes), 0),(int(start_mes), height),(0,0,255),2)
                        cv2.line(frame,(int(end_mes), 0),(int(end_mes), height),(0,0,255),2)

                        #Inseem
                        Inseem_length_1,Inseem_length_2 = Inseem_length_func(mask_np)
                        cv2.line(frame,(int((mask_np[11][0])), int((mask_np[11][1]))),(int((mask_np[13][0])), int((mask_np[13][1]))),(0,255,255),5)
                        cv2.line(frame,(int((mask_np[13][0])), int((mask_np[13][1]))),(int((mask_np[15][0])), int((mask_np[15][1]))),(0,255,255),5)
                        inseem_mes_5_value = Inseem_length_1
                        checks_number += 1
                        cv2.line(frame,(int((mask_np[12][0])), int((mask_np[12][1]))),(int((mask_np[14][0])), int((mask_np[14][1]))),(0,255,255),5)
                        cv2.line(frame,(int((mask_np[14][0])), int((mask_np[14][1]))),(int((mask_np[16][0])), int((mask_np[16][1]))),(0,255,255),5)
                        inseem_mes_6_value = Inseem_length_2
                        checks_number += 1


                        #Arms lengths
                        arm_length_1,arm_length_2 = Arms_length_func(mask_np)
                        cv2.line(frame,(int((mask_np[5][0])), int((mask_np[5][1]))),(int((mask_np[7][0])), int((mask_np[7][1]))),(0,255,255),5)
                        cv2.line(frame,(int((mask_np[7][0])), int((mask_np[7][1]))),(int((mask_np[9][0])), int((mask_np[9][1]))),(0,255,255),5)
                        arm_mes_7_value = arm_length_1
                        checks_number += 1
                        cv2.line(frame,(int((mask_np[6][0])), int((mask_np[6][1]))),(int((mask_np[8][0])), int((mask_np[8][1]))),(0,255,255),5)
                        cv2.line(frame,(int((mask_np[8][0])), int((mask_np[8][1]))),(int((mask_np[10][0])), int((mask_np[10][1]))),(0,255,255),5)
                        arm_mes_8_value = arm_length_2
                        checks_number += 1
                        
                        
                        
                        # DETECT THE HIGHT (How tall in pixels) of the person 
                        cv2.line(frame,(int((mask_np[0][0])), int((mask_np[0][1]))),(int((mask_np[15][0])), int((mask_np[16][1]))),(125,0,125),2)
                        cv2.line(frame,(int((mask_np[0][0])), int((mask_np[0][1]))),(int((mask_np[16][0])), int((mask_np[16][1]))),(125,0,125),2)
                        cm_value_factor,nose_location_x,nose_location_y,head_tip_location,legs_tip_location,man_hight_calculated = cm_factor_func(mask_np,image_mask_width,numpydata,User_hight)
                        length_man_9_value = man_hight_calculated
                        checks_number += 1
                        cm_value_factor_10_value = cm_value_factor
                        checks_number += 1
                        cv2.line(frame,(int(nose_location_x), int(head_tip_location)),(int(nose_location_x), int(legs_tip_location)),(125,0,125),2)
                        input_text = str(man_hight_calculated)
                        cv2.putText(frame,input_text,(int(nose_location_x), int(nose_location_y)), font,1,(125,0,125),2)
                        number_of_columns = len(data_arr_names)
                        print("number_of_columns",number_of_columns)
                        print("checks_number", checks_number)
                        
                        ##########################################################
                        if int(checks_number) == int(number_of_columns-1) : 
                            cm_value_factor_10.append(cm_value_factor_10_value)
                            length_man_9.append(length_man_9_value)
                            arm_mes_8.append(arm_mes_8_value)
                            arm_mes_7.append(arm_mes_7_value)
                            inseem_mes_6.append(inseem_mes_6_value)
                            inseem_mes_5.append(inseem_mes_5_value)
                            width_mes_4.append(width_mes_4_value)
                            width_mes_3.append(width_mes_3_value)
                            width_mes_2.append(width_mes_2_value)
                            width_mes_1.append(width_mes_1_value)
                            User_hight_array_11.append(User_hight)

                    except:
                        print("messurment not detected")
                        # Record the values:
                        # Mes_1 : sholder level
                        width_mes_1.append(0)
                        # Mes_2 : Chest
                        width_mes_2.append(0)
                        # Mes_3 : Waist 
                        width_mes_3.append(0)
                        # Mes_4 : Hipps
                        width_mes_4.append(0)
                        # Mes_5 : Inseem_1
                        inseem_mes_5.append(0)
                        # Mes_6 : Inseem_2
                        inseem_mes_6.append(0)
                        # Mes_7 : arm_1
                        arm_mes_7.append(0)
                        # Mes_8 : arm_2
                        arm_mes_8.append(0)
                        # human _ length
                        length_man_9.append(0)
                        # cm_value_factor_10
                        cm_value_factor_10.append(0)
                        # User_hight_array
                        User_hight_array_11.append(0)
                    
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    input_text_2 = str(width) + "X" + str(height)
                    cv2.putText(frame,input_text_2,(int(width*0.05), int(height*0.99)), font,1,(0,255,255),2)
                    
                    
                    ## Draw a diagonal blue line with thickness of 5 px
                    start_line1= int(width/2) + int(0.3*width/2) 
                    start_line2= int(width/2) - int(0.3*width/2) 
                    cv2.line(frame,(start_line1,0),(width,height),(255,0,255),3)
                    cv2.line(frame,(start_line2,0),(0,height),(255,0,255),3)
                    cv2.ellipse(frame,(int(width/2),int(height*0.8)),(int(width*0.45),50),0,0,180,(255,0,255),3)

                    # Draw input name and value on the frame
                    text_name = f"Name: {name}"
                    cv2.putText(frame, text_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    duble_input_value=input_value*2
                    text_hight = f"Value: {duble_input_value}"
                    cv2.putText(frame, text_hight, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
    return frame,width_mes_1,width_mes_2,width_mes_3,width_mes_4,inseem_mes_5,inseem_mes_6,arm_mes_7,arm_mes_8,length_man_9,cm_value_factor_10,User_hight_array_11

