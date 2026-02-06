from pydantic import BaseModel

data ={
    "name": "IT pvt ltd",
    "location": {"country": "India", "state": "TamilNadu"}
}


class location_base(BaseModel):
    country: str
    state: str  

class company(BaseModel):
    name: str
    location: location_base 



companyProfile = company(**data)
print(companyProfile.name)


# To filter Even number from list of numbers
c = [1,2,3,4,5,6]
even = filter(lambda s: s % 2 ==0, c)
print(list(even))

mapFunc = [1,3,5,35,6,4]
result = map(lambda x: x*4, mapFunc)
print(list(result))

models = [

    {"modelName" : "Apple i phone 14", "price": 100000, "Available": 100},
    {"modelName" : "Nothing phone 1", "price": 20000, "Available": 50},
    {"modelName" : "samsung", "price": 60000, "Available": 10}
]

filteredProduct = filter(lambda prod: prod["price"] > 20000, models )
print(list(filteredProduct))




filterdMap = map(lambda sample: sample["modelName"], models)
print(list(filterdMap))

filterdMapNew = map(lambda m: m["price"]*10, models)
print(list(filterdMapNew))
