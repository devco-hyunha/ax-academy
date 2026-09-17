from utils import padByDisplayWidth

class SystemViews:

  def headline(*contents):
    print(f"⌜{'-'*48}⌝")
    print(f"|{' '*48}|")
    for content in contents:
      print(f"|{padByDisplayWidth(content, 48, align='center')}|")
    print(f"|{' '*48}|")
    print(f"⌞{'-'*48}⌟")

  def menu(*menus):
    for index, menu in enumerate(menus):
      print(f'  [{index + 1}] {menu}')
  def choice(placeholder, max, min = 1):
    while True:
      print('-'*50)
      value = input(f'{placeholder} >>> ').strip()
    
      if value is None: 
        continue
      else:
        try:
          value = int(value)
          if min > value or value > max:
            SystemViews.errorMessage(f'{min}-{max}사이의 숫자를 입력해 주세요')
            continue
          else:
            return value
        except ValueError:
          SystemViews.errorMessage('숫자를 입력해 주세요')
          continue

  def errorMessage(message):
    print()
    print('-'*50)
    print()
    print(f'[System] {message}')