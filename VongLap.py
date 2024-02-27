#in ra số chẵn <= 100
i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1

# sử dụng while - continue
i=1
while i<=100:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1
#lệnh lặp với kiểu từ điển
d={'name':'Thinh','age':20}
for key in d:
    print(key,d[key])
#lặp 2 biến chạy
for i,j in d.items():
    print(i,j)
#for comprehensive    #tạo danh sách các số nguyên liên tiếp từ 1 tới 100
a=[i for i in range(1,101)]
print(a)
myOddNum = [i for i in range(1,101) if i%2!=0]
print(myOddNum)
