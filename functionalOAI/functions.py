from typing import Dict, Union

class functionsList(list):
    def __init__(self):
        self.__types = (dict, Dict)
        self.__map   = dict() 

    def __getitem__(self, val: Union[str, int]) -> Dict:
        if isinstance(val, str):
            ntk = self.name_to_key(val)
            return super().__getitem__(ntk)

        return super().__getitem__(val)

    def __contains__(self, val: Union[dict, str]) -> bool:
        if isinstance(val, str):
            try:
                ntk = self.name_to_key(val)
            except KeyError:
                return False
            return super().__contains__(super().__getitem__(ntk))

        return super().__contains__(val)
    
    def remove(self, val: Union[dict, str]) -> None:
        if isinstance(val, str):
            super().remove(self.__getitem__(val)) 
            del self.__map[val]
        else: 
            super().remove(val)
            del self.__map[val.get("name")]

    def __delitem__(self, val: Union[str, int]) -> None:
        if isinstance(val, str):
            ntk = self.name_to_key(val)
            del self.__map[val]
            super().__delitem__(ntk)
        else:
            del self.__map[self.key_to_name(val)]
            super().__delitem__(val)

    def __setitem__(self, index: Union[str, int], val) -> None:
        self.__validateType(val)

        if isinstance(index, str):
            self.__map.update({val.get("name"): val})
            ntk = self.name_to_key(index)
            super().__setitem__(ntk, val)
        else:
            del self.__map[self.key_to_name(index)]
            super().__setitem__(index, val)
            self.__map.update({self.key_to_name(index): val})

    def insert(self, index: Union[int, str], val) -> None:
        self.__validateType(val)
        if isinstance(index, str):
            self.__map.update({index: val})
            ntk = self.name_to_key(index)
            super().insert(ntk, val)
        else:
            super().insert(index, val)
            self.__map.update({val.get("name"): val})

    def append(self, val) -> None:
        self.__validateType(val)
        self.__map.update({val.get("name"): val})

        super().append(val)
    
    def index(self, name: Union[str, dict]) -> int:
        return self.name_to_key(name)

    def clear(self) -> None:
       self.__map.clear()
       super().clear()

    def __validateType(self, value) -> None:
        if not isinstance(value, self.__types):
            raise TypeError("Input value must be of type dict")
    
    def name_to_key(self, val: Union[str, dict]) -> int:
        if isinstance(val, str):
            val = self.__map.get(val, None)
            if not val:
                raise KeyError("item is not found in __map")

        return super().index(val)

    def key_to_name(self, key: int) -> str:
        return super().__getitem__(key).get("name")
