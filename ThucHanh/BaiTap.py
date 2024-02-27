# viết chương trình python nhập 1 số nguyên n, thoả 0<n<=1000.(lặp lại việc nhập cho đến khi n thoả mãn)
# a/ kiểm tra n có phải số nguyên tố
# b/ In ra các số nguyên tố <= n


while True:
    n = int(input("Nhập số nguyên n (0 < n <= 1000): "))
    if 0 < n <= 1000:
        break
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"{n} là số nguyên tố" if is_prime(n) else f"{n} không là số nguyên tố")

print("Các số nguyên tố <= n:")
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")


def Sum(*n):
    s=0;
    for i in n:
        s+=i
    return s

print(Sum(1,2,3,4,5,6,7,8,9,10)) # 55