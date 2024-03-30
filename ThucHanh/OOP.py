# class Personel:
    
#     def __init__(self, name="",age=0):
#         self.Name = name
#         self.Age = age
#         self.__Salary = None
#     def PrintInfo(self):
#         print(f"Name: {self.Name}, Age: {self.Age}, Salary: {self.__Salary}")
        
# if __name__ == "__main__":
#     p1 = Personel("Thinh", 20)
#     p1.PrintInfo()
#     print(p1.Name)
#     print(p1._Pesonel__Salary)
#     # print(p1.__Salary)

class Laptop:
    def __init__(self):
        pass
    def PrintInfo(self):
        print(self.Model)
        self.Battery.PrintInfo()
    # định nghĩa lớp Battery
    class Battery:
        def __init__(self, mnf, model, capacity):
            self.Manufacturer = mnf
            self.Model = model
            self.Capacity = capacity
        def PrintInfo(self):
            print(f"Manufacturer: {}, capacity: {} mAh".format(self.Manufacturer, self.Capacity))
            
if __name__ == "__main__":
    b1 = Laptop.Battery("Dell")
    b1.PrintInfo()