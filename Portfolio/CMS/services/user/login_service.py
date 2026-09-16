from config import STATUS, CODE

class LoginService():
  def __init__(self, store):
    self.store = store

  def failedLogin():
    return {
      'status': STATUS['ERROR'],
      'code': CODE['FAILED_LOGIN'],
    }

  def login(self, data):
    findResult = self.store.findBy('users', 'uid', data.get('uid'))
    if findResult.get('status') == STATUS['ERROR']:
      return LoginService.failedLogin()

    if findResult['data']['password'] != data.get('password'):
      return LoginService.failedLogin()

    del findResult['data']['password']
    return findResult