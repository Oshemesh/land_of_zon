def median(arr):
    #first sort the array
    arr.sort()
    #get middle position as type int
    middlePosition = int(len(arr)/2)
    
    #figure out if the length is even or odd
    #if the remainder of length of list divided by 2 is 0,
    #theres an even number of elements in the list
    if(len(arr) % 2 == 0):
        return (arr[middlePosition] + arr[middlePosition - 1 ])/2.0
    else:
        #here we know its odd, so just return the middle number        
        return arr[middlePosition]

#
# Code to test our function below
#
arr_odd = [1 , 2 , 3]
arr_even = [ 1 , 2 , 3 , 4 ]

#correct answer for arr_odd is 2
#correct answer for arr_even is 2.5 , since ( 2 + 3 )/2

print(median(arr_odd))
print(median(arr_even))