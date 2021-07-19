import re

class level3(object):
    def __init__(self, *args, **kwargs):
        self.__text = open('resources/level3text.txt').read()

    def my_solution(self):
        return "".join(re.findall("[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+", self.__text))