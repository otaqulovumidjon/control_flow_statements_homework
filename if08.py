def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a==int(a) and a>=10 and a<=99:
        if a%2==1:
            return "two-digit odd number"
        else:
            return "two-digit even number"

    if a==int(a) and a>=100 and a<=999:
        if a%2==1:
            return "three-digit odd number"
        else:
            return "three-digit even number"

print(main(344))