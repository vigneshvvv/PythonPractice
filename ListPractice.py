sample = [10,30,40,50]

print(sample)
sample2 = [50,60,70,80]

#to combine two list
# sample = sample+sample2
sample.extend(sample2)
print(sample)


#to add value to the end of the list
sample3 = [10,20,30,40,50]
sample3.append(60)
print("sample 3 value is", sample3)
print(len(sample3))

#To get the values using index from list
print(sample3[0])

#printing last element of list
num = len(sample3) -1
print(sample3[len(sample3) -1])


#inserting the value based on index
valueSample = [100,200,300,400, 200]
valueSample.insert(1, 50)
# valueSample.remove(30)
valueSample.pop(4)
print(valueSample)

#to find the index of element in list
print(valueSample.index(200))

#to replace the value in index of list
valueSample[0]= 30
print(valueSample)

#To count the number of values in the list
print(valueSample.count(200))


#to wipeout the entire values in the list
valueSample.clear()
print(valueSample)

sam = [17, 15, 1,22]
print(sam[-4])

#to arrange elements in asc order
sam.sort()
print(sam)

#to arrange the elements in Desc order
sam.sort(reverse= True)
print(sam)

#arrange string list in asc order
stringContent = ["Hi", "Welcome", "To", "Python", "Class"]
stringContent.sort()
print(stringContent)

print(stringContent[0][0])

nestedList = [[1,3,5,7], [22,24,27,25], [33, 34,36, 38]]
print(nestedList[-1][-1])
print(len(nestedList[0]))

# sampleList = []
sampleList = list()
sampleList.append(nestedList[0][0])
print(sampleList)









