def decorator_function(function):
    def wrapper(*arg):
        print(f"Calling {function.__name__}")
        result = function(*arg)
        print(f"Result: {result}")
        return result
    return wrapper


@decorator_function
def a_function(*arg):
    return sum(arg)

a_function(1,2,3)