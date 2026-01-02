sample = (100, 200, 300, 400)
print(type(sample))
print(sample[2])
# sample[0] = 150

#converting tuple to list
temp_list = list(sample)
temp_list[0] = 150
print(temp_list)

#converting list to tuple
sample1 = tuple(temp_list)
print(sample1)

#merging two tuple

# sample1 += (500,)
sample1 = sample1+ (500,)
print(sample1)


#replacing the existing tuple with new one 
sample2 = (6, 3,4,5)
sample2 = (3,3,4,5)
print(sample2)
# print(sampl2[-1])

#To iterate tuple using index
for i in range(len(sample2)):
    print(sample2[i])

#to print all the element inside the tuple
for x in sample2:
    print(x)

#To check whether the nnumber 4 present in the tuple or not
for sam in sample2:
    if(sam == 4):
        print("The value present in the tuple", sam)
