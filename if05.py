def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
        
    x = 0
    if a == int(a) and a<0:
        x+=1
    if b == int(b) and b<0:
        x+=1
    if c == int(c) and c<0:
        x+=1
    return x
print(main(2, 3, 4))