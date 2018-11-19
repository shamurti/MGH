#!/usr/bin/env python3

import os
import sys
import fileinput

original_file = open("router_config.TXT", "r+")

read_original = original_file.read()

changed_file = read_original.replace("Serial0/0/0", "Changed0/0/0")

new_file = open("new_config.txt", "w")

new_file.write(changed_file)

new_file.close()


exit()


