''' rental cars '''
cars = ["Toyota Corolla", "Honda CRV", "Suzuki Swift", "Suzuki Swift", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ac"]
seats =["4","4","4","4","4","7","12","12"]
print 
car = len(cars)
for i in range(1,car+1):
    print (f"{i}. {cars[i-1]} - {seats}")