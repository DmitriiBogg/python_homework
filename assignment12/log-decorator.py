import logging
from functools import wraps

# Logger
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Decorator
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {pos_args}")
        logger.info(f"keyword parameters: {kw_args}")
        logger.info(f"return: {result}\n")

        return result
    return wrapper

# Function 1
@logger_decorator
def say_hello():
    print("Hello, World!")

# Function 2
@logger_decorator
def always_true(*args):
    return True

# Function 3
@logger_decorator
def keyword_logger(**kwargs):
    return logger_decorator

# Main
if __name__ == "__main__":
    say_hello()
    always_true(1, 2, 3)
    keyword_logger(x=1, y=2)
