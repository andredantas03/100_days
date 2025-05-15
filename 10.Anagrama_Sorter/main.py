import turtle
import random

patterns = []
with open("patterns.txt","r") as file:
    for pattern in file.readlines():
        patterns.append(pattern.split("\n")[0])

print(patterns)





