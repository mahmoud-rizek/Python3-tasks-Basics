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
star_num = int(input("Enter start number: "))
end_num = int(input("Enter end number: "))

for x in range(star_num, end_num+1):
    if x%2 == 0 :
        even_num.append(x)
    
    else:
        odd_num.append(x)


print(f"Even Numbers List : {even_num}")
print(f"Odd Numbers List : {odd_num}")

