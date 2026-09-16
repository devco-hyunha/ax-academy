import time
from config import STATUS
from services import LoginService, SignupService
from views import LoginViews, SignupViews

class UserController():
  def __init__(self, store):
    self.signupService = SignupService(store)
    self.loginService = LoginService(store)
    self.signupViews = SignupViews()
    self.loginViews = LoginViews()
    self.currentUser = None

  def isLoggedIn(self):
    return self.currentUser is not None

  def getCurrentUser(self):
    return self.currentUser

  def logout(self):
    self.currentUser = None

  def login(self):
    uid = input('Enter your user id: ')
    password = input('Enter your password: ')
    data = {
      'uid': uid,
      'password': password
    }

    result = self.loginService.login(data)
    if result.get('status') == STATUS['ERROR']:
      self.loginViews.display_error()
    else:
      self.loginViews.display_success()
      self.currentUser = result.get('data')

  def signup(self):
    uid = input('Enter your user id: ')
    username = input('Enter your username: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    currentTime = int(time.time())
    data = {
      'uid': uid,
      'username': username,
      'email': email,
      'password': password,
      'createdAt': currentTime,
      'updatedAt': currentTime
    }

    validateResult = self.signupService.validate(data)
    if validateResult.get('status') == STATUS['ERROR']:
      self.signupViews.display_error(validateResult['data']['errors'])
      return validateResult
    else:
      self.signupViews.display_success()
      return self.signupService.create(data)
