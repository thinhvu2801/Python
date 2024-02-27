#phạm vi của biến trong python
#global: biến toàn cục
#local: biến cục bộ
#nonlocal: biến không phải toàn cục và cục bộ

def MyFunc():
    x = 300
    print(x)
    
def MyFunc2():
    global x2
    x2 = 100
    print(x2)
        
#gọi hàm MyFunc2()
MyFunc()