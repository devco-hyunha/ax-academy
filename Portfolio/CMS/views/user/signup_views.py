class SignupViews:
  def __init__(self):
    pass

  def display_success(self):
    print()
    print('-'*50)
    print()
    print(f"{'User created successfully':^50}")
    print()
    print('-'*50)
    print()

  def display_error(self, errors):
    print('-'*50)
    print()
    print(f"{'Failed to signup. Please try again.':^50}")
    print()
    print('-'*50)

    print()
    print('check the following errors:')
    print()
    for error in errors:
      target = error.get('target')
      code = error.get('code')
      print(f' - {target:<10} : {code}')
    print()