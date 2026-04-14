# FunSimple8
def AddRightDigit(d: int, k: int):
    """K soniga o‘ng tarafdan R raqamini (1-9) qo‘shadi"""
    return k * 10 + d


# FunSimple9
def AddLeftDigit(d: int, k: int):
    """K soniga chap tarafdan R raqamini (1-9) qo‘shadi"""
    return d * (10 ** len(str(k))) + k


# FunSimple10
def Swap(a: int, b: int):
    """Ikki sonning qiymatlarini almashtiradi"""
    return b, a


# FunSimple11
def Minmax(x: int, y: int):
    """X va Y dan kichik va kattasini topib, o‘zgaruvchilarga joylaydi"""
    mn = min(x, y)
    mx = max(x, y)
    return mn, mx


# FunSimple12
def SortInc3(a: int, b: int, c: int):
    """A, B, C ni o‘sish tartibida joylashtiradi"""
    return tuple(sorted([a, b, c]))


# FunSimple13
def SortDec3(a: int, b: int, c: int):
    """A, B, C ni kamayish tartibida joylashtiradi"""
    return tuple(sorted([a, b, c], reverse=True))


# FunSimple14
def ShiftRight(a: int, b: int, c: int):
    """O‘ngga siklik siljitish: A→B, B→C, C→A"""
    return c, a, b


# FunSimple15
def ShiftLeft(a: int, b: int, c: int):
    """Chapga siklik siljitish: A→C, C→B, B→A"""
    return b, c, a







































































