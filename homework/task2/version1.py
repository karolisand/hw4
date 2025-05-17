
print("Hello world \n")

distance = input("Please enter distance in kilometers: ")

if distance.isdigit():                                              #checks if distance input is a numeric value.
    parsed_distance = float(distance)
    processed_distance = parsed_distance / 1.60934

    print(f"{distance} kilometers is {processed_distance:.2f} miles.")

else:
    print("You should not enter more than just numbers.")