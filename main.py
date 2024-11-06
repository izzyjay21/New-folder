from array import *


arr = array("i", [1,2,3,4,5,6])
 
def array_rotation(arr,shift):
    for i in range(0,shift):
        temp = arr[len(arr) - 1]
        for j in range(len(arr) - 1, 0 , - 1):
          arr[j] = arr[j - 1]
        arr [0] = temp 

    return arr        

print(array_rotation(arr,6))