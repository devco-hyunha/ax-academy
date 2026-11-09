# 세션 30: PCA 실습 — ChurnData

<!-- session-nav -->

**이동:** [← 세션 29](./session29.md) · [세션 31 →](./session31.md)

날짜: 2026.11.05  
카페: [pca - csv](https://cafe.naver.com/f-e/cafes/31780422/articles/632) · [지금까지 한거](https://cafe.naver.com/f-e/cafes/31780422/articles/633) · [PCA](https://cafe.naver.com/f-e/cafes/31780422/articles/634)  
첨부: `ChurnData.csv` → [`data/ChurnData.csv`](./data/ChurnData.csv)  
노트북: `Untitled`(634) → [`Jupyter/14_pca_churn.ipynb`](./Jupyter/14_pca_churn.ipynb)

session29의 **PCA 개념**을 고객 이탈 표로 직접 돌려 봅니다.  
먼저 로지스틱으로 맞춘 뒤, PCA로 칸을 줄여 다시 학습·그려 봅니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 고객 이탈 표를 읽고, 칸을 맞춘 뒤 **로지스틱**으로 이탈을 맞춥니다.  
> 이어서 **PCA**로 “정보가 많은 새 축”을 만들고, 축을 줄인 표로 다시 학습합니다.  
> 마지막에 PC1·PC2로 **점 그림**을 그려 이탈/비이탈을 눈으로 봅니다.

---

## 1. 데이터 · 경로

| 구분        | 내용                                         |
| ----------- | -------------------------------------------- |
| CSV         | [`data/ChurnData.csv`](./data/ChurnData.csv) |
| 노트북 경로 | `../data/ChurnData.csv`                      |
| 라벨        | `churn` (마지막 칸)                          |

```python
df = pd.read_csv("../data/ChurnData.csv")
```

> **쉽게 이해하기**  
> Jupyter 노트북은 `Jupyter/` 폴더가 **현재 위치**입니다.  
> 한 칸 위 `data/` 폴더의 파일은 `../data/파일명.csv`로 가리킵니다.  
> `churn` 칸이 **정답(라벨)** 이고, 나머지 칸이 **힌트(피처)** 입니다.

---

## 2. 노트북 흐름

| 순서 | 내용                                                              |
| ---- | ----------------------------------------------------------------- |
| 1    | CSV 읽기 · 피처/라벨 나누기 (`churn` 제외)                        |
| 2    | Train/Test 80/20 · `StandardScaler`                               |
| 3    | `LogisticRegression(solver='lbfgs')` 학습 · `accuracy_score`      |
| 4    | `PCA` fit/transform · `components_` · `explained_variance_ratio_` |
| 5    | 누적 분산 **90%**에 필요한 주성분 개수 확인                       |
| 6    | `PCA(n_components=13)` 후 로지스틱 재학습 · 정확도                |
| 7    | PC1·PC2 산점도 (`churn` 0/1 색 구분)                              |

> **쉽게 이해하기**  
> 1~3. 먼저 **원래 칸**으로 로지스틱을 돌려 “기준 점수”를 잡습니다.  
> 4~5. PCA로 새 축을 만들고, 각 축이 **정보를 얼마나 담는지**(`explained_variance_ratio_`)를 봅니다.  
> 누적 **90%**는 “원래 퍼짐의 90%를 남기려면 축이 몇 개 필요한가?”입니다.  
> 6. 축을 줄인 표로 다시 맞춰, 칸을 줄여도 실력이 얼마나 남는지 비교합니다.  
> 7. PC1·PC2만으로 점을 찍으면, 이탈(1)과 비이탈(0)이 **눈으로** 갈라지는지 확인할 수 있습니다.

---

## 3. 앞 세션과의 연결

| 세션             | 연결                           |
| ---------------- | ------------------------------ |
| session15·20·28  | 로지스틱 · 표준화 · Churn 분류 |
| session29        | 차원의 저주 · PCA 개념         |
| session30 (이번) | ChurnData PCA 실습             |

> **쉽게 이해하기**  
> session29가 “왜 줄이는가 / PCA가 무엇인가”라면,  
> 이번은 “같은 이탈 표로 **손으로 돌려 보기**”입니다.  
> session28의 분류 숙제와 **같은 주제**, 다른 도구(차원 축소)입니다.

---

## 한눈에

```text
카페 632~634 · Jupyter/14_pca_churn.ipynb
데이터: ../data/ChurnData.csv
스케일 → 로지스틱 → PCA → (90% 축) 재학습 → PC 산점도
```

<!-- session-nav -->

**이동:** [← 세션 29](./session29.md) · [세션 31 →](./session31.md)
