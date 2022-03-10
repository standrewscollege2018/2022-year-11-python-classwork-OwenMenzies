''' rental cars, this program is designed to rent out cars every day'''
ask = True
error = False 
car_confirmation = True
start = False 
day = True
name = True

amount_of_cars = 0
#global variables
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seats =["2","4","4","4","4","4","7","12","12"]
availability = ["avalible", "available", "available", "available", "available", "available", "available", "available", "available"]
names = ["","","","","","","","",""]
#set up lists
#availability[1] = "unavailable" 
car = len(cars)


    
while day == True:
    if amount_of_cars == 8:
        car_confirmation = False
        ask = False
        day = False
        start = False    
        name = True    
    print("would you like to reserve a car?(yes or no)")
    error = False
    car_day = input()
    car_day = car_day.lower()
    for i in car_day:
        if (i.isalpha()):
            pass
        else:
            error = True
    if error == False:
        if car_day == "no":
            car_confirmation = False
            ask = False
            day = False
            start = False
            name = True      
            #set everything to false to make sure that the end occurs
        elif car_day == "yes":
            start = True
            name = False
            #foreshadowing for later on talk
            print("What is your name?")
        else:
            print("please enter either yes or no")
    else:
        print("please enter yes or no and only letters in the english alphabet")  
        

    while name == False:
        error = False
        person_name = input()
        person_name = person_name.lower()
        for i in person_name:
            if (i.isalpha()):
                pass
            else:
                error = True
        if error == False:
            start = True
        else:
            print("please enter your name and only letters in the english alphabet")     
            start = False
        while start == True:
            for i in range(1,car+1):
                print (f"{i}. {cars[i-1]} - {seats[i-1]} seats {availability[i-1]}")
            print("What car would you like to reserve?(number)")
            ask = True
            while ask == True:
                try:
                    choice = int(input())
                    if choice > 9 or choice < 1:
                        print("please enter a digit between 1 and 9")
                    elif availability[choice-1] == "unavailable":
                        print("car is unavailable please reserve a different car")
                    else:
                        ask = False 
                        car_confirmation = True
                        while car_confirmation == True:
                            print("are you sure you want to reserve this car?(yes or no)")
                            error = False
                            yes_no = input()
                            yes_no = yes_no.lower()
                            for i in yes_no:
                                if (i.isalpha()):
                                    pass
                                else:
                                    error = True
        
                            if error == False:
                                if yes_no == "no":
                                    car_confirmation = False
                                    start = False
                                    name = True
                                    ask = False 
                                elif yes_no == "yes":
                                    names[choice] = person_name
                                    car_confirmation = False
                                    name = True  
                                    start = False
                                    ask = False
                                    print("Thank you for your reservation")
                                    availability[choice-1] = "unavailable" 
                                    amount_of_cars = amount_of_cars + 1 
                                else:
                                    print("please enter either yes or no")
                            else:
                                print("please enter yes or no and only letters in the english alphabet")
                                                               
                except ValueError:
                    print("please enter a digit between 1 and 9")
#end of the day checker of how many, if any, cars were booked 
if amount_of_cars == 0:
    print("there were no cars reserved today")
else:
    print(f"today there were {amount_of_cars} cars reserved which were:")
    for i in range(0,9): 
        if availability[i] == "unavailable":
            print(f"{i+1}. {cars[i]} rented by {names[i+1]}")
        