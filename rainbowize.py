# rainbowizer script

# idea: read through the file line by line and check for the delimiters.
# when found, execute the `rainbowize` function to change the color of each character.

import sys, random
from functools import reduce

if len(sys.argv) < 2:
    print("Please enter a filename.")
    sys.exit(1)

rand = False
if len(sys.argv) == 3:
    if sys.argv[2].lower() in ['random', 'true', 'randomize']:
        rand = True

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()

# get starts and ends in order
starts, ends = [], []
for i,line in enumerate(lines):
    if line == '-=- rainbow -=-\n':
        starts.append(i)
    elif line == '-=- wobniar -=-\n':
        ends.append(i)

# check that starts and ends are valid
if len(starts) != len(ends):
    if len(starts) > len(ends):
        print(f"""Error: the number of beginnings you have for rainbow
    text exceeds the number of endings. Please make sure you line
    up your `-=- rainbow -=-` and `-=- wobniar -=-` lines correctly.""")
    else: 
        print(f"""Error: the number of endings you have for rainbow
    text exceeds the number of beginnings. Please make sure you line
    up your `-=- rainbow -=-` and `-=- wobniar -=-` lines correctly.""")
    
    sys.exit(1)

for i in range(len(starts)):
    if ends[i] <= starts[i]:
        print(f"Error: rainbowize ending before a beginning at line {ends[i]}.")
        sys.exit(1)

# rainbowize

COLORS = ['purple',
          'red',
          'orange',
          'yellow',
          'lime', 
          'green',
          'teal',
          'cyan',
          'blue',
          'violet']

def next_color(pointer, rand):
    if rand:
        return random.choice(COLORS)
    else:
        return COLORS[(pointer + 1) % len(COLORS)]

def rainbowize(region, rand):

    ## get characters 

    begin = '\\textcolor{'
    middle = '}{'
    end = '}'

    color_pointer = 0
    color = random.choice(COLORS) if rand else COLORS[color_pointer]

    altered_region = ''
    for char in region:
        if char.isalpha():
            colored_char = begin + color + middle + char + end
            altered_region += colored_char
            color_pointer += 1
            color = next_color(color_pointer, rand)
        else:
            altered_region += char
    return altered_region


# iteratively rainbowize across all regions

altered_regions = []

for i,e in enumerate(zip(starts, ends)):
    region = ''.join(lines[e[0]+1 : e[1]])
    altered_region = rainbowize(region, rand)
    altered_regions.append((altered_region, e))

# print(altered_regions[0])

unaltered_regions = []
for i,e in enumerate(zip(starts, ends)):
    if i == 0:
        unaltered_regions.append(list(range(0, e[0])))
    else:
        unaltered_regions.append(list(range(ends[i-1], e[0])))
unaltered_regions.append(list(range(e[1], len(lines) - 1)))
# concatenate all lists of indices
unaltered_regions = reduce(lambda x,y:x+y, unaltered_regions)

filename_no_ext = filename[:filename.rfind('.')]
ext = filename[filename.rfind('.'):]
with open(filename_no_ext + '_rainbowized' + ext, 'w') as g:
    i = 0
    k = 0
    while i < len(lines):
        if i in unaltered_regions or k > len(altered_regions) - 1:
            g.write(lines[i])
            i += 1
        else:
            # find line in altered_regions
            for j in altered_regions[k][0].split('\n'):
                g.write(j + '\n')
            i = altered_regions[k][1][1]+1
            k += 1