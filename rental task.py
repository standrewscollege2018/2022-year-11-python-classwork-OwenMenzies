''' rental cars '''
ask = True
error = False 
car_confirmation = True
start = True 
#global variables
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seats =["2","4","4","4","4","4","7","12","12"]
availability = ["avalible", "available", "available", "available", "available", "available", "available", "available", "available"]
#set up lists
#availability[1] = "unavailable" 
car = len(cars)

while start == True:
    for i in range(1,car+1):
        print (f"{i}. {cars[i-1]} - {seats[i-1]} seats {availability[i-1]}")
    print("What car would you like to resserve?(number)")
    ask = True
    while ask == True:
        try:
            choice = int(input())
            if choice > 9 or choice < 1:
                print("please enter a digit between 1 and 9")
            else:
                ask = False 
                car_confirmation = True
                while car_confirmation == True:
                    print("are you sure you want to reserve this car?(yes or no)")
                    error = False
                    yes_no = input()
                    yes_no.lower()
                    for i in yes_no:
                        if (i.isalpha()):
                            pass
                        else:
                            error = True

                    if error == False:
                        if yes_no == "no":
                            car_confirmation = False
                            ask = False 
                        elif yes_no == "yes":
                            car_confirmation = False
                        else:
                            print("please enter either yes or no")
                    else:
                        print("please enter yes or no and only letters in the english alphabet")
                            
                    
        except ValueError:
            print("please enter a digit between 1 and 9")
           
     
