import sys
import argparse
import catmodule

parser =argparse.ArgumentParser(description='combine text file and output to screen or file')
parser.add_argument('files', metavar='F', type=str, nargs='+',
                    help='file to read')
args=parser.parse_args()
print(catmodule.cat(args.files))


