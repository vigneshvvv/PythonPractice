sampleSet = {"Hi", "Hello", "Welcome", "hi"}
print(type(sampleSet))
print(sampleSet)

#adding values in set
sampleSet.add("NewProject")
print(sampleSet)

#removing values in set
sampleSet.remove("Welcome")
print(sampleSet)

#updating values in set
sampleSet.update(["Welcome", "forPython"])
print(sampleSet)

#to check for element in set if present print value exist else print doesn't exist
result = False
for i in sampleSet:
    if(i == "HelloN"):
       result = True

if(result):
    print("value Exist")
else:
    print("value doesn't exist")

#short form to check element in set
if "Hello" in sampleSet:
    print("The given value exist")


vivoSpec = {"6GB RAM", "128GB ROM", "Bluetooth", "5G"}
nothingSpec = {"8GB RAM", "64GB ROM", "Bluetooth", "4G"}

all_feature = vivoSpec | nothingSpec

print(all_feature)

repeatedElement = vivoSpec & nothingSpec
print(repeatedElement)

vivoAlteredSpec = vivoSpec - nothingSpec
print(vivoAlteredSpec)

remainingElement = vivoSpec ^ nothingSpec
print(remainingElement)

numList = [10,20,10,30,20]
converted = set(numList)
print(converted)
numList = list(converted)
print(numList)

convertedNew = list(set(numList))
print(convertedNew)

locations = {
    (42.44, 83.044),
    (40.01, 85.33),
    (42.44, 83.044)
}

print(locations)
newlocation = (20.22, 44.33)
locations.add(newlocation)
print(locations)
