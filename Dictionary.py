my_car = {
    "name": "Fiesta",
    "brand": "FORD",
    "CC": "1500",
    "ModelYear": 2026
}

print(my_car)
print(type(my_car))

#to get value using key
print(my_car["ModelYear"])

#getting value using get method
print(my_car.get("name"))

#Setting Default value to return incase key not present
print(my_car.get("vin", "Key Not Available"))

my_car["ModelYear"] = 2025
print(my_car)
print(my_car["ModelYear"])

my_car.pop("CC")

print(my_car)

#To remove key value
my_car.popitem()
print(my_car)

#to print keys alone
print(my_car.keys())

#to print values alone
print(my_car.values())

print(my_car.items())

# CarInfo = dict()

#Creating Empty dict
CarInfo = {}

#Adding key value to Dict
CarInfo["CarName"] = "Mustang"

print(CarInfo)

#Updating value to Dict
CarInfo.update({
    "Brand": "FORD",
    "IsEv": True,
    "vin": "efswq233243",
    "ModelYear": 2025,
    "Delivered": False,
    25: "NO"
})

print(CarInfo)

#updating single value using key
CarInfo.update(ModelYear = "2024")
print(CarInfo)
