# Find the angle made by the hour and the minute 
# Hand at any given time. Assume it is an anloag clock

def CalculateAngle(hour,minute):
    if hour < 0 or minute < 0 or hour > 12 or minute > 60:
        print("In valid Inputs given the user:")
        return
    else:
        if hour == 12:
            hour == 0 
        if minute == 60:
            minute == 0
# hour hand rotates 360 degrees in 12 hours 
# 360/12 * 60 ==> 0.5 degrees every minute

# similarity minute hand rotates 360 degrees in one hour i.e.,
# 360/60 ==> 6 degrees every minute

    
        hour_angle = ((hour * 60) + minute) * (360/12)
        minute_angle = minute * (360/60)
# We take the absolute difference
# and then return the acute angle between the two

        
        difference = abs(hour_angle - minute_angle)

        return min(difference, 360 - difference)

input_time = (9,9)
print("The angle between hour and minute hand is:",CalculateAngle(input_time[0],input_time[1]),'\u00b0')






