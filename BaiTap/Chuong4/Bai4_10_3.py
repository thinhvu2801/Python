def luy_thua_mod(a, x, p):
    ket_qua = 1
    while x > 0:
        if x % 2 == 1:
            ket_qua = (ket_qua * a) % p
        a = (a * a) % p
        x = x // 2
    return ket_qua

# Ví dụ kiểm tra
a = 3
x = 5
p = 7
ket_qua = luy_thua_mod(a, x, p)
print(f"Kết quả của {a}^{x} mod {p} là: {ket_qua}")