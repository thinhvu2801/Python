def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

gcd, x, y = extended_euclidean_algorithm(a, b)
print("Ước chung lớn nhất của", a, "và", b, "là:", gcd)
print("Hệ số x và y thỏa mãn phương trình", a, "* x +", b, "* y =", gcd, "là:", x, "và", y)
