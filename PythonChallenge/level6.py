import zipfile, re

class level6(object):
    def __init__(self, *args, **kwargs):
        self.__zip = zipfile.ZipFile("resources/channel.zip")

    def my_solution(self):
        num = '90052'
        comments = []

        while True:
            content = self.__zip.read(num + ".txt").decode("utf-8")
            comments.append(self.__zip.getinfo(num + ".txt").comment.decode("utf-8"))
            
            match = re.search("Next nothing is (\d+)", content)

            if match == None:
                break

            num = match.group(1)

        return "".join(comments)