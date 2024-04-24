# Tech 258 Python
- [Tech 258 Python](#tech-258-python)
  - [Python. What is it?](#python-what-is-it)
  - [Pythons popularity and DevOps](#pythons-popularity-and-devops)
  - [Venv](#venv)
  - [Preferred Installer Program](#preferred-installer-program)
  - [Scripting vs Programming](#scripting-vs-programming)
  - [Base and inbuilt libraries](#base-and-inbuilt-libraries)
  - [Examples of the most popular external libraries](#examples-of-the-most-popular-external-libraries)
- [Age\_checker](#age_checker)
- [Loops](#loops)

## Python. What is it?
Python is a computer programming language used in modern day to create a plethora
of different programmes. A key factor of python is that is it a general purpose language!<br>
Python was created in the Netherlands by programmer Guido Van Rossum in 1991. 
The name comes from Monty Python's Flying Circus which gives it the symbols its large snake.

## Pythons popularity and DevOps
What makes a coding language popular is its uses and how easy it is to pick up. Python has both many uses
and is very easy to learn. The GitHub blog says " you can create complex, multi-protocol applications while maintaining 
concise, readable syntax".<br>
When it comes to DevOps engineering, Python is particularly helpful because of its simple syntax and deep libraries, it 
becomes easier to write automation scripts. On top of simple straight forward scripts python can be used for complex 
applications with GUIs.

## Venv
Venv stands for virtual environment, it doesn't physically exist it is just software. Each virtual environment is lightweight
and has their own individual independent set of packages installed. This allows a programmer to have and run different projects
without them interfering with one another.

## Preferred Installer Program
Pip is a python package manager, after installing packages for a desired project it can be installed into your environment
using PIP. It installs manages and uninstalls packages into your projects. Pip is the most used Python package manager

## Scripting vs Programming
A script is a file that contains logically ordered commands. The defining feature of a script is that it produces an output
in the python interpreter whereas a programme doesn't have to. A programme could be function however a script would have to
print out that function to be labelled a script.

## Base and inbuilt libraries
Base libraries come with the python download, they are standard so no matter which computer or environment you go to, these
libraries will be on python. 

## Examples of the most popular external libraries
External libraries are libraries of code or functions that are available for download to apply to your project. 
For example Numpy (Numerical python) which performs mathematical operations on lists and Matplotlib which visualises data. 
** **
# Age_checker

```python
film_rating = input("What's the age rating of the film?")

# use an if statement to check for "universal" rating
if film_rating == "universal":
    print("all age groups can watch this film")

# check if film rating is "pg"
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")

# check if film rating is "12" or "12a"
elif film_rating == "12" or film_rating == "12a":
    print(
    "Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

# check if film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")

# check if film rating is "18"
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")

else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
```

# Loops
A loop is a sequence of codes/ instructions that are continually repeated until certain conditions are fulfilled, loops are used in a variety of ways. 
The main two types of loops are for loops and while loops.
- For loops<br>
Runs for each item in a range that is decided by the programmer.
```python
example = "test"
for char in example:
    print(char)
```
- While loops<br>
This loop runs until a certain condition is fulfilled.
```python
i = 0
while i <=5:
    print(i)
    i += 1
```

Depending on the situation you would use while over for, or for instead of while. A for loop could not print i until it reaches 5 
without extensive coding and boundaries.<br>
Loops can be infinite if not coded properly, this means your code will run forever.
** **