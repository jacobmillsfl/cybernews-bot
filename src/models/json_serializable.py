import json
from abc import ABC, abstractmethod


class JSONSerializable(ABC):    
    def __str__(self):
        return json.dumps(
            self.__dict__,
            indent=2,
            default=vars)
