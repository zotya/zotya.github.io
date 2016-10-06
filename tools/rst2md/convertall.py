#!/usr/bin/env python
import rst2md

f = open('packages', 'r')

for package in f:
    rst2md.convert(package)
    print package