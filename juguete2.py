import time

def timer(func):
    # Decorator that measures the execution time of a function and displays the result

    def wrapper(*args, **kwargs):
        # Function that wraps the original function

        start = time.time()  # Save the start time
        func(*args, **kwargs)  # Execute the original function with the provided arguments
        elapsed = time.time() - start  # Calculate the elapsed time
        print(f"'{func.__name__}' took '{str(elapsed)}' seconds")  # Display the elapsed time result

    return wrapper  # Return the wrapper function

@timer
def test(n):
    # Test function that sleeps for one second

    time.sleep(1)

test(10)  # Call the test function with the argument 10

"""
Defines a decorator named 'timer' that measures the execution time of a function and displays the result.

The 'timer' decorator defines a 'wrapper' function that wraps the original function passed as an argument (func) 
using the decorator syntax.

Inside the 'wrapper' function, the start time is recorded using time.time() before calling the original function.

After executing the original function with the provided arguments,
the elapsed time is calculated by subtracting the start time from the current time.

Finally, the name of the original function and the elapsed time in seconds are printed.

The 'wrapper' function is returned as the result of the 'timer' decorator.

The 'test' function is defined and decorated with @timer, meaning that when 'test' is called, 
the execution time will be measured.

The 'test' function simply sleeps for one second using time.sleep().

Then, the 'test' function is called with the argument 10, triggering the 'timer' decorator 
and measuring the execution time of the function.

In summary, the code measures the execution time of the 'test' function using a decorator 
and displays the elapsed time in seconds after the function execution. 
In this case, the 'test' function sleeps for one second before finishing.
"""
