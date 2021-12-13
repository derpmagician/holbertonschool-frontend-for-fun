#!/usr/bin/python3
"""
Markdown to HTML
"""
import sys
if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    elif len(sys.argv) == 3:
        if not path.isfile(sys.argv[1]):
            sys.stderr.write("Missing {}\n".format(sys.argv[1]))
            exit(1)
    else:
        with open(sys.argv[1]) as md:
            with open(sys.argv[2], 'w') as html:
                exit(0)
