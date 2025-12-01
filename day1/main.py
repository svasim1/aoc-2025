def decode(data):
    pos = 50 
    zeros = 0
    
    stepMax = 100
    
    for each in data:
        dir = each[0]
        steps = int(each[1:])
        step = -1 if dir == "L" else 1
    
        pos = (pos + step * steps) % stepMax
        if pos == 0:
            zeros += 1

    return zeros

def decode_perclick(data):
    pos = 50
    zeros = 0
    stepMax = 100

    for each in data:
        dir = each[0]
        steps = int(each[1:])
        step = -1 if dir == "L" else 1

        if step == 1:
            k_first = (stepMax - pos) % stepMax
        else:
            k_first = pos % stepMax
        if k_first == 0:
            k_first = stepMax

        if steps >= k_first:
            zeros += 1 + (steps - k_first) // stepMax

        pos = (pos + step * steps) % stepMax

    return zeros


data = open("input.txt").read().strip().split("\n")

print(decode(data))
print(decode_perclick(data))