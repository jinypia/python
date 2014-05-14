import unittest
def comma_number(no):
    t = no.split(".")
    decimal = t[0]
    sosu = ""
    if len(t) > 1: sosu = t[1]
    if sosu:
        return comma(decimal) + "." + sosu
    else:
        return comma(decimal)

def comma(no):
    result = []
    numbers = list(str(no))
    numbers.reverse()
    for i, n in enumerate(numbers):
        if i%3 == 0 and i: result.insert(0, ",")
        result.insert(0, n)
    return "".join(result)

class CommaTest(unittest.TestCase):
    def test1(self):
        self.assertEqual("", comma_number(""))
        self.assertEqual("1", comma_number("1"))
        self.assertEqual("12", comma_number("12"))
        self.assertEqual("123", comma_number("123"))
        self.assertEqual("1,234", comma_number("1234"))
        self.assertEqual("1,234.02", comma_number("1234.02"))
        self.assertEqual("3,312,345.3234", comma_number("3312345.3234"))

if __name__ == "__main__":
    unittest.main()
