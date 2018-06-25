# Json config file handling
import json
from collections import namedtuple

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        return str(self.__dict__)



class Handler:
    def __init__(self, filename):
        self.objs = {}
        self._loadObjects(filename)

    @staticmethod
    def _loadConfig(filename):
        """
        Load objects in to dictionary from json file
        """
        with open(filename) as f:
            return json.load(f)

    def _loadObjects(self, filename):
        """
        Take file -> make json dictionary -> convert to native format -> return objects list
        """
        olist = self._loadConfig(filename)

        #convert to object dict by ID
        for obj in olist:
            #self.objs[obj["id"]] = namedtuple("Object",obj.keys())(*obj.values())
            self.objs[obj["id"]] = Struct(**obj)

    def __getitem__(self, key):
        return self.objs[key]
