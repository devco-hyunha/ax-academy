# 세션 28: 문제 2 — Customer Churn 로지스틱 회귀

<!-- session-nav -->

**이동:** [← 세션 27](./session27.md) · [세션 29 →](./session29.md)

날짜: 2026.11.04  
카페: [문제 2](https://cafe.naver.com/f-e/cafes/31780422/articles/627)  
데이터: Kaggle **Customer Churn Dataset** (Predict Customer's Retention)

session14의 「문제 2」(California Housing 회귀)와 **다른 과제**입니다.  
이번은 고객 **이탈(Churn)** 을 로지스틱으로 맞추는 문제입니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 통신·구독 서비스에서 “이 고객이 **떠날까, 남을까?**”를 맞춥니다.  
> 표를 **공부용/시험용**으로 나누고, 칸 크기를 맞춘 뒤 **로지스틱**으로 학습합니다.  
> 맞힌 비율뿐 아니라, **정밀도·재현율·F1**과 **혼동행렬**, **합격선(threshold)** 까지 봅니다.

---

## 1. 데이터

- Kaggle: Customer Churn Dataset (고객 유지·이탈 예측)
- 카페 본문에 데이터셋 링크가 있습니다.

> **쉽게 이해하기**  
> **Churn(이탈)** 은 “서비스를 해지한 고객”입니다.  
> 표의 각 줄은 한 고객이고, 칸에는 이용 패턴·요금 같은 **힌트**가 있습니다.  
> 목표는 그 힌트로 “떠날까?”를 **예/아니오**로 맞추는 **분류**입니다.  
> 집값을 맞추던 session14와 달리, 이번 답은 **숫자 하나**가 아니라 **두 갈래**입니다.

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
> 1~2. 표를 **공부용 80% / 시험용 20%**로 나누고, 칸마다 단위가 달라도 공정하도록 **크기(스케일)** 를 맞춥니다.  
> 3~4. **로지스틱**은 “이탈 확률”을 내는 분류기입니다. `predict`는 예/아니오, `predict_proba`는 **0~1 점수**입니다.  
> 5~6. **정확도**만 보면 부족할 수 있어, **정밀도**(이탈이라 한 것 중 진짜 비율) · **재현율**(진짜 이탈을 얼마나 잡았는지) · **F1**(둘의 균형)과 **혼동행렬**(맞힌/틀린 표)을 봅니다.  
> 7~8. **threshold(합격선)** 는 “이 점수 이상이면 이탈”입니다. 0.3으로 낮추면 이탈이라고 **더 많이** 말하고, 0.7로 높이면 **더 까다롭게** 말합니다(session20과 같은 아이디어).

---

## 3. 앞 세션과의 연결

| 세션             | 연결                                       |
| ---------------- | ------------------------------------------ |
| session15·20     | 로지스틱·시그모이드·임계값·F1              |
| session14        | 예전의 「문제 2」(회귀) — 이번과 주제 다름 |
| session28 (이번) | Churn 분류 숙제                            |

> **쉽게 이해하기**  
> 로지스틱·임계값 이론은 session15·20에서 이미 봤습니다.  
> 이번은 **고객 이탈 표**로 그 도구를 **숙제처럼 끝까지** 돌려 보는 세션입니다.

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

**이동:** [← 세션 27](./session27.md) · [세션 29 →](./session29.md)
