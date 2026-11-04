# 세션 04: Pandas

<!-- session-nav -->
**이동:** [← 세션 03](./session03.md) · [세션 05 →](./session05.md)

Pandas는 표 형태 데이터를 다루는 파이썬 라이브러리입니다. CSV·엑셀처럼 생긴 자료를 읽고, 고르고, 비운 칸을 채우는 일을 쉽게 해 줍니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 오늘은 **표(엑셀처럼 생긴 데이터)** 를 파이썬 안에서 다루는 도구 **Pandas**를 배웁니다.  
> 한 줄짜리 **Series**, 표 전체인 **DataFrame**,  
> 파일 읽기·앞부분 보기·행/열 고르기·빈칸(결측치) 처리를 익힙니다.  
> 실습에서 “데이터를 눈으로 확인하는” 대부분의 작업이 여기서 이뤄집니다.

---

## 1. Pandas 구성

- Pandas는 데이터 분석을 위해 만들어진 라이브러리
- Series data type과 DataFrame data type으로 구성됨

> **쉽게 이해하기**  
> **Pandas**는 표 형태 데이터를 다루는 라이브러리입니다.  
> **Series**는 한 열(값+index), **DataFrame**은 여러 열이 붙은 표입니다.  
> NumPy **ndarray**에 열·행 이름을 붙인 형태라고 보면 됩니다.

---

## 2. Series (1차원) — numpy array와 유사

- 1차원 데이터 (열/벡터 형태), 인덱스(index)와 값(value)으로 구성

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30
```

> **쉽게 이해하기**  
> **Series**는 값과 **index(인덱스, 이름표)** 한 줄입니다.  
> 0, 1, 2 대신 `'a', 'b', 'c'`처럼 의미 있는 이름을 붙일 수 있습니다.

---

## 3. DataFrame (2차원, table) — 파이썬 프로그램 안의 엑셀

- 2차원 데이터 (엑셀 표처럼 행과 열 구조), 행(row)과 열(column)에 이름 붙여서 다룸

```python
data = {
    "Name": ["Tom", "Jerry", "Anna"],
    "Age": [20, 21, 19],
    "Score": [85, 90, 88]
}
df = pd.DataFrame(data)
print(df)
```

- 입출력:

```python
pd.read_csv("data.csv")
pd.read_excel("data.xlsx")
df.to_csv("result.csv", index=False)   # 저장
```

- 기초 확인:

```python
df.head(5)        # 상위 5행 출력
df.tail(3)        # 마지막 3행 출력
df.info()         # 데이터 요약 (결측치, 타입)
df.describe()     # 수치형 요약 통계 (평균, 표준편차, 분위수 등)
df.shape          # (행, 열) 크기
df.columns        # 열 이름
df.index          # 행 인덱스
```

- 열 선택:

```python
df["Name"]           # 특정 열 선택
df[["Name", "Score"]]  # 여러 열 선택
```

- 행 선택:

```python
df.loc[0]         # 인덱스 이름 기반 선택
df.iloc[0]        # 행 번호 기반 선택
df.loc[0, "Name"] # 특정 행과 열 선택
```

- 결측치 처리:

```python
df.dropna()             # 결측치 있는 행 제거
df.fillna(0)            # 결측치 0으로 채움
df["Age"].fillna(df["Age"].mean(), inplace=True) # 평균으로 채움
```

> **쉽게 이해하기**  
> **DataFrame**은 행이 한 건, 열이 항목인 표입니다.  
> `read_csv`·`head`·`info`·`describe`로 읽고 훑습니다. `loc`는 이름, `iloc`는 순번으로 고릅니다.  
> **결측치(missing value, 빈칸)** 는 `dropna`로 지우거나 `fillna`로 채웁니다.  
> `df["Age"] = df["Age"].fillna(...)`처럼 재대입하는 편이 안전합니다.

---

## 4. Pandas transpose

- Pandas는 `DataFrame.T`와 `df.transpose()`로 행·열을 전치한다.

```python
import pandas as pd

data = {
    "Name": ["Tom", "Jerry", "Anna"],
    "Age": [20, 21, 19],
    "Score": [85, 90, 88]
}
df = pd.DataFrame(data)

print(df.T)
print(df.transpose())
```

- 전치 후 index가 columns가 되고, columns가 index가 된다.
- ML 전처리에서 열이 features·행이 표본으로 배치된 `X`를 전치하면 features가 행으로 배치된 형태가 되므로, 연산 방향에 따라 전치 방향을 판단한다.

> **쉽게 이해하기**  
> `df.T`는 행과 열을 바꿉니다.  
> 보통 행은 표본, 열은 **피처(feature)** 입니다.  
> 계산이 요구하는 모양에 맞출 때만 전치합니다.

---

## 복습 체크 (스스로)

1. Series와 DataFrame의 차이는 무엇인가요?
2. DataFrame을 “파이썬 안의 엑셀”이라고 부르는 이유는 무엇인가요?
3. `loc`과 `iloc`의 차이는 무엇인가요?
4. `head`, `info`, `describe`는 각각 무엇을 보나요?
5. 결측치를 다루는 대표적인 두 가지 방법은 무엇인가요?

<details>
<summary>답 보기</summary>

1. Series는 1차원(값+index), DataFrame은 여러 열을 가진 2차원 표.
2. 행·열에 이름을 붙여 표처럼 읽고 고르고 저장할 수 있어서.
3. loc은 인덱스 이름(라벨), iloc은 행/열 순번(위치)으로 선택.
4. head=앞부분 엿보기, info=타입·결측 요약, describe=숫자 열 통계 요약.
5. 제거(`dropna`)와 채우기(`fillna`, 예: 0 또는 평균).

</details>

<!-- session-nav -->
**이동:** [← 세션 03](./session03.md) · [세션 05 →](./session05.md)
