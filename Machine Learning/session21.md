# 세션 21: 문제 1 — Students Performance

<!-- session-nav -->

**이동:** [← 세션 20](./session20.md) · [세션 22 →](./session22.md)

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

| 칸                          | 의미                         |
| --------------------------- | ---------------------------- |
| gender                      | 성별                         |
| race/ethnicity              | 인종·민족 그룹               |
| parental level of education | 부모 학력                    |
| lunch                       | 점심 유형 (표준 / 무료·감면) |
| test preparation course     | 시험 준비 과정 여부          |
| math score                  | 수학 점수                    |
| reading score               | 읽기 점수                    |
| writing score               | 쓰기 점수                    |

- 파일: `StudentsPerformance.csv` (약 1000행)
- Jupyter에서: `pd.read_csv('../data/StudentsPerformance.csv')`

> **쉽게 이해하기**  
> 표의 한 줄은 **학생 한 명**입니다.  
> 위쪽 칸은 배경(성별·점심 등)이고, 아래쪽 칸은 **시험 점수**입니다.  
> 영어 칸 이름이 낯설면, 표의 「의미」 열만 먼저 보시면 됩니다.

---

## 2. 타겟 후보

맞출 답을 고를 때 후보입니다.

| 후보                  | 성격                                 |
| --------------------- | ------------------------------------ |
| **math score**        | 수학 점수 (회귀 입문·확장 공통 타겟) |
| **reading score**     | 읽기 점수                            |
| **writing score**     | 쓰기 점수                            |
| (응용) 세 점수의 평균 | 전체 성적 한 줄 요약                 |

노트북은 **math score**를 맞춥니다. 셋 다 숫자라 회귀 타겟이 됩니다.

> **쉽게 이해하기**  
> **타겟**은 “맞출 답”입니다.  
> 여기서는 **수학 점수**를 맞춥니다. 읽기·쓰기 점수는 힌트로 쓸 수 있습니다.  
> 점수는 연속 숫자라 **회귀**(숫자를 맞추기) 문제입니다.

---

## 3. EDA 포인트

1. **shape** — 행·열 개수
2. **head / dtypes** — 앞줄과 칸 타입(숫자 vs 글자)
3. **결측** — `isna().sum()`으로 비어 있는 칸 확인
4. **점수 describe · hist · boxplot** — 요약·분포·튀는 점
5. **범주 value_counts** — 성별·점심 등이 몇 명씩인지

> **쉽게 이해하기**  
> **EDA**(탐색적 데이터 분석)는 모델 전에 표 상태를 짧게 점검하는 일입니다.  
> 빈 칸이 얼마나 있는지, 점수가 한쪽으로 쏠렸는지 먼저 확인합니다.

---

## 4. 입문 vs 확장 (노트북과 같음)

|         | 입문                         | 확장                                     |
| ------- | ---------------------------- | ---------------------------------------- |
| Feature | reading · writing **점수만** | 범주(Label Encoding) + reading · writing |
| 이상치  | 없음                         | 점수 칸 **IQR 1.5**로 줄 제거            |
| 모델    | LinearRegression (다중선형)  | 같은 LinearRegression                    |
| 점수    | **MSE · R²**                 | **MSE · R²**                             |

입문은 숫자만으로 빠르게 한 번.  
확장은 글자→번호, 튀는 점수 정리 후 다시 맞춤.

> **쉽게 이해하기**  
> **입문**은 읽기·쓰기 점수만으로 수학 점수를 맞춥니다.  
> **확장**은 성별 같은 글자 칸을 번호로 바꾸고, 점수가 너무 튀는 줄도 정리한 뒤 다시 맞춥니다.  
> 둘 다 같은 직선 모델(`LinearRegression`)을 쓰고, **MSE·R²**로 점수를 봅니다.

---

## 5. 범주형 인코딩이 필요한 이유

`gender`, `lunch` 같은 칸은 **글자**입니다. 많은 모델은 **숫자**만 받습니다.  
**Label Encoding** = 글자를 번호로 바꿈. 배경 칸을 Feature에 넣을 때 필요하고, 입문(점수만)은 건너뜁니다.

> **쉽게 이해하기**  
> 컴퓨터 모델은 보통 **숫자만** 받습니다.  
> `male` / `female` 같은 글자는 **0, 1**처럼 번호로 바꿉니다. 이를 **Label Encoding**이라고 합니다.  
> 입문(점수만)에서는 이 단계가 필요 없습니다.

---

## 6. session13과의 구분 (한 줄)

|           | session13                  | session21 (이번)             |
| --------- | -------------------------- | ---------------------------- |
| 데이터    | heart.csv                  | StudentsPerformance.csv      |
| 목표      | 질병 여부 **분류**         | 시험 점수 **회귀·EDA**       |
| 대표 모델 | GradientBoostingClassifier | LinearRegression (입문·확장) |

> **쉽게 이해하기**  
> **session13**과 같이 「문제 1」이어도 과제 종류가 다릅니다.  
> 심장 질병 표는 **예·아니오** 분류입니다.  
> 학생 성적 표는 **점수**를 맞추는 회귀입니다.

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

<!-- session-nav -->

**이동:** [← 세션 20](./session20.md) · [세션 22 →](./session22.md)
