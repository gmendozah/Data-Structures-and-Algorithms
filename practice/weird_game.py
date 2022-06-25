
def callPopints(ops) -> int:
    record = []
    for c in ops:
        if c == "C":
            record = record[:-1]
        elif c == "D":
            previous = record[-1:]
            record.append(sum(previous) * 2)
        elif c == "+":
            last_t = record[-2:]
            record.append(sum(last_t))
        else:
            num = int(c)
            record.append(num)

    return sum(record)


t = '5 -2 4 C D 9 + +'
result =callPopints(t.strip().split())
print(result)

l = [1,2,3,4]
print(l.pop())
print(l)