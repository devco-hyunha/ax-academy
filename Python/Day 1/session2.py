escape_code = """ 활용도가 높은 Escape 코드
\n : 개행 (enter)
\t : 탭 (tab)
\\ : 문자(백슬래시)
\' : 문자(작은따옴표)
\" : 문자(큰따옴표)
\000 : Null 문자
"""

print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print("It\'s Python")
print("\"Hello\"")

print("""python
well
come""")

print('''python
well
come''')
print() # 빈 줄 출력

food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he said.'
print(say)

say2 = "'Python is very easy.' he said."
print(say2)

# 문자열 연산
head = "Python"
tail = " is fun"
print(head + tail)
print(head * 2)
print(len(head))
