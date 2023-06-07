def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

# display_info(name="tes", age=25)


def disp(sh):
    print(type(sh))
    print("Disp Function" + sh())

def show():
    return " Show Function"

disp(show)