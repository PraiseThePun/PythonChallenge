from PIL import Image
import requests
from io import BytesIO

class level7(object):
    def __init__(self, *args, **kwargs):
        self.__img = Image.open("resources/oxygen.png")


    def read_from_url(self):
        self.__img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))


    def my_solution(self):
        row = [self.__img.getpixel((x, self.__img.height / 2)) for x in range(self.__img.width)]
        row = row[::7]
        ords = [r for r, g, b, a in row if r == g == b]

        return "".join(map(chr, ords))


    def read_da_thingy(self):
        array = [105, 110, 116, 101, 103, 114, 105, 116, 121]

        return "".join(map(chr, array))