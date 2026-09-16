import os
import sys
from managers import DataManager
from controllers import UserController

basePath = os.path.dirname(__file__)

store = DataManager(basePath=basePath)
userController = UserController(store)
# store.saveData('users', data=[{
#   'name': 'John Doe',
#   'age': 30,
#   'email': 'john.doe@example.com'
# }])

def beforeLoginMenu():
  print('1. Signup')
  print('2. Login')
  print('3. Exit')
  choice = input('Enter your choice: ')
  return choice if choice in ['1', '2', '3'] else None
def afterLoginMenu():
  print('1. Logout')
  print('2. Exit')
  choice = input('Enter your choice: ')
  return choice if choice in ['1', '2'] else None

def main():
  print('Welcome to the CMS')
  while True:
    if userController.isLoggedIn():
      print(f'Welcome, {userController.getCurrentUser().get("name")}')
      choice = afterLoginMenu()
      if choice == '1':
        userController.logout()
      elif choice == '2':
        sys.exit(0)
    else:
      print('Please login to continue')
      choice = beforeLoginMenu()
      if choice == '1':
        userController.signup()
      elif choice == '2':
        userController.login()
      elif choice == '3':
        sys.exit(0)


if __name__ == '__main__':
  main()