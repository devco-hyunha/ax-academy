# 상속 클래스
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.speed = 0

  def name(self):
    names = str(self.year) + ' ' + self.make + ' ' + self.model
    return names
  def getSpeed(self):
    print(str(self.speed) + '이다')

c1 = Car('tesla', 'A Class', 2018)

print(c1.name())
c1.getSpeed()


# class [자식클래스명 = 서브클래스명]([부모클래스 = 슈퍼클래스])
# super()를 통해 부모 클래스에 접근
class CampingCar(Car):
  def __init__(self, make, model, year, bed):
    self.bed = bed
    super().__init__(make, model, year)


# 메서드 오버라이딩 - 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것

camp1 = CampingCar('tesla', 'A Class', 2017, 2)
print(camp1.name())
camp1.getSpeed()

# 되새김 문제
# 1
class Calculator:
  def __init__(self):
    self.value = 0

  def add(self, val):
    self.value += val

class UpgradeCalculator(Calculator):
  def __init__(self):
    super().__init__()
  def minus(self, val):
    self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 2
class MaxLimitCalcurator(Calculator):
  MAX_LIMIT = 100
  def __init__(self):
    super().__init__()
  def add(self, val):
    super().add(val)
    if (self.value > self.MAX_LIMIT):
      self.value = 100

cal = MaxLimitCalcurator()
cal.add(50)
cal.add(60)

print(cal.value)

# 6
a = list(map(lambda i: i * 3,[1, 2, 3, 4]))
print(a)

## 
class Container:
  stock_num = 0
  def __init__(self, name):
    self.name = name
    Container.stock_num += 1

c = Container('Lee')
c2 = Container('Kim')

print(Container.stock_num)
print(c.name)
print(c2.name)
print(c.__dict__)
print(c2.__dict__)

