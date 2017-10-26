'''
Write a program that take x, y, z parameter in type of floating numbers:
x is required
y is required
z is optional

Then calculate the area/volume of the rectangle/cube.

Then you have to use parser.add_mutually_exclusive_group() to print the result
in quiet mode using switch (--quiet or -q) or verbose mode (--verbose or -v)
The desired output is:


'''
import argparse

parser = argparse.ArgumentParser(description='Calculate surface of a rectangle or volume of a cube')
parser.add_argument('-x', '--length', type=float, metavar='', required=True, help='Length of the rectangle/cube')
parser.add_argument('-y', '--width', type=float, metavar='', required=True, help='Width of the rectangle/cube')
parser.add_argument('-z', '--height', type=float, metavar='', help='Height of the rectangle/cube')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def area(length, width):
    area = length * width
    resultString = "Area of the rectangle"
    return area, resultString

def volume(length, width, height):
    vol = length * width * height
    resultString = "Volume of the cube"
    return vol, resultString

if __name__ == '__main__':
    if not args.height:
        result = area(args.length, args.width)[0]
        resultString = area(args.length, args.width)[1]
        resultVerbose = resultString + ' with length {} and width {} is:'.format(args.length, args.width)
    else:
        result = volume(args.length, args.width, args.height)[0]
        resultString = volume(args.length, args.width, args.height)[1]
        resultVerbose = resultString + ' with length {}, width {}, and height {} is:'.format(args.length, args.width, args.height)

    if args.quiet:
        print (result)

    elif args.verbose:
        print(resultVerbose, result)
    else:
        print(resultString, result)
