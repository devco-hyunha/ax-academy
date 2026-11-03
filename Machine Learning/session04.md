# 세션 04: Pandas

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
> **Pandas** = 파이썬용 **표 작업 도구**.  
> 엑셀에서 하던 “열 고르기, 필터, 평균 내기”를 코드로 하는 느낌입니다.
>
> 두 가지 기본 그릇이 있습니다.
>
> - **Series**: 한 줄(또는 한 열) 데이터 + 이름표(index)
> - **DataFrame**: 여러 열을 붙인 **표**. 우리가 가장 많이 씁니다.
>
> NumPy의 `ndarray`가 “숫자 격자”라면,  
> Pandas는 그 위에 **열 이름·행 이름**을 붙여 “사람이 읽기 쉬운 표”로 만든 것에 가깝습니다.

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
> **Series**는 “값 + 붙임표(index)” 한 줄입니다.  
> NumPy 1차원 배열과 비슷하지만, `0, 1, 2` 대신 `'a', 'b', 'c'`처럼  
> **의미 있는 이름**을 붙일 수 있습니다.
>
> 비유: 출석부의 한 과목 점수 열.  
> 이름(index) 옆에 점수(value)가 적혀 있는 모습입니다.

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
> **DataFrame** = **파이썬 프로그램 안의 엑셀 표**.  
> 행(row) = 한 사람/한 건, 열(column) = Name, Age, Score 같은 항목입니다.
>
> 자주 쓰는 동작만 기억해도 실습이 됩니다.
>
> **파일**
>
> - `read_csv` / `read_excel`: 파일 → 표로 읽기
> - `to_csv`: 표를 파일로 저장 (`index=False`는 행 번호 열을 파일에 안 넣겠다는 뜻)
>
> **먼저 살펴보기** (데이터를 받자마자)
>
> - `head` / `tail`: 앞·뒤 몇 줄만 엿보기
> - `info`: 열 타입, 빈칸(결측치) 힌트
> - `describe`: 숫자 열의 평균·최소·최대 등 요약
> - `shape`: (행 수, 열 수)
>
> **고르기**
>
> - `df["Name"]`: 열 하나 → Series
> - `df[["Name", "Score"]]`: 열 여러 개 → 작은 DataFrame
> - `loc`: **이름(라벨)** 으로 행/칸 고르기
> - `iloc`: **순번(0, 1, 2…)** 으로 고르기  
>   “이름이냐, 몇 번째냐”만 구분하면 됩니다.
>
> **결측치(Missing Value)** = 칸이 비어 있음 (`NaN` 등).  
> 모델은 빈칸을 싫어해서, 지우거나(`dropna`) 숫자로 채웁니다(`fillna`).  
> 평균으로 채우는 것은 “대충 가운데 값으로 메우기”입니다.  
> (참고: `inplace=True`는 새 버전에서 경고가 날 수 있어,  
> `df["Age"] = df["Age"].fillna(df["Age"].mean())`처럼 재대입하는 편이 안전합니다.)

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
> NumPy와 같이, **행↔열을 뒤집기**입니다.  
> 전치 후에는 예전 열 이름(Name, Age…)이 행 쪽으로 가고,  
> 예전 행 번호가 열 쪽으로 갑니다.
>
> ML에서는 보통 “행 = 표본, 열 = Feature”로 둡니다.  
> 어떤 계산은 Feature가 행에 있어야 해서 `T`로 방향을 바꿉니다.  
> “항상 전치한다”가 아니라, **공식·행렬 곱이 요구하는 모양에 맞출 때** 씁니다.

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
