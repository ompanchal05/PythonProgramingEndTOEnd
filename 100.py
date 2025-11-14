def greet():
    return "Hello"

def higher(func):
    print(func())

higher(greet)
