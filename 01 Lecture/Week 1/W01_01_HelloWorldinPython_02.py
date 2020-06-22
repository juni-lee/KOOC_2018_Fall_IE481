"""
Object-oriented program
- HelloWorld is an object
- __init__, __del__, and performAverage are methods
"""


class HelloWorld():
    def __init__(self):
        print("Hello World! Just one more time")

    def __del__(self):
        print("Good bye!")

    def performAverage(self,val1,val2):
        average = (val1 + val2) / 2.0
        print("The average of the scores is : ", average)

def main():
    world = HelloWorld()
    score1,score2 = input("Enter two scores separated by a comma: ").split(',')
    score1 = int(score1)
    score2 = int(score2)
    world.performAverage(score1, score2)

main()
