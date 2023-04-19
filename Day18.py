""" 
Day18: Write a program to sort the elements in the list/array in ascending order.
"""

#Program

arr = [5, 2, 8, 7, 1];     
temp = 0;    
       
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
        
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();       
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");   

    
#Output
    
Elements of original array: 
5 2 8 7 1 
Elements of array sorted in ascending order: 
1 2 5 7 8
