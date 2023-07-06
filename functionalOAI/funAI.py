import re
from pprint import pprint
from inspect import Signature, signature, Parameter
from typing import Callable, List, Dict, Union
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
                        "description": self.__getFuncDesc(function.__doc__),
                        "parameters": self.__generateParams(function)
                    })
    
    def __getFuncDesc(self, doc: Union[str, None]):
        if not doc: return ""
        funcDesc = re.search(r"^([\s\S]*)(?=\n\n)", doc.rstrip(), re.MULTILINE)
        return " ".join(funcDesc.group().split()) if funcDesc else ""

    def __getParamDesc(self, doc: Union[str, None]) -> Dict:
        if not doc:
            return {}

        paramDesc = re.findall(r"(?::param(?:eter)?\s+?)([a-zA-Z_][\w\s]*:.*)", doc.rstrip(), re.MULTILINE)

        if not paramDesc:
            return {}

        descDict = {}
        descDict.update([pd.split(":") for pd in paramDesc])

        return descDict

    def __generateParams(self, fn: Callable) -> Dict:
        sig = signature(fn)
        pDescs = self.__getParamDesc(fn.__doc__)
        
        return {
                "type": "object",
                "properties": {
                    k: {
                        "type": self.__castTypes(v.annotation.__name__),
                        "description": pDescs.get(k, "")
                    } for k, v in sig.parameters.items()
                },
                "required": self.__isRequired(sig)
            }

    def __isRequired(self, fsig: Signature) -> List:
        return [k 
                for k, v in fsig.parameters.items() 
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
    
