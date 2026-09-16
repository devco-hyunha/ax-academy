from config import STATUS, CODE

REQUIRED_FIELDS = ['uid', 'username', 'email', 'password']

class SignupService:
  def __init__(self, store):
    self.store = store

  def validateUid(self, value):
    if len(value) < 3:
      return {
        'target': 'uid',
        'status': STATUS['ERROR'],
        'code': CODE['INVALID_UID'],
      }

    duplicateResult = self.store.findBy('users', 'uid', value)
    if duplicateResult.get('status') == STATUS['SUCCESS']:
      return {
        'target': 'uid',
        'status': STATUS['ERROR'],
        'code': CODE['DUPLICATE_DATA'],
      }
    return None

  def validateEmail(self, value):
    if '@' not in value or '.' not in value:
      return {
        'target': 'email',
        'status': STATUS['ERROR'],
        'code': CODE['INVALID_EMAIL'],
      }
    return None
  
  def validatePassword(self, value):
    if len(value) < 8:
      return {
        'target': 'password',
        'status': STATUS['ERROR'],
        'code': CODE['INVALID_PASSWORD'],
      }
    return None

  def validateUsername(self, value):
    if len(value) < 3:
      return {
        'target': 'username',
        'status': STATUS['ERROR'],
        'code': CODE['INVALID_USERNAME'],
      }
    return None
  
  def validate(self, user):
    errors = []

    for key in REQUIRED_FIELDS:
      value = user.get(key)
      if value is None or value == '':
        errors.append({
          'target': key,
          'status': STATUS['ERROR'],
          'code': CODE['MISSING_REQUIRED_DATA'],
        })
        continue

      validator = {
        'uid': self.validateUid,
        'email': self.validateEmail,
        'password': self.validatePassword,
        'username': self.validateUsername,
      }.get(key)
      if validator is not None:
        error = validator(value)
        if error is not None:
          errors.append(error)

    if errors:
      return {
        'status': STATUS['ERROR'],
        'data': { 'errors': errors },
      }
    return {
      'status': STATUS['SUCCESS'],
      'code': CODE['DATA_VALID'],
    }

  def create(self, data):
    result = self.store.create('users', data)
    if result.get('status') == STATUS['ERROR']:
      return result
    return {
      'status': STATUS['SUCCESS'],
      'code': CODE['DATA_SAVED'],
      'data': result.get('data'),
    }