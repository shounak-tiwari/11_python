pairs = [('x','y'),('y','x'),('a','b'),('b','a'),('y','z')]



uniques_paris = {tuple(sorted(pair)) for pair in pairs }

print(uniques_paris)
