def confirm_trip():
  """
  This function asks the user to confirm their trip.

  Returns:
    A string that represents the user's confirmation.
  """
  user_input = input("Enter any character to confirm your trip: ")

  return user_input


def lining_algo():
  
    """
    This function implements a lining algorithm.

    Args:
    None.

    Returns:
    None.
    """
    driver_details = {}
    # Initialize the current car ID and capacity.
    all_cars = 3
    driver_details["all_cars"] = all_cars
    makings = 0
    current_car_id = 0
    current_capacity = 0
    while current_car_id < all_cars:
        print(current_car_id)
        driver_details["current_car_id"] = current_car_id
        driver_details["makings"] = makings
    # Loop until the car is full.
        while current_capacity < 14:
            # Ask the user to confirm their trip.
            confirmation = confirm_trip()

            # If the user confirms their trip, increase the capacity and print the new capacity.
            if confirmation == "a":
                current_capacity += 1
                print(current_capacity)
                print(driver_details)
        
        if current_capacity == 14:
            current_car_id += 1
            makings += 200
            current_capacity = 0
            
        
            # If the capacity is full, increment the current car ID.
    


if __name__ == "__main__":
  lining_algo()