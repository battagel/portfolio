"""
This code runs on an input string where the class Hex then decides if it is a hex, denoted by the "0x" prefix, or a normal string. If the string is a hex then it calculates the value of the hex (max 3, doesnt have to be - change char_count).
If it is a normal string then it will ignore any letters and only print out the numbers in the string. Also the program removes white space infont and behind the input string.
"""

class Hex():

    def __init__(self, str):

        self.str = str
        if self.check_hex():
            result = self.calc_hex()
            print(result)
        else:
            result = self.calc_norm()
            print(result)

    def check_hex(self):
        if self.str[0] == "0" and self.str[1] == "x":
            return True
        else:
            return False

    def calc_hex(self):
        self.str = self.str[2:]
        total_hex = 0
        char_count = 0
        for digit in self.str:
            if char_count == 3:
                pass
            else:
                char_ascii = ord(digit) - 87
                total_hex += char_ascii * pow(16,((len(self.str)) - (self.str.index(digit) + 1)))
                char_count += 1
        return total_hex
    
    def calc_norm(self):
        clean_str = ""
        for digit in self.str:
            if digit.isdigit():
                digit.append(clean_str)
        if clean_str == "":
            return 0
        else:
            return int(clean_str)


if __name__ == "__main__":
    str = "0xabc"
    Hex = Hex(str)