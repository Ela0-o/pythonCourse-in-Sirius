# import regex as re
from sys import argv
import re

def gen_shab(pattern: str):
    len_mass = pattern.count('%')

    pattern = (pattern
    .replace('%d', '([\+\-]?[0-9]+)')
    .replace('%f', '([\+\-]?\d*\.*\d*[[eE]?[\+\-]?\d*]?)')
    .replace('%s', '(.*)')
    .replace(' ', '\s'))

    pattern = re.compile(pattern) #сборка шаблона

    return len_mass, pattern

def file_work(path, len_mass,  pattern):
    arr = []
    for i in range(len_mass):
        arr.append([])
    with open(path,'r') as f:
        for line in f:
            if len(line) == 0: continue
            ans = pattern.match(line) #применение шаблона к линии
            for i in range(len_mass):
                arr[i].append(ans.groups()[i])
            # mass = mass.append(arr)

    # print(mass)
    return arr


if __name__ == "__main__":
    path = argv[1]
    pattern = argv[2]
    len_mass, shablon = gen_shab(pattern)
    arr = file_work(path, len_mass,  shablon)

    for i in arr:
        print(i)




