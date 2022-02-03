from audioop import add
from msilib.schema import Class
from os import stat
from pstats import Stats


import json

from matplotlib.pyplot import tick_params

class Stats():
    """
    def __init__(self):
        fh = open("stats.json", "r")
        x = fh.readline()
        self.ranking = json.loads(x)
    """

    def setup(self):
        self.memory = {
            "top": {"Leo": 0, "Max": 0, "Carl": 0},
            "reasons": {
                "Leo": []
            }
        }

        #self.memory["top"][0][1] = 3
        #y =json.dumps(x)
        #print(y)

    def add(self, name):
        if self.__is_person(name):
            self.memory["top"][name] += 1
        else:
            self.__create(name, 1)

        print(self.memory["top"])

    def subtract(self, name):
        name = name.capitalize()
        for person in self.memory["top"]:
            if name == person[0]:
                person[1] -= 1

        print(self.memory["top"])

    def __create(self, name, val):
        name = name.capitalize()
        self.memory["top"][name] = val

    def __is_person(self, name):
        name = name.capitalize()
        try:
            if self.memory["top"][name] != None:
                return True
        except:
            return False

        """name = name.capitalize()
        for person in self.memory["top"]:
            if name == person[0]:
                return True
        return False"""



if __name__ == "__main__":
    test = Stats()
    test.setup()
    test.add("New")

        