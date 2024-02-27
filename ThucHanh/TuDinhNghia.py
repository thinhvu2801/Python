#tạo module tụ định nghĩa và sử dụng
# B1: Tạo 1 thư mục đặt tên tuỳ ý, chẳng hạn "my_lib"
##Trong thư mục phải chứa file __init__.py (nội dung có thể để trống), File này không có nội dung gì cả, chỉ để thông báo rằng thư mục này là một package
# B2: Trong thư mục "my_lib" tạo file "functions.py" chứa các thành phần tự cài đặt
## B2: Sử dụng module tự định nghĩa
### Tạo file mã nguồn python mới
### Thêm dòng khai báo import my_lib.functions
from my_lib.functions import *

HiName("Thịnh")