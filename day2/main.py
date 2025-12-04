def format():
    res = []
    for each in data:
        a,b = each.split("-")
        res.append( (int(a),int(b)) )
    return res

def repeated_ids_in_range(a,b):
    res=[]
    s=1
    while True:
        n=int(str(s)+str(s))
        if n>b: break
        if n>=a: res.append(n)
        s+=1
    return res

def sum_repeated_ids(ranges):   
    intervals = ranges
    max_b = max(b for _, b in intervals)
    found = set()
    s = 1
    while True:
        s_str = str(s)
        if int(s_str + s_str) > max_b:
            break
        k = 2
        while True:
            n = int(s_str * k)
            if n > max_b:
                break
            for a, b in intervals:
                if a <= n <= b:
                    found.add(n)
                    break
            k += 1
        s += 1
    return sum(found)

data = open("input.txt").read().strip().split(",")
data = format()

# part 1
total = 0
for each in data:
    lst = repeated_ids_in_range(each[0], each[1])
    total += sum(lst)
print("total =", total)

# part 2
p2 = sum_repeated_ids(data)
print("p2 total =", p2)