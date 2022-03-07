''' rental cars '''
cars = ["Toyota Corolla", "Honda CRV", "Suzuki Swift", "Suzuki Swift", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seats =["4","4","4","4","4","7","12","12"]
availability = ["available", "available", "available", "available", "available", "available", "available", "available"]
#set up lists
#availability[1] = "unavailable" 
car = len(cars)
for i in range(1,car+1):
    print (f"{i}. {cars[i-1]} - {seats[i-1]} seats {availability[i-1]}")
print("What car would you like to resserve?(number)")
choice = input()
choice.lower() 
for i in range(1,car+1):
    
    
    