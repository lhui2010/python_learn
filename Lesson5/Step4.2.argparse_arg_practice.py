import argparse

# #https://www.slideshare.net/tisto/argparse-python-command-line-parser

parser = argparse.ArgumentParser(
    description="A worker that doing the work in a place"
)

# parser.print_help()

# add optional arguments
parser.add_argument('-n', '--name')

# add positional arguments
parser.add_argument('arg1')
parser.add_argument('arg2')

# reads from sys.argv and extract args
args = parser.parse_args()

# python Step4.1.argparse_hello_world.py

print(args.name)
print(args.arg1)
print(args.arg2)

print('Look! A {} is {}ing in {}'.format(args.name, args.arg1, args.arg2))

# /Users/liuhui/.conda/envs/python_learn/bin/python /Users/liuhui/PycharmProjects/python_learn/Lesson5/Step4.2.argparse_arg_practice.py -n gardener water greenhouse
# gardener
# water
# greenhouse
# Look! A gardener is watering in greenhouse
