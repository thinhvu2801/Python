import datetime
class Xe:
    nam_luu_hanh_max = 20

    def __init__(self, bien_so='000000000', hang_sx='', nam_sx=datetime.datetime.now().year):
        self.bien_so = bien_so
        self.hang_sx = hang_sx
        self.nam_sx = nam_sx

    def input(self):
        #check điều kiện biển số
        while True:
            self.bien_so = input("Nhập biển số xe (9 kí tự, bắt đầu bằng 2 kí tự số): ")
            if len(self.bien_so) == 9 and self.bien_so[:2].isdigit():
                break
            print("Biển số không hợp lệ!")
        while True:
            self.nam_sx = int(input("Nhập năm sản xuất (1980 < năm < 2024): "))
            if 1980 < self.nam_sx < datetime.datetime.now().year:
                break
            print("Năm sản xuất không hợp lệ!")
        self.hang_sx = input("Nhập hãng sản xuất: ")

    def output(self):
        print(f"Biển số: {self.bien_so}, Hãng sản xuất: {self.hang_sx}, Năm sản xuất: {self.nam_sx}")


    def tinh_so_nam_luu_hanh(self):
        return datetime.datetime.now().year - self.nam_sx


# Main 
danh_sach_xe = [Xe() for _ in range(int(input("Nhập số lượng xe (0<n<100): ")))]

for i, xe in enumerate(danh_sach_xe):
    print(f"Nhập xe thứ {i+1}")
    xe.input()
print("=====================================")

for xe in danh_sach_xe:
    print(f"Xe thứ {i+1}")
    xe.output()
print("=====================================")

nam_dai_nhat = max(danh_sach_xe, key=lambda x: x.tinh_so_nam_luu_hanh())
print("Xe có năm lưu hành dài nhất:")
nam_dai_nhat.output()
print(f"Số năm lưu hành của xe: {nam_dai_nhat.tinh_so_nam_luu_hanh()}")
print("=====================================")

danh_sach_xe = [xe for xe in danh_sach_xe if not xe.bien_so.startswith('79')]
print("Danh sách xe sau khi xóa xe có biển số bắt đầu bằng '79':")
for xe in danh_sach_xe:
    print(f"Xe thứ {i+1}")
    xe.output()