class LoginViews:
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

  def display_error(self):
    print('-'*50)
    print()
    print(f"{'Failed to login. Please try again.':^50}")
    print()
    print('-'*50)
    print()