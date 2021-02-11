from array import *

# sizeList = array('i', [2,4,5,6,2])
# print(sizeList.typecode)


unknown_Arr = array('i', [])

Arr_Length = int(input('Length of the Array? '))

for i in range(Arr_Length):
    Arr_Value = int(input('Next Value? '))
    unknown_Arr.append(Arr_Value)
print(unknown_Arr)

user_Arr_search = int(input('Enter the Value Index you like to search? '))


k = 0
for e in unknown_Arr:
    if e==user_Arr_search:
        print(k)
        break
    k+=1




