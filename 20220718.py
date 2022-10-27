set_ = {1, 2, 3}

def foo(Set: set):
    lst = sorted(list(Set))
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            yield set(lst[i: j+1])