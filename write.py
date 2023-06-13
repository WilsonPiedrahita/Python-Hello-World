#!/usr/bin/python3
import sys

def write(message):
    sys.stderr.write(message + '\n')
    sys.exit(1)

message = 'and that piece of art is useful - Dora Korpar, 2015-10-19'
write(message)