import sys

def check_acceleration():
    velocity_initial = float(input("Enter the initial velocity (m/s): "))
    velocity_final = float(input("Enter the final velocity (m/s): "))
    time = float(input("Enter the time taken (seconds): "))
    motion_direction = input("Enter the direction of motion (forward/backward): ").strip().lower()

    acceleration = (velocity_final - velocity_initial) / time

    if motion_direction == "forward":
        if acceleration > 0:
            print(f"Acceleration is positive: {acceleration} m/s²")
        elif acceleration < 0:
            print(f"Acceleration is negative: {acceleration} m/s²")
        else:
            print("No acceleration, the object is moving at constant velocity.")
    elif motion_direction == "backward":
        if acceleration > 0:
            print(f"Acceleration is negative (since it's decelerating backward): {-acceleration} m/s²")
        elif acceleration < 0:
            print(f"Acceleration is positive (since it's accelerating backward): {-acceleration} m/s²")
        else:
            print("No acceleration, the object is moving at constant velocity.")
    else:
        print("Invalid direction input. Please enter 'forward' or 'backward'.")
        


check_acceleration()

input("Enter any key to exit... ")
sys.exit()
