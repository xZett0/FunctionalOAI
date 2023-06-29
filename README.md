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
