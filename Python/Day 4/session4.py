# 객체
# class 설계도
# object 설계도를 바탕으로 실제 만들어진 제품

# 클래스
# self, 인스턴스 메소드, 인스턴스 변수
# 클래스 메소드, 클래스 변수

# 객체(Object) : 클래스의 인스턴스를 포함한 모든 파이썬 데이터

# 객체와 인스턴스의 차이
# 클래스로 만든 객체를 인스턴스라고 함
# 인스턴스라는 말은 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용
# a 는 인스턴스 보다 객체라는 말이 더 어울림
# b 는 a의 객체 보다 b는 a의 인스턴스라는 말이 더 어울림
# 인스턴스 : 특정 클래스에 의해 생성된 객체를 지칭

class Func:
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email
    
  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

  def set_data(self, a, b):
    self.a = a
    self.b = b

  def add(self):
    return self.a + self.b
  
  def sub(self):
    return self.a - self.b
  
  def mul(self):
    return self.a * self.b
  
  def div(self):
    return self.a / self.b


p1 = Func("John", 20, "john@example.com")
p1.set_data(1, 2)
print(p1.add())
print(p1.sub())
print(p1.mul())
print(p1.div())
print(p1)


class Profile:
  name = 'gildong' # 클래스 변수
  def __init__(self, age, name = name):
    self.name = name
    self.age = age

user1 = Profile(20, 'john')
print(user1.name)
print(user1.age)

user2 = Profile(30, 'jane')
print(user2.name)
print(user2.age)

print(Profile.name)

print("{0} {1} {2} {3} ".format(user1.name, user1.age, user2.name, user2.age))


class Test:
  def func():# 클래스 메소드
    print("Test func")

  def func2(self):# 인스턴스 메소드
    print(id(self))
    print("Test func2")

Test.func()
t = Test()

# 클래스 메소드로 호출시, self 인자를 넘겨줘야 함
Test.func2(t)
# t.func() #인스턴스 메소드로 호출시, 자동으로 self 인자가 전달됨
t.func2()

Test.func2(Test)