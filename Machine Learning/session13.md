# 세션 13: 문제 1 — Gradient Boosting Classifier (Heart Disease)

<!-- session-nav -->

**이동:** [← 세션 12](./session12.md) · [세션 14 →](./session14.md)

> **이 세션이 하는 일 (쉬운 말)**  
> 심장병 표로 **병이 있는지 없는지(예/아니오)** 를 맞춥니다.  
> 빈칸을 채우고, 표를 나눠 학습한 뒤 **Gradient Boosting**으로 분류합니다.  
> 마지막에 **맞힌 비율**과 **혼동행렬**로 결과를 확인합니다.

## 데이터

| 구분        | 내용                                                              |
| ----------- | ----------------------------------------------------------------- |
| 데이터셋    | Heart Disease Dataset                                             |
| 첨부 파일명 | `heart.csv`                                                       |
| 권장 경로   | `Machine Learning/data/heart.csv`                                 |
| Kaggle      | https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset |

- 카페 첨부 또는 Kaggle에서 확보 후 `data/`에 저장
- Jupyter 경로 제안: `Machine Learning/Jupyter/` (노트북이 아직 없어도 경로만 기준)
- Jupyter 실행 시 데이터는 `../data/heart.csv`로 읽음

> **쉽게 이해하기**  
> 한 줄은 사람 한 명의 건강 수치와 **심장병 여부**입니다.  
> 나이·혈압 같은 **힌트(입력)** 로, 병이 있는지 **이름표(정답)** 를 맞춥니다.  
> 파일을 `data/heart.csv`에 두면, 노트북에서는 `../data/heart.csv`로 읽습니다.

---

## 요구사항 체크리스트

1. 데이터 불러오기
2. 결측치 있으면 평균값으로 대체
3. 학습/테스트 80:20 분할
4. `GradientBoostingClassifier` 학습 — `n_estimators=100`, `learning_rate=0.1`, `max_depth=3`
5. 테스트 예측 후 accuracy 출력
6. Confusion Matrix 출력

> **쉽게 이해하기**  
> 아래 순서대로 하시면 됩니다.
>
> 1. **불러오기**: 표를 올려야 칸을 고르고 모델에 넣을 수 있습니다.
> 2. **빈칸 채우기**: 비어 있는 숫자는 그 칸의 **평균**으로 메웁니다.
> 3. **나누기**: 100명 중 80명은 공부용, 20명은 아직 안 본 시험용입니다.
> 4. **학습**: 약한 나무를 여러 그루 이어 붙이며 틀린 곳을 고칩니다.
> 5. **accuracy(정확도)**: 시험용에서 **맞힌 비율**입니다.
> 6. **Confusion Matrix(혼동행렬)**: 맞힌 것과 틀린 종류를 표로 보여 줍니다.

---

## 핵심 코드 스케치

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("../data/heart.csv")
# X, y 분리 후
df = df.fillna(df.mean(numeric_only=True))   # 결측 → 평균

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=...
)

clf = GradientBoostingClassifier(
    n_estimators=100, learning_rate=0.1, max_depth=3
)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

- session09 Gradient Boosting의 분류 실습 + session07 평가지표(accuracy, Confusion Matrix)와 연결

> **쉽게 이해하기**  
> `n_estimators=100`은 나무를 **100그루** 이어 붙인다는 뜻입니다.  
> `learning_rate=0.1`은 한 번에 **조금**만 고치라는 크기입니다.  
> `max_depth=3`은 나무 질문 깊이를 **얕게** 두어, 외우기만 하는 것을 줄입니다.  
> 시험지 답(`y_test`)과 모델 답(`y_pred`)을 비교해 점수와 혼동행렬을 냅니다.

<!-- session-nav -->

**이동:** [← 세션 12](./session12.md) · [세션 14 →](./session14.md)
