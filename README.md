
# Task 2
At first you can check installed Ansible version by using this command `ansible --version`. If you don't have ansible installed, be sure to install it by using brew package for mac systems following this command `brew install ansible` or following this [link's guide](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html) for other operating systems. to this directory by using `cd "directory path"` command.
- 2-a: You can find the answer for this task here in the [inventory.yml](./Task2/inventory.yml).
- 2-b: At first you have to move to this directory by using `cd/"folder path"` command an then run these commands:
```shell
ansible-palybook -i ./inventory.yml -e action="verify_install" playbook.yml
```

```shell
ansible-playbook -i ./inventory.yml -e action="check-disk" playbook.yml
```




# Python Developer Questions
   
## 1. Basic Python Knowledge

Explain the difference between Python 2 and Python 3:
- Python 2 reached its end of life in 2020 and not getting updated anymore. While Python 3 is currently developed actively and has more features than Python 2.
- Python 3 is recommended for development becasue of its improved features and syntaxes. Also, transitioning from Python 2 to Python 3 may require some adjustments, which make Python 3 more efficient for long-term development.

Describe Python's data types, such as integers, strings, lists, dictionaries, and
sets.
- <u> int</u> : They store any numerical varibales. 
- <u> str</u> : They store sequence of characters between single ('') or double quotes ("").
- <u> list</u> : It stores ordered and mutable group of items in different types by using '[]'.
- <u> dict </u> : Unordered collections of key-value pairs. Each key is unique. it uses '{}' to define a dictionary. 
- <u> set </u> : An unordered collection of unique elements. it defines by '{}'.

Describe your understanding of variables, data assignment, and variable scope.
- Variables are labels used to store and manage data in a program.
- Data assignment is the process of assigning a value to a variable by '='.
- Variable scope knowledge is cruicial for modular and object-oriented programming since it defnies where the variable is accessible in our code:
  - Local: Limited to a specific block or function
  - Global: Accessible from anywhere in the program


## 2. Control Structures

Write a simple if statement to check a condition.

```python 
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")
```

Advice / write a code that uses a for loop to iterate over a list or range.

```python 
list = [1,2,3,4]

for i in list:
    print()
```

Tell us some example of using while loops.
- They can be powerful especially in scenrios that we are not sure about the exact number of iterations in advance. 
  
```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
```

## 3. Functions

Define a function that takes parameters and returns a value.

```python
def func (a, b):
    return a+b

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))

print(f"Sum of {num1} and {num2} is {func(num1,num2)}")
```

Describe about the usage of keyword arguments and default parameter values.
- <u>Keyword Arguments</u>: It allows you to pass values to a function by explicitly specifying the parameter names, so you can provide arguments out of order.

```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet(greeting="Hello", name="Sam") 
#it prints "Hello Sam!"
#==================#
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Hello", "Sam")
#it prints "Sam, Hello!"
```

- <u> Default Parameter Values</u>: It uses default value which is assigned to a parameter when a caller doesn't provide any value for that specific parameter.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Sam")  # it uses default greeting: "Hello, Sam!"
greet("Sam", "Hi")  # it overrides the default greeting: "Hi, Sam!"
```
Request an example of a function that uses the return statement.

```python
def func (a, b):
    return a+b

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))

print(f"Sum of {num1} and {num2} is {func(num1,num2)}")
```


## 4. Data Structures

Tell us about your knowledge of lists and their methods (e.g., append, pop, index)
- I have worked with these various data structures and havse strong knowledge to implement them for mainipulatin and defining algorithms by Python. 
  - append() adds an item to the end of a list.
  - pop() removes and returns a specific item if the index is provides; otherwise, it will use the last itme in the list.
  - index() retunrs the item at first point it finds the specific value. 

Advice about work with dictionaries, including adding, modifying, and accessing keys and values.
- Dictionaries in Python offer fast O(1) and efficient key-based data retrieval, flexible organization, and the ability to handle unique keys, making them valuable for various data storage and retrieval tasks.

```python
# add to dictionary
student["city"] = "New York" 

# modifying values in dictionary
student["age"] = 26 

# removing item from dictionary
del student["grade"] 

