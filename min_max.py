from collections.abc import Iterator
def fun_min_max(L=None):
    if isinstance(L, Iterator):
        x = 0;
        y = 0;
        for value in L:
            if x == None:
                x = value;
                y=  value;
            if value < x:
                x=value;
            if value > y:
                y=value;
        return (x,y)
    else:
        return (4,None);