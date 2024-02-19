#in các số từ 1 đến 100, mỗi dòng in 10 số
for i in range(1, 101):
    print("%3d" %i, end=' ')
    if i % 10 == 0:
        print()
    
# nhập 1 năm dương lịch, in ra tên năm âm lịch của nó. ví dụ: 2024 -> Giáp Thìn
def get_lunar_year_name(year):
    tenTruoc = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    tenSau = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

    truoc = (year-4) % 10
    sau = (year-4) % 12

    lunar_year_name = tenTruoc[truoc] + " " + tenSau[sau]
    return lunar_year_name

year = int(input("Enter a year: "))
lunar_year_name = get_lunar_year_name(year) 
print("Lunar year name:", lunar_year_name)

