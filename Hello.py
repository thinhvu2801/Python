import math
def Hello():
    print("Hello World!")
    return Hello
Hello()

def so():
    print(10)
    return so
so()

# def nhap_so():
#     so = input("Nhập một số: ")
#     print("Đây là số: "+ so)
#     return nhap_so
# nhap_so()
def dem_so_tu(chuoi):
    so_tu = len(chuoi.split())
    return so_tu

chuoi = "Hello, đây là Vu Mink Thinh"
print(dem_so_tu(chuoi))
#in kí tự đầu và kí tự cuối
def in_ki_tu_dau_va_cuoi(chuoi):
    print(chuoi[0]) #in kí tự đầu tiên
    print(chuoi[-1]) #in kí tự cuối cùng
    print(chuoi[:10]) #in 10 kí tự đầu tiên
    print(chuoi[-10:]) #in 10 kí tự cuối cùng
    return in_ki_tu_dau_va_cuoi
in_ki_tu_dau_va_cuoi(chuoi)
def dinh_dang_cau():
    name = "Vu Minh Thinh"
    age = 21
    print("Tôi tên là %s, tôi %d tuổi" % (name, age)) 
    print("Tôi tên là {}, tôi {} tuổi".format(name, age)) 
    return dinh_dang_cau
dinh_dang_cau()
# định dạng chuỗi
def dinh_dang_chuoi(chuoi):
    print(chuoi.upper()) #in hoa
    print(chuoi.lower()) #in thường
    print(chuoi.capitalize()) #in hoa chữ cái đầu
    print(chuoi.title()) #in hoa chữ cái đầu mỗi từ
    return dinh_dang_chuoi
dinh_dang_chuoi("hello, đây là vu minh thinh")
#hàm tính toán import math và giải thích
def tinh_toan():
    print(math.pi)
    print(math.e)
    print(math.sin(30))
    print(math.cos(30))
    print(math.tan(30))
    print(math.log(10))
    print(math.sqrt(10))
    print(math.pow(2, 3))
    print(math.factorial(5))
    return tinh_toan
tinh_toan()
#thao tác với danh sách
def thao_tac_voi_danh_sach():
    ds = ["Vu Minh Thinh", 21, "Nha Trang"]
    print(ds)
    print(ds[0])
    print(ds[-1])
    print(ds[:2])
    print(ds[1:])
    ds.append("Đại học Nha Trang")
    print(ds)
    ds.insert(2, "Sinh viên")
    print(ds)
    ds.remove("Nha Trang")
    print(ds)
    ds.pop(2)
    print(ds)
    return thao_tac_voi_danh_sach
thao_tac_voi_danh_sach()
print("-------------------------")
#hàm thao tác với tuple
def thao_tac_voi_tuple():
    tp = ("Vu Minh Thinh", 21, "Nha Trang")
    print(tp)
    print(tp[0])
    print(tp[-1])
    print(tp[:2])
    print(tp[1:])
    return thao_tac_voi_tuple
thao_tac_voi_tuple()
#kiểu tập hợp set
def kieu_tap_hop_set():
    st = {"Vu Minh Thinh", 21, "Nha Trang"}
    print(st)
    st.add("Sinh viên")
    print(st)
    st.remove("Nha Trang")
    print(st)
    return kieu_tap_hop_set
kieu_tap_hop_set()
#trừ 2 tập hợp số nguyên
def tru_2_tap_hop_so_nguyen():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a - b)
    return tru_2_tap_hop_so_nguyen
tru_2_tap_hop_so_nguyen() 
#kiểu từ điển
def kieu_tu_dien():
    dic = {"name": "Vu Minh Thinh", "age": 21, "address": "Nha Trang"}
    print(dic)
    print(dic["name"])
    print(dic["age"])
    print(dic["address"])
    dic["school"] = "Đại học Nha Trang"
    print(dic)
    dic.pop("address")
    print(dic)
    return kieu_tu_dien
kieu_tu_dien()
#đếm xem mỗi từ xuất hiện bao nhiêu lần trong một câu
def dem_tu():
    chuoi = """Từ ấy trong tôi bừng nắng hạ
                Mặt trời chân lý chói qua tim
                Hồn tôi là một vườn hoa lá
                Rất đậm hương và rộn tiếng chim..."""
    ds = chuoi.split()
    dic = {}
    for tu in ds:
        if tu in dic:
            dic[tu] += 1
        else:
            dic[tu] = 1 
    for tu in dic:
        print(tu,":",dic[tu])
    return dem_tu
dem_tu()