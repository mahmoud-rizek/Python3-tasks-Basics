class Game:

    choice = int(input('''        
        Weclome in our Game
        we have fife Games
        Enter the game's number for play
        1:Even Numbers & Odd Numbers
        2:Counter to tell you how many word at the sentence
        3:Enter number to tell you range  form zero to this number
        4:Enter two numbers and tell u if equal or not
        5:Enter two numbers to tell you the even and odd numbers betwen them
        Enter number's game:
        '''))
    
    if choice == 1:
        start_num = int(input("Enter start number: "))
        end_num = int(input("Enter end number: "))
        self.first(start_num , end_num)

    elif choice == 2 :
        sentance = input("Enter the sentance: ")
        self.second()

    elif choice == 3 :
        num = int(input("Enter the number: "))
        self.third()

    elif choice == 4 :
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        self.fourth(num1 , num2)

    elif choice == 5 :
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        self.fifth(number1 , number2)
    else:
        print("your choice is wrong")
    

    # def userChoice():
    #     while True:
    #         paly = input("Enter y for paly agin and X for exit: ")
    #         if paly == 'y':
    #             User = int(input("Number of the game: "))
    #             if User == 1:
    #                 self.frist()
    #             elif User == 2:
    #                 self.second()
    #             elif User == 3:
    #                 self.thierd()
    #             elif User == 4:
    #                 self.fourth()
    #             elif User == 5:
    #                 self.fifth()
    #             else:
    #                 print("Type i number 0 to exit or range 1->5")
    #                 continue
    #         elif paly == 'x':
    #             print("Tanks....")
    #             break
    
    def first(self, start_num, end_num):
        even_num = [] 
        odd_num = []

        for x in range(start_num, end_num+1):
            if x%2 == 0 :
                even_num.append(x)
            
            else:
                odd_num.append(x)


        print(f"Even Numbers List : {even_num}")
        print(f"Odd Numbers List : {odd_num}")


    def second(self , sentance):

        result = len(sentance.split(" ") )
        print(result)


    def third(self , num):
        for i in range(num+1):
            print(i)


    def fourth(self , num1 , num2):
        for i in range(num1+1):
            if i%num2 ==0 :
                print(i)


    def fifth(self , number1 , number2):
        for i in range(101):
            if i%number1==0 or i%number2==0:
                print(i)


g = Game()