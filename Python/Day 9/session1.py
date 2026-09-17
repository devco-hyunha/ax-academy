# 가변 인자

def find_max(*args):
  if not args:
    return None
  return max(args)

print(find_max(3, 8, 2))
print(find_max())

# 구매할 수량 (qty)이 재고보다 많으면
class OutofCtockError(Exception):
  pass


# 수량 (qty)이 0 이하이면
class InvalidError(Exception):
  pass

class Product:
  def __init__(self, name, stock):
    self.name = name
    self.stock = stock

  def sell(self, qty):
    if qty < 0:
      raise InvalidError('수량을 잘못 입력')
    if qty > self.stock:
      raise OutofCtockError('재고 부족')
    self.stock -= qty
    print(f'{self.name} {qty}개 판매')

product = Product('노트북', 5)

product.sell(2)

print(product.stock)# 3

try:
  product.sell(10)

except OutofCtockError as e:
  print(e)
except InvalidError as e:
  print(e)

