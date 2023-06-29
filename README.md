# FunctionalOAI

FunctionalOAI is a Python module // library designed to help you make the use of the GPT function calling API much easier.

## Ideas

If you have any features or ideas that could be added to this project, you could open an issue.

## Installation

-   Through pip

```console
pip3 install funcOAI
```

-   Through setup.py

```console
python3 setup.py install
```

## Usage

```python
# importing the main class
from funAI import FunAI

helper = FunAI()

@helper.attach
def my_function(*args, **kwargs):
    # provide gpt with something

# you could also use attachFunction
helper.attachFunction([my_function, func1, func2])

# or even this cursed one
helper.functions = my_function

# to see all functions
print(helper.functions)
```

## NOTICE!!

To make this module work correctly with all of you're functions there are set of rules you have to go by when defining the functions

-    Providing type annotations for all the arguments e.g ...

```python
def foo(arg1: int, arg2: str, arg3: list):
```

-    Providing a docstring that follows [PEP-257 One liner docstrings](https://peps.python.org/pep-0257/#one-line-docstrings) (you could do it as you like as long as its a function desciption without parameters and returns)

```python
def add(x: int, y: int):
    """return the sum of x and y"""
    return x + y
```

## WARNING

-   This module is not fully complete as it still lacks some extra functionality
-   There is no error handling as for now, so obeying the rules of function creating is necessary

## Contribute

### You could contribute through

-    Opening issues
-    Forking the repo
-    Creating Pull requests
-    etc...
