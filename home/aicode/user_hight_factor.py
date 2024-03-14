
def cm_factor_func(mask_np,image_mask_width,numpydata,User_hight):

    nose_location_y = int(mask_np[0][1])

    ankle_location_1_y = int(mask_np[15][1])
    ankle_location_2_y = int(mask_np[16][1])

    image_mask_hight = numpydata.shape[0]


    nose_location_x = int(mask_np[0][0])
    start_condition = 0
    for i in range(0,image_mask_hight -5):
        current_location_value = abs(numpydata[i][nose_location_x])
        #print("current_location_value",current_location_value)
        if current_location_value > 0 and abs(numpydata[i][nose_location_x]) > 1 and abs(numpydata[i][nose_location_x]) > 1:
            if start_condition == 0:
                start_mes = i
                start_condition = 1
                head_tip_location = start_mes
                print("head_tip_location",head_tip_location)
                

    ankle_location_1_x = int(mask_np[15][0])            
    start_condition = 1
    for i in range(ankle_location_1_y,image_mask_hight - 5):
        current_location_value = abs(numpydata[i][ankle_location_1_x])
        if current_location_value < 1 and abs(numpydata[i+1][ankle_location_1_x]) < 1 and abs(numpydata[i+2][ankle_location_1_x]) < 1:
            if start_condition == 1:
                end_mes = i
                legs_tip_location_1 = end_mes
                start_condition = 0

                
    ankle_location_2_x = int(mask_np[16][0])            
    start_condition = 1
    for i in range(ankle_location_2_y,image_mask_hight - 5):
        current_location_value = abs(numpydata[i][ankle_location_2_x])
        if current_location_value < 1 and abs(numpydata[i+1][ankle_location_1_x]) < 1 and abs(numpydata[i+2][ankle_location_1_x]) < 1:
            if start_condition == 1:
                end_mes = i
                legs_tip_location_2 = end_mes
                start_condition = 0

    legs_tip_location = max(legs_tip_location_1, legs_tip_location_2)#(legs_tip_location_1+legs_tip_location_2)/2
    man_hight_calculated = abs(legs_tip_location-head_tip_location)
    
    User_hight = float(User_hight)
    cm_value_factor = User_hight/man_hight_calculated
                        

    return cm_value_factor,nose_location_x,nose_location_y,head_tip_location,legs_tip_location,man_hight_calculated