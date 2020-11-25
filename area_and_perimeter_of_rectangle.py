#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program calculates the area and perimeter of a rectangle
# with user input


def main():
    # this functions area and perimeter

    # input
    Length = int(input("Enter the length of the rectangle (mm):"))
    width = int(input("Enter the width of the rectangle (mm): "))

    # process
    area = Length * width
    perimeter = 2*(Length + width)

    # ouput
    print("")
    print("Area is {}mm^2".format(area))
    print("perimeter is {}mm".format(perimeter))

    if __name__ == "__main__":
        main()
