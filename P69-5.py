'''
def ff():
    try:
        g = input("type a number")
        g = float(g)
        return g
    except ValueError:
            print("Invalid Input.")

result = ff()
print(result)
'''

def ff(x):
    try:
        return float(x)
    except ValueError:
        print("Could not convert the string to a float.")


result = ff("40")
print(result)
