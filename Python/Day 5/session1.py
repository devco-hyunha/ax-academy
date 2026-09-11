class Fruit:
  price = 20000
  def __init__(self, title, color):
    self.title = title
    self.color = color

  def info(self):
    return "{}과일은 {}색".format(self.title, self.color)

  def buy1(self, buy1):
    return "{}과일은 {}에서 사야지".format(self.title, buy1)


f = Fruit('apple', 'red')

print(f.info())
print(f.buy1('lotte'))


class Student():
  def __init__(self, id, name, score = 0):
    self.id = id
    self.name = name
    self.score = score

  def get(self):
    return {
      "id": self.id,
      "name": self.name,
      "score": self.score
    }
  def getId(self): return self.id
  def getName(self): return self.name
  def getScore(self): return self.score
  def setScore(self, score): self.score = score

class Cal:
  def __init__(self):
    self.stu = list()

  def add(self, student):
    self.stu.append(student)

  def avg(self):
    sum = 0
    for student in self.stu:
      sum += student.getScore()
    count = len(self.stu)
    avg = sum / count
    return avg, count
  


cal1 = Cal()
user1 = Student(1, '찬웅')

user1.setScore(100)
user2 = Student(2, '예진', 90)
user3 = Student(3, '우정', 80)
user4 = Student(4, '소영', 80)

print(user1.getName())

cal1.add(user1)
cal1.add(user2)
cal1.add(user3)
cal1.add(user4)
avg, count = cal1.avg()

print('평균: {}'.format(avg))
