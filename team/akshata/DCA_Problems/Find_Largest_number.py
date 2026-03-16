
# given a list, find the largest number in the list
# input_list = [1,5,66,8,78,19,22,36] 

input_list = [1,5,66,8,78,19,22,36]
largest = input_list[0]
for num in input_list:
    if num > largest:
        largest = num
print("Largest number is : ",largest)
