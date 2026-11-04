# 세션 27: 문제 1 — Medical Cost 고객 군집화

<!-- session-nav -->

**이동:** [← 세션 26](./session26.md) · [세션 28 →](./session28.md)

날짜: 2026.11.04  
카페: [문제 1](https://cafe.naver.com/f-e/cafes/31780422/articles/628)  
데이터: [Medical Cost Personal Datasets (Kaggle)](https://www.kaggle.com/datasets/mirichoi0218/insurance)

session13의 「문제 1」(Heart 분류)과 **다른 과제**입니다.  
이번은 보험 고객을 **군집화**하는 문제입니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 나이·BMI·흡연·의료비 등으로 고객을 **비슷한 무리**로 나눕니다.  
> K-Means로 묶고, 실루엣으로 품질을 본 뒤, 무리별 평균으로 보험 전략을 생각해 봅니다.

---

## 1. 데이터

| 칸       | 의미                |
| -------- | ------------------- |
| age      | 나이                |
| sex      | 성별                |
| bmi      | 체질량지수          |
| children | 자녀 수             |
| smoker   | 흡연 여부           |
| region   | 지역                |
| charges  | 의료비(보험 청구액) |

사용할 변수(카페 지정): `age`, `bmi`, `children`, `smoker`, `charges`

> **쉽게 이해하기**  
> 한 줄은 보험 고객 한 명입니다.  
> 목표 칸(정답 라벨)을 맞추는 것이 아니라, **비슷한 고객끼리 묶는** 일입니다.

---

## 2. 요구사항 체크리스트

1. `smoker` 등 범주형을 **0/1**로 변환
2. **표준화(Standardization)** 수행
3. **K-Means**로 고객 군집화
4. **실루엣 계수**로 군집 품질 평가
5. 군집별 `age`, `bmi`, `charges` 등 **평균** 분석
6. 군집 특성으로 보험사가 쓸 **전략** 생각해 보기
7. **시각화**

> **쉽게 이해하기**  
> 글자 칸을 숫자로 바꾸고, 단위를 맞춘 뒤 묶습니다.  
> 실루엣은 “무리가 잘 모였나?” 점수입니다(session23).  
> 평균표를 보고 “이 무리는 의료비가 높다”처럼 해석하면 됩니다.

---

## 3. session13과의 구분

|           | session13                  | session27 (이번)         |
| --------- | -------------------------- | ------------------------ |
| 데이터    | heart.csv                  | Medical Cost (insurance) |
| 목표      | 질병 **분류**              | 고객 **군집화**          |
| 대표 모델 | GradientBoostingClassifier | K-Means (+ 실루엣)       |

---

## 한눈에

```text
카페 628 · Kaggle Medical Cost Personal Datasets
변수: age, bmi, children, smoker(0/1), charges
표준화 → K-Means → 실루엣 → 군집별 평균·전략·시각화
Heart 문제 1: session13 (별도)
```

<!-- session-nav -->

**이동:** [← 세션 26](./session26.md) · [세션 28 →](./session28.md)
