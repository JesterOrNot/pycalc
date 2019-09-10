def acceleration():
    initial_velocity = float(input("What is the initial velocity?: "))
    final_velocity = float(input("What is the final velocity?: "))
    starting_time = float(input("What is the starting time?: "))
    ending_time = float(input("What is the ending time?: "))
    delta_t = ending_time - starting_time
    delta_v = final_velocity - initial_velocity
    acceleration = delta_v/delta_t
    print(f"acceleration = {acceleration} m/s")
acceleration()