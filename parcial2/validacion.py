import math

def valInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

_valInt = valInt

def valInt(num, interval):
    if _valInt(num):
        if isinstance(interval, list):
            if len(interval) != 2:
                return False
            if type(interval[0]) != int or type(interval[1]) != int:
                return TypeError("Interval must be a tuple of integers")
            return num >= interval[0] and num <= interval[1]
        elif isinstance(interval, tuple):
            if len(interval) != 2:
                return False
            if type(interval[0]) != int or type(interval[1]) != int:
                return TypeError("Interval must be a tuple of integers")
            return num > interval[0] and num < interval[1]
        else:
            return TypeError("Interval must be a collection")
    else:
        return False


def valFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

_valFloat = valFloat

def valFloat(num, interval):
    if _valFloat(num):
        if isinstance(interval, list):
            if len(interval) != 2:
                return False
            if type(interval[0]) != int or type(interval[1]) != int:
                return TypeError("Interval must be a tuple of integers")
            return num >= interval[0] and num <= interval[1]
        elif isinstance(interval, tuple):
            if len(interval) != 2:
                return False
            if type(interval[0]) != int or type(interval[1]) != int:
                return TypeError("Interval must be a tuple of integers")
            return num > interval[0] and num < interval[1]
        else:
            return TypeError("Interval must be a collection")
    else:
        return False




def valComplex(num):
    try:
        complex(num)
        return True
    except ValueError:
        return False

_valComplex = valComplex

def valComplex(num, interval):
    if _valComplex(num):
        num = math.sqrt(num.real**2 + num.imag**2)
        if isinstance(interval, list):
            if len(interval) != 2:
                return False
            if type(interval[0]) != int or type(interval[1]) != int:
                return TypeError("Interval must be a tuple of integers")
            return num >= interval[0] and num <= interval[1]
        elif isinstance(interval, tuple):
            if len(interval) != 2:
                return False
            if type(interval[0]) != int or type(interval[1]) != int:
                return TypeError("Interval must be a tuple of integers")
            return num > interval[0] and num < interval[1]
        else:
            return False
    else:
        return False

def valList(lista):
    if isinstance(lista, list):
        return True
    else:
        return False

_valList = valList

def valList(lista, arg2, string):
    if _valList(lista):
        if string == 'len':
            if type(arg2) != int:
                return TypeError("Second argument must be an integer")
            return len(lista) == arg2
        if string == 'values':
            if type(arg2) != list:
                return TypeError("Second argument must be a list")

            for elem in lista:
                if elem not in arg2:
                    return False
            return True
        else:
            return ValueError("String must be 'len' or 'values'")
    else:
        return False

if __name__=='__main__':
    print(valInt(5, (1, 10)) == True)
    print(valFloat(5.0, (1, 10)) == True)
    print(type(valFloat(4,5)) == TypeError)
    print(valComplex(5+0j, (1, 10)) == True)
    print(type(valList([1, 2, 3], [1, 2, 3], 'len')) == TypeError)
    print(valList([1, 2, 3], 3, 'len') == True)
    print(valList([1, 2, 3], [1, 2, 3], 'values') == True)
    print(valList([1, 2, 3], [1, 3, 3], 'values') == False)