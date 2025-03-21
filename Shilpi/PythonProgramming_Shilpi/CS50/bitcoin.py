

def checknumber(num1):
    try:
        f=float(num1)
        return True
    except ValueError:
        return False

a="2.7"
b="2"
c="cat"
print(checknumber(b))