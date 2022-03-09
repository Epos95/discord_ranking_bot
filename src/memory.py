# imports from lib
import datetime
import json

# Other selfwritten files
import utils

class Stats():
    # Just initialation, loading json file and making it usable
    def __init__(self):
        self.__savefile = "../stats.json"
        
        fh = open(self.__savefile, "r")
        self.__memory = json.load(fh)
        fh.close()

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
        name = utils.fix_str(name)
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
        name = utils.fix_str(name)
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
        name = utils.fix_str(name)
        if name in self.__memory["names"]:
            name = self.__memory["names"][name]
        x = name + " " + str(self.__memory["top"][self.alias_id(name)]) + "\n"
        return x

    def get_pos(self, name):
        name = self.alias_id(utils.fix_str(name))
        top_list = self.get_list()
        for i in range(len(top_list)):
            if top_list[i] == name:
                return i+1
        return 0
    
    # Works, just needs to be implemented
    def history(self, sender, reciever, reason, vote):
        vote = utils.vote_meaning(vote)
        timeholder = datetime.datetime.now()
        time = timeholder.strftime("%d/%m-%Y %H:%M:%S")
        self.__memory["voting_history"].insert(0, {"sender": sender, "reciever": reciever, "reason": reason, "vote": vote, "timestamp": time})
        self.__save()

    def alias_id(self, name):
        name = name.capitalize()
        try:
            return str(self.__memory["alias"][name])
        except:
            # This should return discord nickname
            return "Jane Doe"

    def add_alias(self, person_id, new_alias):
        new_alias = utils.fix_str(new_alias)
        for key, val in self.__memory["alias"].items():
            if key == new_alias:
                if val != person_id:
                    return 0
                return 1
        self.__memory["alias"][new_alias] = person_id
        self.__save()
        print("new alias")
        return 1

    def change_name(self, person_id, new_name):
        if not self.add_alias(person_id, new_name):
            return 0

        for key, val in self.__memory["names"].items():
            if val == new_name:
                if key != person_id:
                    return 0
                return 1

        utils.fix_str(new_name)
        self.__memory["names"][person_id] = new_name
        self.__save()
        return 1

                    
# If starting this file as main
if __name__ == "__main__":
    test = Stats()
    #test.setup()
    #print(test.alias_id("hej"))
    #test.history("From", "To", "Reasoning", "-")