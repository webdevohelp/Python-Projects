"""example 1"""
try:
    #will try to run this code and if there is error then except is executed
    result = 10 + 10
except:
    print("Error in data-type")
    #executed of there is error
else:
    #executed if there is no error
    print(f"The result is: {result}")


"""example 2"""
try:
    f = open('testfile','w')
    f.write("Write a test line")
except OSError:
    print("Hey you have an OS Error")
except:
    print("There was other type of error!!!")
finally:
    #finally always gets executed
    print("I always run!")

"""3"""
def ask_for_int():
    while True:
        try:
            num = int(input("Please input a number: "))
        except:
            print("\nOnly the input of a number is allowed... \nTry again!")
            continue
        else:
            print("\nYes,\nThank you")
            break
        finally:
            print("\n'try/except/finally' will always run at the end!")
ask_for_int()

"""4"""
for i in ['a',2,3]:
    try:
        print(i**2)
    except:
        print("This was not a number")
        continue

"""5"""
x = 1
y = 2
try:
    z = x/y
except:
    print("Either x or y are not integer or y is zero(0)!")
finally:
    print("The addition is done!")

"""6"""
def ask():
    while True:
        try:
            x = int(input("\nPlease enter a number\n"))
        except:
            print("Please input a number, not a string!")
        else:
            print("The number squared is: ")
            print(x**2)
            break
ask()