from calculation_loop import main_measurement_loop

def main():

    Chest,Waist,Hipps,Inseem,arm = main_measurement_loop(175,"./video/front.mp4","./video/side.mp4")

if __name__ == "__main__":
    main()