# 세션 13: 문제 1 — Gradient Boosting Classifier (Heart Disease)

## 데이터

| 구분 | 내용 |
| ---- | ---- |
| 데이터셋 | Heart Disease Dataset |
| 첨부 파일명 | `heart.csv` |
| 권장 경로 | `Machine Learning/data/heart.csv` |
| Kaggle | https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset |

- 카페 첨부 또는 Kaggle에서 확보 후 `data/`에 저장
- Jupyter 경로 제안: `Machine Learning/Jupyter/` (노트북이 아직 없어도 경로만 기준)
- Jupyter 실행 시 데이터는 `../data/heart.csv`로 읽음

---

## 요구사항 체크리스트

1. 데이터 불러오기
2. 결측치 있으면 평균값으로 대체
3. 학습/테스트 80:20 분할
4. `GradientBoostingClassifier` 학습 — `n_estimators=100`, `learning_rate=0.1`, `max_depth=3`
5. 테스트 예측 후 accuracy 출력
6. Confusion Matrix 출력

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
