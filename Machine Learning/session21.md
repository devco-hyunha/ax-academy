# 세션 21: 문제 1 — Students Performance

session13의 「문제 1」은 Heart Disease **분류**(GBC)였습니다.  
이번 「문제 1」은 Students Performance 표로 **시험 점수**를 다루는 **새 문제**입니다.

실습 노트북: [`Jupyter/10_students_performance.ipynb`](./Jupyter/10_students_performance.ipynb)  
데이터: [`data/StudentsPerformance.csv`](./data/StudentsPerformance.csv)

> **이 세션이 하는 일 (쉬운 말)**  
> 학생 한 줄 = 한 명.  
> 배경 칸과 점수 칸이 있고, **math score**를 맞춥니다.  
> 입문 = 점수만. 확장 = 결측·IQR·Label Encoding까지.

---

## 1. 데이터 칸 설명

| 칸 | 의미 |
| -- | ---- |
| gender | 성별 |
| race/ethnicity | 인종·민족 그룹 |
| parental level of education | 부모 학력 |
| lunch | 점심 유형 (표준 / 무료·감면) |
| test preparation course | 시험 준비 과정 여부 |
| math score | 수학 점수 |
| reading score | 읽기 점수 |
| writing score | 쓰기 점수 |

- 파일: `StudentsPerformance.csv` (약 1000행)
- Jupyter에서: `pd.read_csv('../data/StudentsPerformance.csv')`

---

## 2. 타겟 후보

맞출 답을 고를 때 후보입니다.

| 후보 | 성격 |
| ---- | ---- |
| **math score** | 수학 점수 (회귀 입문·확장 공통 타겟) |
| **reading score** | 읽기 점수 |
| **writing score** | 쓰기 점수 |
| (응용) 세 점수의 평균 | 전체 성적 한 줄 요약 |

노트북은 **math score**를 맞춥니다. 셋 다 숫자라 회귀 타겟이 됩니다.

---

## 3. EDA 포인트

1. **shape** — 행·열 개수
2. **head / dtypes** — 앞줄과 칸 타입(숫자 vs 글자)
3. **결측** — `isna().sum()`으로 비어 있는 칸 확인
4. **점수 describe · hist · boxplot** — 요약·분포·튀는 점
5. **범주 value_counts** — 성별·점심 등이 몇 명씩인지

> **쉽게 이해하기**  
> 모델 전에 표 모양만 짧게 봅니다.  
> 빈 칸이 많은지, 점수가 한쪽에만 몰렸는지도 봅니다.

---

## 4. 입문 vs 확장 (노트북과 같음)

| | 입문 | 확장 |
| - | ---- | ---- |
| Feature | reading · writing **점수만** | 범주(Label Encoding) + reading · writing |
| 이상치 | 없음 | 점수 칸 **IQR 1.5**로 줄 제거 |
| 모델 | LinearRegression (다중선형) | 같은 LinearRegression |
| 점수 | **MSE · R²** | **MSE · R²** |

입문은 숫자만으로 빠르게 한 번.  
확장은 글자→번호, 튀는 점수 정리 후 다시 맞춤.

---

## 5. 범주형 인코딩이 필요한 이유

`gender`, `lunch` 같은 칸은 **글자**입니다. 많은 모델은 **숫자**만 받습니다.  
**Label Encoding** = 글자를 번호로 바꿈. 배경 칸을 Feature에 넣을 때 필요하고, 입문(점수만)은 건너뜁니다.

---

## 6. session13과의 구분 (한 줄)

| | session13 | session21 (이번) |
| - | --------- | ---------------- |
| 데이터 | heart.csv | StudentsPerformance.csv |
| 목표 | 질병 여부 **분류** | 시험 점수 **회귀·EDA** |
| 대표 모델 | GradientBoostingClassifier | LinearRegression (입문·확장) |

> **쉽게 이해하기**  
> 제목이 둘 다 「문제 1」이어도 숙제가 다릅니다.  
> Heart = 예/아니오. Students = **몇 점?**

---

## 한눈에

```text
데이터: StudentsPerformance.csv (1000행)
타겟: math score
EDA: shape, dtypes, 결측, hist, boxplot, value_counts
입문: 점수만 → 다중선형 → MSE·R²
확장: IQR + Label Encoding + 다중선형 → MSE·R²
노트북: Jupyter/10_students_performance.ipynb
Heart 문제 1: session13 (별도)
```
