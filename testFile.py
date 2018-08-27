import os

def testMethod():
    print("Test")
    name = os.path.dirname(os.getcwd())
    print(name)

testMethod()