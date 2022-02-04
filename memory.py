import json

class Stats():
    # Just initialation, loading json file and making it usable
    def __init__(self):
        self.__savefile = "stats.json"
        
        fh = open(self.__savefile, "r")
        x = fh.readline()
        fh.close()

        self.__memory = json.loads(x)

    # This is just a quick write over everything solution
    def setup(self):
        self.__memory = {
            "top": {"Leo": 0, "Max": 0, "Carl": 0},
            "reasons": {
                "Leo": ["hej", "test"]
            }
        }
        self.__save()

    # This is for adding points to a person
    def add(self, name):
        name = self.fix_str(name)
        print(f"name: {name}")
        if self.__is_person(name):
            self.__memory["top"][name] += 1
        else:
            # If the name was not recognized
            self.__create(name, 1)

        print(self.__memory["top"])
        self.__save()

    # This is for subtracting points from person
    def subtract(self, name):
        print(f"name is {name}")
        name = self.fix_str(name)
        if self.__is_person(name):
            self.__memory["top"][name] -= 1
        else:
            self.__create(name, -1)

        print(self.__memory["top"])
        self.__save()

    # To create a new person, this is a private function
    def __create(self, name, val):
        self.__memory["top"][name] = val

    # To check if person exists in json top-list, think I should swatch this out with the actual dictionary find funciton
    def __is_person(self, name):
        try:
            if self.__memory["top"][name] != None:
                return True
        except:
            return False

    # This will just return the persons in ranking order from high to low
    def get_list(self):
        top = []
        for person in self.__memory["top"]:
            if len(top) == 0:
                top.append(person)
            else:
                top.append(person)
                for i in range(len(top)-1, 0, -1):
                    if self.__memory["top"][person] > self.__memory["top"][top[i-1]]:
                        top[i] = top[i-1]
                        top[i-1] = person

        return top
    
    # When saving all the new cool info 
    def __save(self):
        fh = open(self.__savefile, "w")
        fh.write(json.dumps(self.__memory))
        fh.close()

    # This is a "To string" function for each person individualy
    def get_stat(self, name):
        name = self.fix_str(name)
        x = name + " " + str(self.__memory["top"][name]) + "\n"
        return x

    def fix_str(self, name):
        alias = {"Ckarl": "Carl", "Maxen": "Max", "Poggy": "Peggy", "Karl": "Carl", "Calle": "Carl", "Kalle": "Carl", "Epos": "Max"}
        name = name.replace(" ", "").capitalize()
        if name in alias:
            name = alias[name]
        return name
        
                    
# If starting this file as main
if __name__ == "__main__":
    test = Stats()
    #test.setup()
    test.subtract("leo")
    print(test.get_list())
    #print(test.get_stat("leo"))

        