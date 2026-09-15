class User:
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email

  def info(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email
    }

  def __str__(self):# 객체 출력시, 자동으로 출력되면서 객체가 문자열로 출력
    return f"{self.id}, {self.name}, {self.email}"

class UserManager:
  users = []
  def list(self):
    return list(self.users)

  def add_user(self, User):
    self.users.append(User)

  def delete_user(self, id):
    user = UserManager.find_user(self, id)
    if user:
      self.users.remove(user)
    else:
      print('none id')

  def find_user(self, user_id):
    for user in self.users:
      if user.id == user_id:
        return user
    return None


user1 = User(1, '가', 'a@domain.com')
user2 = User(2, '나', 'b@domain.com')
user3 = User(3, '다', 'c@domain.com')

manager = UserManager()

manager.add_user(user1)
manager.add_user(user2)
manager.add_user(user3)

manager.delete_user(2)

for user in manager.list():
  print(user)