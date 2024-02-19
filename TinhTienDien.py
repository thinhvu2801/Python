def tinh_tien_dien(so_dien):
    if so_dien <= 50:
        tien_dien = so_dien * 1678
    elif so_dien <= 100:
        tien_dien = 50 * 1678 + (so_dien - 50) * 1734
    elif so_dien <= 200:
        tien_dien = 50 * 1678 + 50 * 1734 + (so_dien - 100) * 2014
    elif so_dien <= 300:
        tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (so_dien - 200) * 2536
    else:
        tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (so_dien - 300) * 2834
    
    return tien_dien

so_dien = float(input("Nhập số điện tiêu thụ (kWh): "))
tien_dien = tinh_tien_dien(so_dien)
print("Số tiền điện cần thanh toán là:", tien_dien, "VNĐ")
