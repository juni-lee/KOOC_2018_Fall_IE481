def main():
    print("Hello, world!")
    print("This program computes the average of two exam scores.")

    score1,score2 = input("Enter two scores separated by a comma: ").split(',')
    score1 = int(score1)
    score2 = int(score2)
    average = (score1 + score2) / 2.0;

    print("The average of the scores is : ", average)


main()
