# 세션 25: 지금까지 한 코드 — pandas 복습

<!-- session-nav -->

**이동:** [← 세션 24](./session24.md) · [세션 26 →](./session26.md)

날짜: 2026.11.04  
카페: [지금까지 한 코드](https://cafe.naver.com/f-e/cafes/31780422/articles/624)  
첨부: `Untitled9.ipynb` → 로컬 [`Jupyter/12_pandas_review.ipynb`](./Jupyter/12_pandas_review.ipynb)

수업에서 지금까지 쓴 **표(pandas) 다루는 코드**를 한곳에 모은 복습 노트북입니다.  
군집화(session22~24)와 별개로, **표를 고르는 기본기**를 다시 봅니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 작은 표로 **칸 고르기**, **조건에 맞는 줄만 남기기**, **한 줄 집기**를 연습합니다.  
> 이어서 온라인 쇼핑몰 CSV를 읽고, **CustomerID가 비어 있는 줄**을 걸러 냅니다.

---

## 1. 노트북 흐름

| 순서 | 내용                                                                     |
| ---- | ------------------------------------------------------------------------ |
| 1    | 작은 DataFrame 만들기 (이름·색·순위)                                     |
| 2    | `df['이름']` → Series / `df[['이름']]` → DataFrame                       |
| 3    | **불리언 인덱싱**: `df[df['순위'] < 3]`, `df[df['색']=='red']`           |
| 4    | `df.iloc[0]` — 위치(행 번호)로 한 줄 가져오기                            |
| 5    | `online_retail.csv` 읽기 → `CustomerID` 결측 확인 → `notnull()`로 남기기 |

> **쉽게 이해하기**  
> **Series**는 칸 하나짜리 줄(세로 한 줄)입니다.  
> **DataFrame**은 칸이 여러 개인 표입니다.  
> `df[조건]`은 시험에서 “이 조건 맞는 사람만 남기기”와 같습니다.

---

## 2. 자주 쓰는 문법

| 코드                             | 쉬운 뜻                              |
| -------------------------------- | ------------------------------------ |
| `df['칸']`                       | 그 칸만 (Series)                     |
| `df[['칸']]`                     | 그 칸만인데 표 모양 유지 (DataFrame) |
| `df[df['순위'] < 3]`             | 순위가 3보다 작은 **행만**           |
| `df[df['색']=='red']`            | 색이 red인 **행만**                  |
| `df.iloc[0]`                     | **0번 자리** 행                      |
| `df['CustomerID'].isna().sum()`  | CustomerID가 비어 있는 개수          |
| `df[df['CustomerID'].notnull()]` | CustomerID가 **있는** 행만 남김      |

> **쉽게 이해하기**  
> `isna()`는 “비었나?”, `notnull()`은 “값이 있나?”입니다.  
> 값이 있는 행만 다시 `df`에 넣으면, 빈 CustomerID 줄은 버려집니다.

---

## 3. 데이터 경로

로컬 파일: [`data/online_retail.csv`](./data/online_retail.csv)

노트북에서는 아래로 읽습니다.

```python
df = pd.read_csv("../data/online_retail.csv")
```

> **쉽게 이해하기**  
> Jupyter는 노트북이 있는 `Jupyter/` 폴더가 기준입니다.  
> 그래서 한 칸 위의 `data/`는 `../data/파일명.csv`로 가리킵니다.

---

## 4. 앞 세션과의 연결

| 세션             | 연결                                |
| ---------------- | ----------------------------------- |
| session04        | Pandas 기초 개념                    |
| session08 등     | 실습에서 표 고르기·결측 처리        |
| session25 (이번) | 오늘 수업 코드를 한 노트북으로 복습 |

---

## 한눈에

```text
카페 article 624 · Untitled9 → Jupyter/12_pandas_review.ipynb
Series vs DataFrame, 불리언 인덱싱, iloc
online_retail: CustomerID 결측 확인 후 notnull로 필터
경로: ../data/online_retail.csv
이전: session24 DBSCAN 실습
다음: session26 RFM 군집화
```

<!-- session-nav -->

**이동:** [← 세션 24](./session24.md) · [세션 26 →](./session26.md)
