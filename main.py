import random
import time


class my_float:
    def __init__(self, instr):
        if instr.startswith("-"):
            sign = True
            instr = instr[1:]
        elif instr.startswith("+"):
            sign = False
            instr = instr[1:]
        else:
            sign = False

        exp = 0
        if "E" in instr:
            exp = int(instr[instr.index("E")+1:])
            instr = instr[:instr.index("E")]
        
        if "." in instr:
            exp -= (len(instr) - 1) - instr.index(".")
            instr = instr.replace(".", "")

        base = int(instr)
        if base == 0:
            exp = 0

        assert base >= 0
        assert exp == int(exp)
        self.sign = sign
        self.base = base
        self.exp = exp

    def __add__(self, value):
        while self.exp != value.exp:
            if self.exp > value.exp:
                self.exp -= 1
                self.base *= 10
            elif self.exp < value.exp:
                value.exp -= 1
                value.base *= 10
        
        assert self.exp == value.exp
        self.base += value.base
        return self

    def __repr__(self):
        signchar = ""
        if self.sign:
            signchar = "-"
        output = ""
        if self.exp == 0:
            output = "{}{}".format(signchar, self.base)
        elif self.exp < 0:
            integer = self.base // 10**abs(self.exp)
            fract = str(self.base - integer * 10**abs(self.exp)).rjust(abs(self.exp), "0")
            output = "{}{}.{}".format(signchar, integer, fract)
        elif self.exp > 0:
            output = "{}{}".format(signchar, self.base * 10**self.exp)

        output = output.rstrip("0")
        if output.endswith("."):
            output += "0"
        return output

while True:
    x = random.randrange(100000)/(random.randrange(5000)+1)
    y = random.randrange(100000)/(random.randrange(5000)+1)
    true_value = x + y
    my_float_x = my_float(str(x))
    my_float_y = my_float(str(y))
    tested_value = my_float_x + my_float_y
    if str(true_value) != str(tested_value):
        if abs(float(true_value) - float(str(tested_value))) > 0.000001:
            print("X:\t{}".format(x))
            print("Y:\t{}".format(y))
            print("real:\t{}".format(true_value))
            print("got:\t{}".format(tested_value))
        
