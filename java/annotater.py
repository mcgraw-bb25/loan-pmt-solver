#!/usr/bin/env python
import sys

tag = sys.argv[1]

for line in sys.stdin.readlines():
    sys.stdout.write('%s> %s' % (tag, line))
