# Array manipulation
first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []
print(first_list)
while first_list:
    num = first_list.pop()
    inverse_list.append(num)
    
print(inverse_list)

# Implementing function
def reversed_array(first_list):
    first_list = [0,1,2,3,4,5,6,7,8,9]
    inverse_list = []
    while first_list:
        num = first_list.pop()
        inverse_list.append(num)
    return inverse_list
reversed_list = reversed_array(first_list.copy())
print(reversed_list)




    

   
    
    






 