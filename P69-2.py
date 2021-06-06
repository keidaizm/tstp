'''
def aa():
    """
    Returns input letters
    :param x: str.
    :return: int string letter of x.
    """
    x = input("type some letters")
    return x

result = aa()
print(result)
'''
'''
def print_string(string):

    print(string)

print_string("Testing: 1, 2, 3.")
'''

s = input("type some letters")

def print_string():
    global s
    print(s)

print_string()
