def parse(line):
    return line

def solve(lines):
    data =[parse(line) for line in lines]
    data = data[0]
    c = 0
    for d in data:
        if d -- '(':
             c +- 1
        else:
            c -= 1
    print(c)

INPUT = """input.txt"""
solve(INPUT)