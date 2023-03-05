def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==1:
        print("Musbat toq son")

    if a>0 and a%2==0:
        print("Musbat juft son")

    if a<0 and a%2==1:
        print("Manfiy toq son")

    if a<0 and a%2==0:
        print("Manfiy juft son")
    
    if a==0:
        print("Son nol")
    return a

print(main(56))