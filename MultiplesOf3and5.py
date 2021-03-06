# Project Euler Problem 1

from mytc import Test

def multiplesOf3and5(number):
    mults = [x for x in range(number) if x % 3 == 0 or x % 5 == 0]
    return sum(mults)

if __name__ == "__main__":
    testcases = {
        1000: 233168,
        49: 543,
        19564: 89301183,
        8456: 16687353,
    }

    Test(testcases, multiplesOf3and5)