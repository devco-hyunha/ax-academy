# Machine Learning Study

머신러닝 학습 노트 저장소입니다. 세션별로 내용을 정리합니다.

## 처음 읽는 분

이 폴더는 **파이썬·Jupyter를 처음 쓰는 분**도 따라 올 수 있게 적어 두었습니다.

1. **순서:** [`session01.md`](./session01.md)부터 번호 순으로 읽습니다. 각 문서 위·아래 **이동** 링크로 이전·다음 세션을 열 수 있습니다.
2. **세션 vs 노트북:** `sessionNN.md`는 **개념·순서** 설명입니다. `Jupyter/01_`~`12_` 노트북은 **손으로 실행하는 실습**입니다. 번호는 실습 순서라 **세션 번호와 같지 않을 수** 있습니다(B안).
3. **데이터:** CSV는 [`data/`](./data/)에 둡니다. 노트북에서는 보통 `../data/파일명.csv`로 읽습니다.
4. **읽는 팁:** 본문의 **이 세션이 하는 일**과 **쉽게 이해하기**를 먼저 읽은 뒤, 표·코드를 보시면 부담이 덜합니다.

## 세션 목록

- [`session01.md`](./session01.md) — 기본 개념, 진행 순서흐름
- [`session02.md`](./session02.md) — Jupyter Notebook 설치 및 사용
- [`session03.md`](./session03.md) — Numpy
- [`session04.md`](./session04.md) — Pandas
- [`session05.md`](./session05.md) — Matplotlib
- [`session06.md`](./session06.md) — 분류 모델 (Decision Tree, 앙상블)
- [`session07.md`](./session07.md) — 검증 방식 및 평가지표
- [`session08.md`](./session08.md) — 타이타닉 데이터셋 (데이터 구조·유형, 정규화, fit/transform/predict)
- [`session09.md`](./session09.md) — 지니 불순도 & Gradient Boosting
- [`session10.md`](./session10.md) — 회귀 입문 (단순·다중 선형, MSE, 경사하강법, 규제)
- [`session11.md`](./session11.md) — 당뇨병 회귀 & R²
- [`session12.md`](./session12.md) — 오후 실습 (Titanic Bagging / Social_Network_Ads)
- [`session13.md`](./session13.md) — 문제 1 — Gradient Boosting Classifier (Heart Disease)
- [`session14.md`](./session14.md) — 문제 2 — California Housing (선형·다중 회귀)
- [`session15.md`](./session15.md) — 머신 러닝 5 (회귀 심화 · 로지스틱 회귀)
- [`session16.md`](./session16.md) — 머신 러닝 5-1 (트리 계열 회귀기)
- [`session17.md`](./session17.md) — 하이퍼파라미터 튜닝 (GridSearchCV & RandomizedSearchCV)
- [`session18.md`](./session18.md) — 다이아몬드 회귀 (Feature와 이상치)
- [`session19.md`](./session19.md) — 다이아몬드 회귀 완성 (선형·Ridge·Lasso·ElasticNet·교차검증·log1p)
- [`session20.md`](./session20.md) — 로지스틱 회귀 실습 이어서 (Social_Network_Ads)
- [`session21.md`](./session21.md) — 문제 1 — Students Performance
- [`session22.md`](./session22.md) — 머신 러닝 6 (군집화 · K-Means · 유클리드 거리)
- [`session23.md`](./session23.md) — 머신 러닝 7 (실루엣 계수 · DBSCAN core/border)
- [`session24.md`](./session24.md) — 군집화 실습 (K-Means · DBSCAN 노트북)
- [`session25.md`](./session25.md) — 지금까지 한 코드 (pandas 복습 · 불리언 인덱싱)

## Jupyter 실습 파일

`01_`~`12_` 접두 번호는 **실습 진행 순서**이며, 세션 번호와 무관합니다(B안).

- [`Jupyter/01_numpy_basics.ipynb`](./Jupyter/01_numpy_basics.ipynb) — NumPy 입문
- [`Jupyter/02_titanic_classification.ipynb`](./Jupyter/02_titanic_classification.ipynb) — 타이타닉 분류·앙상블
- [`Jupyter/03_diabetes_regression.ipynb`](./Jupyter/03_diabetes_regression.ipynb) — 당뇨병 회귀
- [`Jupyter/04_breast_cancer_missing.ipynb`](./Jupyter/04_breast_cancer_missing.ipynb) — 유방암 결측 처리
- [`Jupyter/05_social_network_ads_rf.ipynb`](./Jupyter/05_social_network_ads_rf.ipynb) — Social_Network_Ads RF
- [`Jupyter/06_ads_logistic_regression.ipynb`](./Jupyter/06_ads_logistic_regression.ipynb) — Social_Network_Ads 로지스틱·임계값·F1
- [`Jupyter/07_california_housing_tuning.ipynb`](./Jupyter/07_california_housing_tuning.ipynb) — GridSearchCV·RandomizedSearchCV
- [`Jupyter/08_diamonds_eda.ipynb`](./Jupyter/08_diamonds_eda.ipynb) — 다이아몬드 EDA·IQR 이상치
- [`Jupyter/09_diamonds_regression.ipynb`](./Jupyter/09_diamonds_regression.ipynb) — 다이아몬드 회귀 완성본(선형·Ridge·Lasso·ElasticNet·교차검증·로그 변환)
- [`Jupyter/10_students_performance.ipynb`](./Jupyter/10_students_performance.ipynb) — Students Performance EDA·math score 회귀(입문·확장)
- [`Jupyter/11_dbscan_clustering.ipynb`](./Jupyter/11_dbscan_clustering.ipynb) — K-Means·DBSCAN 군집화 실습
- [`Jupyter/12_pandas_review.ipynb`](./Jupyter/12_pandas_review.ipynb) — pandas 복습(Series·불리언 인덱싱·결측 필터)

## 파일 규칙

- 각 세션은 `sessionNN.md`로 순번을 매긴다
- 새 세션이 추가되면 session25.md 이후부터 이어간다
