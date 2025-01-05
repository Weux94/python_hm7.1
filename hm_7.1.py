name=input("Enter your name: ")
age=int(input("Enter your age: "))
def say_hi (name, age):
    return f"Hello, my name is {name}! I am {age} years old."

print(say_hi(name, age))