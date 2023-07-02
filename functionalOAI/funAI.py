from inspect import signature, Parameter
from typing import Callable, List, Dict
from functions import functionsList

class FunAI:
    def __init__(self) -> None:
        self.__functionsList: functionsList = functionsList()

    @property
    def functions(self) -> functionsList:
        """
        return a list of all the attached functions.
        
        :returns: __functionsList
        :rtype  : <Class functionsList> 
        """
        return self.__functionsList

    @functions.setter
    def functions(self, fn: List[Dict]) -> functionsList:
        """
        replace all the functions inside __functionsList with the functions that the user has provided 

        :param fn: functions to attach
        :type fn : typing.List[typing.Dict] 
        :returns : __functionsList
        :rtype   : <Class functionsList>
        """
        self.__functionsList.clear()
        for function in fn:
            self.__functionsList.append(function)
        return self.__functionsList

    @property
    def attach(self) -> Callable:
        """
        attach a decorated function body to functionsList.

        :returns: wrapper
        :rtype  : typing.Callable
        """
        def wrapper(func) -> Callable:
            self.attachFunctions([func])
            return func

        return wrapper

    @attach.setter
    def attach(self, fn: Callable) -> functionsList:
        """
        manually attach a single function body to functionsList.

        :param fn: function to attach
        :type fn : typing.Callable
        :returns : __functionsList
        :rtype   : <Class functionsList>
        """
        self.attachFunctions([fn])
        return self.__functionsList
    
    def attachFunctions(self, fn: List[Callable]) -> None:
        """
        Loop through a list of callables and append their bodies to functionsList,
        functionsList is accessable through the \"functions\" __getter__ method.

        :param fn: functions to attach
        :type fn : typing.List[typing.Callable]
        :returns : None
        :rtype   : None
        """
        for function in fn:
            self.__functionsList.append({
                        "name": function.__name__, 
                        "description": function.__doc__,
                        "parameters": {
                                "type": "object",
                                "properties": self.__generateParams(function.__annotations__),
                                "required": self.__isRequired(function) 
                            },
                    })


    def __generateParams(self, annotations: Dict) -> Dict:
        return {
                aKey: {
                    "type": self.__castTypes(annotations[aKey].__name__),
                    "description": ""
                } for aKey in annotations.keys()
            }

    def __isRequired(self, function: Callable) -> List:
        return [k 
                for k, v in signature(function).parameters.items()
                if v.default == Parameter.empty]

    def __castTypes(self, argType: str):
        return {
                "int":   "number",
                "float": "number",
                "str":   "string",
                "bool":  "boolean",
                "list":  "array",
                "tuple": "array",
                "dict":  "object"
            }.get(argType, "string")
    
    # TODO: parse __doc__ string to differentiate between function description and parameters description
    def __parseDescription(self): ...