# iterating through dictionary
for key in student:
    print(key, student[key])

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
```


## 5. Exception Handling

Write a code that handles exceptions using try and except blocks.

```python
try:
    # check for possible errors
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("result:", result)

except ZeroDivisionError:
    # handle division by zero error
    print("Error: Division by zero is not allowed.")

except ValueError:
    # handle invalid input error
    print("Error: Invalid input. Please enter valid numbers.")

except Exception as e:
    # handle other errors
    print("An error occurred:", e)

else:
    # run this code without any errors deceted
    print("No exceptions were raised.")

finally:
    # run this code to execute regardless of exceptions
    print("Execution completed.")
```

- Uses "finally" mostly for cleanup scenarios like closing all the files regardless of the unexpected errors. 


## 6. File Handling

```python
Input_file = "input.txt"
Output_file = "output.txt"

# open the input file
input_file = open(Input_file, "r")

# read file
file_contents = input_file.read()

# close file
input_file.close()

# open the output file for writing
output_file = open(Output_file, "w")

# write contents 
output_file.write(file_contents)
output_file.close()

print("File contents copied successfully.")
```
- 'r': open file for reading
- 'w': open file for writing. If the file exists, it will remove all the provided contents; Otherwise it will create a new file.
- 'a': open file for writing. If it exists the new content will add to the end of the file; otherwise it will create a new file. 


## 7. Object-Oriented Programming (OOP)

- Class is a blueprint for creating objects, defining their attributes (data), and behaviors (methods). Anobjective is an instance of a class, representing a specific entity with its own data and behavior. Classes and objects enable code organization and reusability concepts. Based on my experience, I have strong knowledge and understanding regarding these concepts and optimizing my codes for further usages. 

```python
class Car:
    def __init__(self, make, model, year):
        # attributes
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self): #method
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is now running.")
            self.is_running = True
        else:
            print("The car is already running.")

    def stop(self): # method
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} has been stopped.")
            self.is_running = False
        else:
            print("The car is already stopped.")

# create an instance
my_car = Car("Toyota", "Camry", 2022)

# access attributes and invoke methods
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
my_car.start() 
my_car.stop()  
my_car.start() 
```


## 8. Modules and Libraries

Tell us about the importing and using external modules (e.g., math, random).
- We can use external modules by importing them to the code and gain access to more pre-built funcitons. Some of the most popular ones are pandas, numpy, sklear, math and etc.


Tell us about the purpose of commonly used libraries like os, sys, or
datetime.
- os: Interacting with the OS functions like files, directory operations.
- sys: Gain access to system-specific funcitons like interpreter setting.
- datetime: Allows manipulating of dates and times. 


## 9. Basic Algorithms and Problem Solving

Present a coding problem that involves iterating over data and performing a simple operation (e.g., finding the sum of all even numbers in a list).

```python
def sum_even_numbers(numbers):
    even_sum = 0
    
    for num in numbers:
        # check if the number is even
        if num % 2 == 0:
            even_sum += num 
    
    return even_sum

numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers)
print(result)  # output: 12

list = []
result = sum_even_numbers(list)
print(result) #output: 0
```

## 10. Coding Exercise
Write a Python code that could solve a problem by include tasks like reversing
a string, calculating Fibonacci numbers, or implementing a simple data
structure.

```python
# reverse a String
def reverse_string(input_str):
    return input_str[::-1]

# Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence[:n]

# stack data structures
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Reversed String:", reversed_str)

n = 10
fib_sequence = fibonacci(n)
print("Fibonacci Sequence (First", n, "numbers):", fib_sequence)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Is Empty:", stack.is_empty())
```


## 11. Version Control

I have great experience using Git commands in projects. I utilize commands such as `git init` and `git clone` to set up and clone repositories. For tracking changes, I use `git add` and `git commit` and monitor the status with `git status`. `git log`, `git log --graph` helps me review the commit history and commit history tree. Managing branches and collaborating is straightforward with commands like `git branch`, `git checkout`, `git merge`, `git pull`, and `git push`. I also employ `git remote` for remote repository management and `git stash` for temporary work storage. I am also familiar with other commands like `git fetch` and `git reset`. Based on all of these commands and skills, I am confidently able to work efficiently in a team project for software development. 