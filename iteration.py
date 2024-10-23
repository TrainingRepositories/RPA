# iterations 

#zip(): Creates an iterator of tuples
 #where each tuple contains the i-th element from each of the input iterables.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

#enumerate(): Adds a counter to an 
#iterable and returns it as an enumerate object.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

    
