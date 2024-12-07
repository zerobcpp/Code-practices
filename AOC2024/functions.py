import time
from functools import wraps

def timer(func):
    import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)   # Execute the function
        end_time = time.perf_counter()  # End the timer
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
        return result
    return wrapper


def time_recur():
    """Decorator to measure the cumulative runtime of a recursive function."""
    cumulative_time = {"total": 0}  # Dictionary to store total time

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()  # Start timer for this call
            result = func(*args, **kwargs)   # Execute the function
            end_time = time.perf_counter()   # End timer for this call
            elapsed_time = end_time - start_time
            
            # Accumulate the runtime
            cumulative_time["total"] += elapsed_time
            #print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
            return result
        
        # Add an attribute to access the total runtime
        wrapper.get_cumulative_time = lambda: cumulative_time["total"]
        return wrapper
    return decorator