# 세션 26: 군집화 — RFM · K-Means · DBSCAN

<!-- session-nav -->

**이동:** [← 세션 25](./session25.md) · [세션 27 →](./session27.md)

날짜: 2026.11.04  
카페: [군집화(RFM - Kmeans, DBSCAN)](https://cafe.naver.com/f-e/cafes/31780422/articles/626)  
첨부: `Untitled9 (2).ipynb` → [`Jupyter/13_rfm_clustering.ipynb`](./Jupyter/13_rfm_clustering.ipynb)

session24·25에서 익힌 **DBSCAN·pandas**를 이어, 쇼핑몰 표로 **고객 RFM**을 만들고 군집화합니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 고객마다 “얼마나 최근에 / 얼마나 자주 / 얼마나 많이 샀는지”를 숫자로 만듭니다.  
> 그 숫자로 **비슷한 손님끼리** K-Means·DBSCAN으로 묶고, 실루엣으로 품질을 봅니다.

---

## 1. RFM이란

| 글자  | 영어      | 쉬운 뜻                                      |
| ----- | --------- | -------------------------------------------- |
| **R** | Recency   | **최근**에 산 지 며칠 지났나 (작을수록 최근) |
| **F** | Frequency | **몇 번** 샀나                               |
| **M** | Monetary  | **얼마** 샀나 (노트북에서는 `TotalPrice`)    |

> **쉽게 이해하기**  
> 단골·큰손·뜸한 손님을 나누려면, 사람마다 세 가지 점수표를 만듭니다.  
> “언제 왔나 / 몇 번 왔나 / 돈은 얼마 썼나”입니다.

---

## 2. 노트북 흐름

1. pandas 복습 (작은 표 · 불리언 인덱싱) — session25와 겹침
2. `online_retail.csv` 읽기 · `CustomerID` 결측 제거
3. 고객별 Recency / Frequency / Monetary(TotalPrice) 만들기
4. `StandardScaler`로 숫자 맞춤
5. K-Means: 실루엣으로 K 고르기 → `n_clusters=4` 등으로 묶기 · 군집별 평균 · 3D 산점도
6. DBSCAN: 밀도 기반 묶기 · `eps` / `min_samples` 튜닝

데이터: [`data/online_retail.csv`](./data/online_retail.csv)  
노트북 경로: `../data/online_retail.csv`

> **쉽게 이해하기**  
> 표를 깨끗이 한 뒤, 고객 한 줄에 R·F·M을 붙입니다.  
> 스케일을 맞춘 다음 K-Means로 “몇 무리?”를 고르고, DBSCAN으로도 같은 표를 묶어 비교합니다.

---

## 3. 앞 세션과의 연결

| 세션             | 연결                                 |
| ---------------- | ------------------------------------ |
| session22~24     | 군집화·K-Means·DBSCAN 개념·기초 실습 |
| session23        | 실루엣 계수                          |
| session25        | pandas 복습                          |
| session26 (이번) | RFM + 실제 고객 표 군집화            |

---

## 한눈에

```text
카페 626 · Jupyter/13_rfm_clustering.ipynb
RFM = Recency / Frequency / Monetary
스케일 → K-Means(+실루엣) · DBSCAN
데이터: online_retail.csv
```

<!-- session-nav -->

**이동:** [← 세션 25](./session25.md) · [세션 27 →](./session27.md)
