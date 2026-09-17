# 정규 표현식
import re

# [a-zA-z] 모든 알파벳
# [0-9] 모든 숫자
# \d: 숫자 [0-9]와 동일
# \D: 숫자가 아닌 문자 [^0-9]와 동일
# \s: 공백
# \S: 공백이 아닌 문자
# \w: 문자 + 숫자 [a-zA-Z0-9_]와 동일
# \W: 문자 + 숫자가 아닌 문자 [^a-zA-Z0-9_]와 동일

# [dot] 문자 - \n을 제외한 모든 문자

p = re.compile("[a-z]+")

# match, search

m = p.match('python')
print(m)

m = p.match('3 python')
print(m)

m = p.search('python')
print(m)

m = p.search('3 python')
print(m)


def email(text):
    pattern=r'^[\w+]+@[\w]+\.[\w.]+$'
    return re.match(pattern, text)

print(email("test@naver.com")) #매치됨  @기호들어가야함
print(email("test-naver-com")) #매치안됨

# #010-1234-5678
# #p.358,361
# def phone_number(text):
#     pattern=r'010-\d{3,4}-\d{4}'
#     return re.findall(pattern,text)


# text="내 연락처는 010-1234-5678이고 동생 연락처는 010-994-3433입니다"
# print(phone_number(text))

#p.376
# p=re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m=p.search("park 010-1234-1234")
# print(m.group("name"))
# print(m.group(2))
# print(m.group(3))