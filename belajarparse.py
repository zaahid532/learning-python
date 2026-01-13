import argparse
parser = argparse.ArgumentParser(
    description = 'just provide your name!' )
parser.add_argument(
    '-n',
    '--name',
    required = True,
    help='show hello words to my name'
)
parser.parse_args()
args = parser.parse_args()
print(f'hello, {args.name}! how are you?')