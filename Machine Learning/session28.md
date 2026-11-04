# 세션 28: 문제 2 — Customer Churn 로지스틱 회귀

<!-- session-nav -->

**이동:** [← 세션 27](./session27.md)

날짜: 2026.11.04  
카페: [문제 2](https://cafe.naver.com/f-e/cafes/31780422/articles/627)  
데이터: Kaggle **Customer Churn Dataset** (Predict Customer's Retention)

session14의 「문제 2」(California Housing 회귀)와 **다른 과제**입니다.  
이번은 고객 **이탈(Churn)** 을 로지스틱으로 맞추는 문제입니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 고객이 **남을지 / 떠날지**를 맞춥니다.  
> 표를 나누고 숫자를 맞춘 뒤 로지스틱으로 학습하고,  
> 정확도·정밀도·재현율·F1과 혼동행렬, **임계값**을 바꿔 가며 봅니다.

---

## 1. 데이터

- Kaggle: Customer Churn Dataset (고객 유지·이탈 예측)
- 카페 본문에 데이터셋 링크가 있습니다.

> **쉽게 이해하기**  
> **Churn(이탈)** = 서비스를 그만둔 고객입니다.  
> 목표는 “떠날까?”를 **예/아니오**로 맞추는 **분류**입니다.

---

## 2. 요구사항 체크리스트

1. Train/Test 분리 (**80% / 20%**)
2. Feature **표준화** (`StandardScaler`)
3. **Logistic Regression** 학습 (`solver='lbfgs'`)
4. 테스트 예측: `predict`, `predict_proba`
5. **Accuracy, Precision, Recall, F1-score** 계산
6. **혼동행렬** 시각화
7. 기본 **threshold = 0.5**
8. threshold **0.3, 0.7**로 바꿔 1로 예측된 샘플 수 · Precision · Recall · F1 확인

> **쉽게 이해하기**  
> 공부용·시험용으로 표를 나눈 뒤, 칸 크기를 맞추고 로지스틱을 학습합니다.  
> 확률을 구한 다음, “이 점수 이상이면 이탈”이라는 **합격선(threshold)** 을 바꿉니다.  
> 낮추면 이탈이라고 더 많이 말하고, 높이면 더 까다롭게 말합니다(session20과 같은 아이디어).

---

## 3. 앞 세션과의 연결

| 세션             | 연결                                       |
| ---------------- | ------------------------------------------ |
| session15·20     | 로지스틱·시그모이드·임계값·F1              |
| session14        | 예전의 「문제 2」(회귀) — 이번과 주제 다름 |
| session28 (이번) | Churn 분류 숙제                            |

---

## 한눈에

```text
카페 627 · Customer Churn (Kaggle)
80/20 분할 → StandardScaler → LogisticRegression(lbfgs)
predict / predict_proba → Accuracy·Precision·Recall·F1·혼동행렬
threshold 0.5 / 0.3 / 0.7 비교
California 문제 2: session14 (별도)
```

<!-- session-nav -->

**이동:** [← 세션 27](./session27.md)
