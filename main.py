#Braden Leach, PJ VanDussen
#januray 6 2025
#Keyword and Postitional arguments



#----1----#

def show_full_name(first_name,last_name):
    print(f'{first_name.capitalize() } {last_name.capitalize()}')
show_full_name('billy','joe')

#----2----#

def calculate_time(speed,distance):
    time = distance / speed
  
    if speed <= 0 or distance < 0: 
      print('One of the values you entered was invalid')

    else: 
     print(f'at {speed} mph, it will take {time:.2f} hours to drive {distance} miles.')
    
calculate_time(distance= 5,speed=3)

