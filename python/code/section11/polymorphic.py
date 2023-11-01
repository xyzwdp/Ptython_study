# _*_ coding:UTF-8 _*_
"""
面向对下那个的多态特性以及抽象类（接口）的使用
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    animal.speak()

# 演示多态，使用2各子类对象调用函数值
dog=Dog()
cat=Cat()

make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:
    def cool_wind(self):
        #制冷
        pass
    def hot_wind(self):
        #制热
        pass
    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的制冷")

    def hot_wind(self):
        print("美的制热")

    def swing_l_r(self):
        print("美的左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力制冷")

    def hot_wind(self):
        print("格力制热")

    def swing_l_r(self):
        print("格力左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac=Midea_AC()
gree_ac=GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)
