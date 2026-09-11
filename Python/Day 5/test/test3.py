class Account:
  def __init__(self, name, money):
    self.name = name
    self.money = money

  def deposit(self, money):
    self.money += money

  def withdraw(self, money):
    if self.money < money:
      print('잔액이 부족합니다')
      return
    self.money -= money

  def show_balance(self):
    print(f"{self.name}님의 현재 잔액 {self.money}원")

# 생성자: 이름, 초기금액
# deposit() : 입금
# withdraw() :출금
# show_balance() : 현재 잔액 보이기
# 출금 시 잔액 부족 시 "잔액이 부족하다" 출력


# 객체 생성코드 참고
acc1 = Account("홍길동", 10000)
acc1.show_balance()# -> 홍길동님의 현재 잔액 10000원
acc1.deposit(5000)# -> 현재 금액+5000 원 더하기
acc1.withdraw(3000)# -> 현재 금액 - 3000
acc1.withdraw(20000)#  # 잔액 부족
acc1.show_balance()# -> 홍길동님의 현재 잔액 {}원