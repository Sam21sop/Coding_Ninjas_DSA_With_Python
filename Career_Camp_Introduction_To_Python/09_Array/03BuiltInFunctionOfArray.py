from array import array

#create array using build in module
user_input = list(map(int, input().split()))
arr = array('I', user_input)
print(arr)

#append elements
arr.append(9)
print('append', arr)


#count element
print('count', arr.count(3))


#find index of element
print('Index:', arr.index(9))

#extend/add n number of element in array 
arr.extend([9, 7, 0])
print("Extend:", arr)

#insert element at specific index
arr.insert(0, 78)
print('insert:', arr)