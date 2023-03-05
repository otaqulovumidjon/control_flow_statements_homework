def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a>0:
        a=1
    else:
        a=0
    if b>0:
        b=1
    else:
        b=0
    if c>0:
        c=1
    else:
        c=0
    if a+b+c>=2:
        print("Musbat sonlar ko'p")
    else:
        print("Manfiy sonlar ko'p")
    return a+b+c
print(main(1,-2,3))