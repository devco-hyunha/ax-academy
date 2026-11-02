# 세션 04: Pandas

- Pandas는 데이터 분석을 위해 만들어진 라이브러리
- Series data type과 DataFrame data type으로 구성됨

## Series (1차원) — numpy array와 유사

- 1차원 데이터 (열/벡터 형태), 인덱스(index)와 값(value)으로 구성

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30
```

## DataFrame (2차원, table) — Python program 안의 Excel

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

## Pandas transpose

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
