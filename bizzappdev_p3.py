# Declaring variables to calculate the time and distance
# "distance" = distance need to be covered
# "distance_covered" = at starting time
# "gap" = gap between two cockroaches
# "time_in_second" = showing time in seconds
# "cockroach_1" = distance covered by cockroach_1
# "cockroach_2" = distance covered by cockroach_2

class calculation:
    def total_distance_and_time_taken(distance):
        distance_covered = 0
        gap = distance
        time_in_second = 1
        cockroach_1 = 0
        cockroach_2 = distance

        while True:
            if time_in_second % 10 == 0:
                # Calculation for every 10 seconds
                cockroach_1 -= 2
                cockroach_2 += 1
                distance_covered += 3
            elif time_in_second % 5 == 0:
                # Calculation for every 5 seconds
                cockroach_1 += 1
                cockroach_2 += 1
                distance_covered += 2
            else:
                # Calculation for every seconds
                cockroach_1 += 1
                cockroach_2 -= 2
                distance_covered += 3
            gap = cockroach_2 - cockroach_1
            if gap < 1:
                # When they meet each other
                break
            # To Display every second info
            # print(str("--Distance Covered in {} second--").format(time_in_second))
            # print("Distance Covered by 'Cockroach 1' ",cockroach_1,"m")
            # print("Distance Covered by 'Cockroach 2' ",(100-cockroach_2),"m")
            # print("Total distance covered by both cockroaches",distance_covered,"m")
            time_in_second += 1
        data= {
            "time":time_in_second,
            "distance":distance_covered,
        }

        return data

# Creating Class Object to access that function which will calculate the value
class_obj = calculation
output=class_obj.total_distance_and_time_taken(100)
print(str("Total Time taken by both cockroaches {} seconds and distance covered by {} m").format(output['time'], output['distance']))
