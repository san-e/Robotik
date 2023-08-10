
def ggT(a: int, b: int) -> int:
    R: int
    while (a % b) > 0:
        R = a % b
        a = b
        b = R

    return b

print(ggT(ggT(42, 120), 285)) # 3