import re
from urllib.request import urlopen

class level4(object):
    def my_solution(self):
        uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
        num = "12345"

        pattern = re.compile("and the next nothing is (\d+)")

        while True:
            content = urlopen(uri % num).read().decode('utf-8')
            print(content)
            match = pattern.search(content)
            divide = re.search("Yes. Divide by two and keep going.", content)

            if divide:
                num = str(16044/2)
            elif match == None:
                break
            else:
                num = match.group(1)