#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program convert the temperature


def convert_temperature():
    # convert temperature

    # input
    tc = int(input("Enter the temperature in degrees Celsius (°C): "))

    # process
    tf = (9/5) * tc + 32

    # output
    print("The temperature in degrees Fahrenheit is {0}°F".format(tf))


def main():
    # this function just calls other functions

    # call functions
    convert_temperature()


if __name__ == "__main__":
    main()