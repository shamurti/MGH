#!/usr/bin/env python3

original_file = open("router_config.TXT", "r+")

read_original = original_file.read()

original_file.close()

changed_file = read_original.replace("Serial0/0/0", "Changed0/0/0")

new_file = open("new_config.txt", "w")

new_file.write(changed_file)

new_file.close()

exit()


