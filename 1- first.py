# input: list of numbers
# output: two lists 
#           - list of numbers odd
#           - list of numbers low

'''
    - write: Enter the numbers
    - Read: list of numbers
    - pross: 


'''

even_num = [] 
odd_num = []

for x in range(50):
    if x%2==0 :
        even_num.append(x)
    
    else:
        odd_num.append(x)


print(f"evenNumbers : {even_num}")
print(f"oddNumbers : {odd_num}")



# nums = list(input("enter the numbers: ")) # get from user list of intger
# even_num = [] 
# odd_num = []

# for x in :
#     if x%2==0 :
#         even_num.append(x)
    
#     else:
#         odd_num.append(x)


# print(f"evenNumbers : {even_num}")
# print(f"oddNumbers : {odd_num}")
