# A simple Python program
# This is my first step into software engineering

def greet(name):
    return f"Hello, {name}! Welcome to software engineering."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)
