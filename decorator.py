def my_decorator(func):
    def wrappeer():
        print("Start login.....")
        func()
        print("End of the login......")
    return wrappeer
@my_decorator
def say_hello():
    print("Hello....!")
say_hello()


def repeat(n):
    def decorater(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorater
@repeat(3)
def say_hello():
    print("hello!")
say_hello() 

