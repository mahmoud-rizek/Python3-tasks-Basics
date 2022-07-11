while True:
    
    choice = int(input('''
Select the game:
1. one
2. two
3. three
4. four
5. fife
'''))
    if choice in (1,2,3,4,5):
        if choice == 1 :
            even_num = [] 
            odd_num = []

            for x in range(50):
                if x%2==0 :
                    even_num.append(x)
                
                else:
                    odd_num.append(x)


            print(f"evenNumbers : {even_num}")
            print(f"oddNumbers : {odd_num}")
    else:
        print("Error, Please choice the opration from 1 to 5")
