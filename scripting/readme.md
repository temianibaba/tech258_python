# Scripting
- [Scripting](#scripting)
  - [Quick basics on scripting](#quick-basics-on-scripting)
    - [Interpreting vs Compling](#interpreting-vs-compling)
  - [Standard packages in python](#standard-packages-in-python)
  - [Python scripts in DevOps](#python-scripts-in-devops)

## Quick basics on scripting
![Scripting-Language-vs-Programming-Language-300x300.png](images%2FScripting-Language-vs-Programming-Language-300x300.png)
<br>Scripting is a way of providing instructions to a computer, so you can tell it what to do. Scripting is meant to aid 
programming, whereas coding for programs is to create complex software. It is mainly used to automate tasks. They provide 
control over one or more applications. 
### Interpreting vs Compling
**Interpreting** refers to code being translated and run line by line whereas **Compiling** refers to translating the entire code into
machine code and then being run.

## Standard packages in python
Here are some listed packages that are default with python. Overtime they were used so much it was considered installing 
python with these packages. It is important to note that all of these packages have easily accessible information about them online.

1. Random
```python
import random
print(random.random())
print(random.randrange(1, 10))
```
This library allows you to create random numbers, after importing the library, the first print statement prints a number 
in between 0-1, and the second print statement prints a number from 0-10 not including 10

2.Math
```python
import math

num_float = 23.66
print(math.ceil(num_float)) #roundup
print(math.floor(num_float)) #round down
print(math.pi)
```
Math allows more complex operations and methods to be used in your code.

3. OS
```python
import os

# returning current working directory
working_dir = os.getcwd()
print(f"Current working directory is:{working_dir}")

# get user
username = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"Username is: {username}")

# cpu cores
cpu_cores = os.cpu_count()
print(f"Amount of CPUs: {cpu_cores}")

# making/remove directory
os.mkdir("test_dir")
os.rmdir("test_dir")
```
This library uses syntax similar to linux, its main use is to execute commands relating to the users operating system.
Such as: making and removing directories, returning the current directory, returning the number of CPU cores and giving information 
about the users OS.

4. Datetime <br>
The final example in this document about scripting is datetime, this gives more methods linking to referencing the date 
and/or time.
```python
import datetime

print(f"Today's date is: {datetime.datetime.today()}")
```
## Python scripts in DevOps
1. Infrastructure as Code
2. Continuous Integration
3. Deployment
4. Monitoring
5. Alerting
6. Log Analysis
7. Configuration Management
8. Container Orchestration
9. Security
10. Cloud Automation

Here's an example of a deployment script:
```python
"deploy.reloaded":{
    "packages": [
        {
            "button": True,
            "name": "bb-core",
            "description": "bb-core for bb-400",
            "files": [
                "**/*"
            ]
            "deploy0nChange": True,
            "exclude": [
                "**/__pycache__/**",
                "examples/**",
            ]
        }
    ]
    "targets": [
        {
            "type": "sftp",
            "name": "BB-400 PP",
            "description": "BB-CORE Folder",
            "dir": "/usr/share/brainboxes/bb-core",
            "host": "192.168.0.60",
            "port": 22,
            "user": "bb",
            "password": "00e8",
            "modes": {
                "/usr/share/brainboxes/bb-core/bb-core": 755,
                "/usr/share/brainboxes/bb-core/bb-core/*": 755,
            }
        }
    ]
}
```