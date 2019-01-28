#task1
#print("What's your age?")
#age = input()
#
#age = input("What's your age?")
#print(age)

#task2
#print("What's your age")
#age = int(input())
#type(age)
#
#age = int(input("What's your age?")) #use that, saves memory
#age = input("What's your age?")
#age_int = int(age)

#task3
#option = input("Please input yes or no: ").lower()

#task4
#if len(option) < 4:
#    q1 = input("Would you like to move to the next question? ").lower()
#else:
#    print("Wrong answer. Bye!")

#task5 
#print("***choice***")
#print("1.Display my name")
#print("2.Display my age")
#print("3.Display my city")


#choice = 0
#while choice < 1 or choice > 3:
#    choice = int(input("What's your choice?"))
#
#if choice == 1:
#    print("Ms Smith")
#elif choice == 2:
#    print("26 years old")
#elif choice == 3:
#    print("London")

#print("1.Display my name")
#print("2.Display my age")
#print("3.Display my city")
#
#choice = 0
#while True:
#    try:
#        while choice < 1 or choice > 3:
#            choice = int(input("What's your choice? "))    
#        break
#
#    except ValueError:
#        print("Please type a number!")
#
#if choice == 1:
#    print("Ms Smith")
#elif choice == 2:
#    print("26 years old")
#elif choice == 3:
#    print("London")
    
    
#task7   
class Spam(object):
    def __init__(self, description, value):
        if not description or value <= 0:
            raise ValueError
        self.description = description
        self.value = value
        
#s = Spam("s", 5)
s = Spam("", -1)
print(s.value)


#class Spam(object):
#    def __init__(self, description, value):
#        assert description != ""
#        assert value > 0
#        self.description = description
#        self.value = value


#Assertions are statements that assert or state a fact confidently in your program. 
#For example, while writing a division function, you're confident the divisor 
#shouldn't be zero, you assert divisor is not equal to zero.
#
#Assertions are simply boolean expressions that checks if the conditions return 
#true or not. If it is true, the program does nothing and move to the next line of 
#code. However, if it's false, the program stops and throws an error.
#
#It is also a debugging tool as it brings the program on halt as soon as any error 
#is occurred and shows on which point of the program error has occurred.