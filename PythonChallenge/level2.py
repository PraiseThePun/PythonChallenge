import string
import urllib.request
import re

class level2():
    def __init__(self, *args, **kwargs):
        self.__rawText = open('resources/level2text.txt').read()

    def my_solution(self):
        result = ""
        for c in self.__rawText:
            if c in string.ascii_letters:
                result += c

        return result

    def read_source_solution(self):
        html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
        comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
        data = comments[-1]

        return "".join(re.findall("[A-Za-z]", data))

    def fancy_solution(self):
        return "".join(filter(lambda x: x in string.ascii_letters, self.__rawText))