# FunctionalOAI

FunctionalOAI is a Python module // library designed to help you make the use of the GPT function calling API much easier.

## Ideas

If you have any features or ideas that could be added to this project, you could open an issue.

## Installation

-   Through pip

```shell 
pip3 install funcOAI
```

-   Through setup.py

```shell 
python3 setup.py install
```

## Usage

```python
# importing the main class
from functionalOAI import FunAI

client = FunAI()

@client.attach
def my_function(*args, **kwargs):
    # provide gpt with something

# you could also use attachFunctions
client.attachFunctions([my_function, func1, func2])

# or even this cursed one
client.functions = my_function

# to see all functions
print(client.functions)
```

-    After creating you're functions then you could use openai python module to create a chat with chatgpt and you could provide it with client.functions e.g ...

```python
from functionalOAI import FunAI

client = FunAI()

@client.attach
def get_current_weather(location: str, unit: str = "fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

def run_conversation():
    messages = [{"role": "user", "content": "What's the weather like in Boston?"}]

    ## function info
    functions = client.functions

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        available_functions = {
            "get_current_weather": get_current_weather,
        }
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )

        messages.append(response_message)
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )

        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )
        return second_response


print(run_conversation())
```

## New Usage Feature

-    You could now access all the elements inside the functions list and do all sort of list methods on them (most of them at least you could look in functions.py to see all the overridden list methods)
```python
from functionalOAI import FunAI

client = FunAI()

@client.attach
def suM(a: int, b: int):
    """return the sum of a and b"""
    return a + b

def muL(a: int, b: int):
    """return the multiplication of a and b"""
    return a * b

print(client.functions)
client.functions.append({"name": "muL", "description": "return the multiplication of a and b", ...})
print(client.functions)
```
### Its made to make removing / adding / deleting functions easy

```python
# see if a function inside the list by the name or the body
print("muL" in client.functions) # True

# remove function by name (you could also add the whole body of the function)
client.functions.remove("muL")

print("muL" in client.functions) # False

# remove a function using the del keyword
del client.functions["muL"] # error since muL was already removed


print(client.functions)

# get the body of a specefic function by its name or its index in the list
print(client.functions["suM"])

# multiple ways to add a function
client.functions.append({"name": "test", "description": "..."})
client.functions.insert("at the index of a specefic function name or by the index", {"name": "test2", "description": "...."})
print(client.functions)

# replace a specefic function
client.functions["test2"] = {"name": "test3", "description": "hackerman++"}

# get the index of a specific function by its name or body
client.functions.index("test3") # the index function calls another function called name_to_key so you could use that directly there is none special about index 

# or get the name by the index
client.functions.key_to_name(0) # suM

# clear the whole list
client.functions.clear()
```

### This is an edited example of the [official OpenAI API example](https://platform.openai.com/docs/guides/gpt/function-calling)

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
-   There is no error handling as for now, so obeying the rules of function defining is necessary

## TODO

-    create a special type for the functions list, to make it more flexable and accessable, and much more efficient (handeling duplicates etc ...)
-    create a multi-line docstring parser that gets a description for the function and a description for each of the arguments
-    handle all possible errors in creating the body of the function, and create backup plans in case something was missing in the function definition

## Contribute

### You could contribute through

-    Opening issues
-    Forking the repo
-    Creating Pull requests
-    etc...
