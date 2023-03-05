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
    if a>0 and a==int(a) and a%2==1:
        return "Musbat toq son"

    if a>0 and a==int(a) and a%2==0:
        return "Musbat juft son"

    if a<0 and a==int(a) and a%2==1:
        return "Manfiy toq son"

    if a<0 and a==int(a) and a%2==0:
        return "Manfiy juft son"
    
    if a==0 and a==int(a):
        return "Son nol"

print(main(3))