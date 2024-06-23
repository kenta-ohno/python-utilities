import os
from functools import wraps

###########   Path   ##############
join_path = os.path.join
split_ext = os.path.splitext


###########   Decorator   ##################

def exception_catch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An Error occurred in {func.__name__}: {e}")
            return None

    return wrapper

def main():
    pass

if __name__ == '__main__':
    main()
