from flask import Flask
import time

app = Flask(__name__)
@app.route('/') #see homepage
def hello_world():
    return 'Hello'

# if __name__=="__main__":
#     app.run()
# print(range.__name__)

def speed_cal_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_cal_decorator
def fast_function():
    for i in range(100000):
        i*i

@speed_cal_decorator
def slow_function():
    for i in range(1000000):
        i*i

fast_function()
slow_function()
