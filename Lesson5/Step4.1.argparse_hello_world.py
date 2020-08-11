import argparse

# #https://www.slideshare.net/tisto/argparse-python-command-line-parser

parser = argparse.ArgumentParser(
    description="A foo that bars"
)

parser.print_help()
