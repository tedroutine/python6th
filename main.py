# 예외가 하나인 경우
def devide(x, y):
    try:
        result = x / y
        print(f"x / y = {result}")
    except:
        print("Error!")
    finally:
        print("This is Math!")

devide(10, 2)

# 예외가 하나 이상인 경우
try:
    number = 5 + int("not a number")
except ValueError:
    print("error - invalid number")
except TypeError:
    print("error - invalid type")


# custom exception

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(f"Error: {e.message}")


