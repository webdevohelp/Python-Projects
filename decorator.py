"""1"""
def inc(x):
    return x+1
def dec(x):
    return x-1
def operate(func,x):
    result = func(x)
    print(result)
operate(inc,2)


"""2"""
def hello(name = "Shubhang"):
    print("Hello Func has been executed")
    
    def greet():
        #func 1 inside hello function
        return '\t This is greet() func inside hello!'
    
    def welcome():
        #func 2 inside hello function
        return '\t This is welcome() inside hello!'

    if name == "Shubhang":
        return greet
    else:
        return welcome

newFunc = hello(1)
#depending on our input newFunc will either have value of greet() or welcome()
print(newFunc())


"""3"""
def cool():
    def super_cool():
        return "I am very cool!"
    return super_cool
some_func = cool()
print(some_func())

def helloo():
    return "Hi Jose!"
def other(some_other_func):
    print("Other code runs here!")
    print(some_other_func())
other(helloo)


"""4"""
def is_called():
    def hellloo():
        print("Hello")
    return hellloo
newHello = is_called()
newHello()


"""5"""
#main example of decorator
def new_decorator(original_func):
    def wrap_func():
        print("some extra code, before the original function!")
        original_func()
        print("Some extra code after the original function!")
    return wrap_func

@new_decorator
#@new_decorator send the following function to new_decorator function as argument(original_func)
def func_needs_decorator():
    print("I want to be decorated!")


#decorated_func = new_decorator(func_needs_decorator)
#@new_decorator on above line works similar to this line
func_needs_decorator()