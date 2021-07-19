class level1():
    def __init__(self):
        self.__cypheredText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    def my_solution(self, text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."):
        result = ""

        for c in text:
            if c >= 'a' and c <= 'z':
                newChar = ord(c) + 2

                if newChar > ord('z'):
                    newChar -= 26

                result += chr(newChar)
            else:
                result += c

        return result

    def intended_solution(self):
        table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
        return self.__cypheredText.translate(table)

    def fancy_solution(self):
        return ''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in self.__cypheredText])