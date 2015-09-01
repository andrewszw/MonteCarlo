__author__ = 'Zachary Andrews'

# import statements
from random import random

# constant number for the number of dots we wish to generate
N = 10000


def estimate_pi():

    # store a count for the number of times dots appear in circle
    count = 0

    # loop through and generate 10,000 random points between -1 and 1
    for i in range(N):

        # store x and y coordinates
        x = 2 * random() - 1
        y = 2 * random() - 1

        # check to see if dot is in circle
        if (x ** 2) + (y ** 2) < 1:
            count += 1

    # store the approximated value of pi
    pi = (count / N) * 4

    return pi


def main():

    # store the value of pi
    pi = estimate_pi()

    # print out the value of pi - hopefully close to 3.14
    print("The value of pi is approximately %f" % pi)

if __name__ == '__main__':
    main()

