# 세션 13: 문제 1 — Gradient Boosting Classifier (Heart Disease)

> **이 세션이 하는 일 (쉬운 말)**  
> 심장병 데이터로 **“병이 있다 / 없다”** 를 가리는 분류 과제를 합니다.  
> 모델은 **Gradient Boosting Classifier**(약한 모델들을 이어서 고쳐 가는 앙상블)입니다.  
> 체크리스트 순서대로 불러오기 → 결측 처리 → 분할 → 학습 → accuracy·Confusion Matrix까지 한 바퀴 돕니다.

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

> **쉽게 이해하기**  
> 각 줄 = 한 사람(또는 한 건의 기록).  
> 여러 검사·특징 열과, 맞추고 싶은 **목표 열**(심장병 여부)이 함께 있습니다.  
> 파일이 없으면 학습이 시작되지 않으니, 먼저 `data/heart.csv`에 두는 것이 1번 과제입니다.  
> Jupyter에서 `../data/`로 읽는 이유: 노트북이 `Jupyter/` 폴더에 있을 때, 한 단계 위 `data/`를 가리키기 위함입니다.

---

## 요구사항 체크리스트

1. 데이터 불러오기
2. 결측치 있으면 평균값으로 대체
3. 학습/테스트 80:20 분할
4. `GradientBoostingClassifier` 학습 — `n_estimators=100`, `learning_rate=0.1`, `max_depth=3`
5. 테스트 예측 후 accuracy 출력
6. Confusion Matrix 출력

> **쉽게 이해하기**  
> 각 단계가 **왜** 필요한지, 짧게만 보면 다음과 같습니다.
>
> 1. **불러오기**: 표(`DataFrame`)로 올려야 열을 나누고 모델에 넣을 수 있습니다.  
> 2. **결측 → 평균**: 빈칸이 있으면 많은 모델이 학습을 거부하거나 이상해집니다.  
>    숫자 열의 빈칸을 **그 열의 평균**으로 채우라는 지시입니다. (완벽한 방법은 아니지만, 과제에서 정한 규칙입니다.)  
> 3. **80:20 분할**: 전부로 공부하면 “외운 문제만 잘 푸는” 착각이 납니다.  
>    80%로 배우고, **안 본 20%**로 진짜 실력을 봅니다.  
> 4. **GradientBoostingClassifier**: 틀린 곳을 다음 나무가 보완하는 방식으로 여러 번 쌓습니다.  
>    - `n_estimators=100`: 나무(약한 학습기)를 100개 정도 쌓음  
>    - `learning_rate=0.1`: 한 번에 얼마나 크게 고칠지(너무 크면 흔들림)  
>    - `max_depth=3`: 나무 깊이 제한 → 한 나무가 너무 복잡하지 않게  
> 5. **accuracy**: 테스트에서 “맞힌 비율”. 직관적이지만, 클래스 불균형이 크면 한계도 있습니다.  
> 6. **Confusion Matrix**: 단순 정답률이 아니라,  
>    참양성·거짓양성·거짓음성 등을 **표로** 보여 어디서 틀렸는지 봅니다.  
>    (의료처럼 “놓침”이 위험한 과제에서 특히 중요합니다.)

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
> 스케치의 흐름을 말로 옮기면 이렇습니다.
>
> 1. CSV를 표로 읽는다  
> 2. **X**(특징들)와 **y**(심장병 여부 등 정답)를 나눈다  
> 3. 숫자 결측을 평균으로 채운다  
> 4. `train_test_split`으로 학습용·시험용을 나눈다 (`test_size=0.2` = 20% 시험)  
> 5. `fit`으로 학습, `predict`로 시험 예측  
> 6. accuracy와 Confusion Matrix를 출력한다  
>
> `random_state`를 고정하면, 다시 실행해도 **같은 분할**이 나와 결과 비교가 쉽습니다.  
> (`...` 자리에는 과제에서 쓰는 정수, 예: 42 등을 넣으면 됩니다.)
>
> **Gradient Boosting이 하는 일(한 줄)**  
> 약한 모델을 여러 개 **이어 붙이면서**, 앞에서 틀린 부분을 다음이 보완합니다.  
> “한 번에 완벽한 선생님”보다 “틀린 숙제만 골라 다시 가르치는 선생님”에 가깝습니다.

---

## 복습 체크 (스스로)

1. 학습/테스트를 나누는 이유는 무엇인가요?
2. 결측치를 평균으로 채우라는 지시가 의미하는 바는 무엇인가요?
3. `n_estimators`, `learning_rate`, `max_depth`는 각각 무엇을 조절하나요?
4. accuracy만 보면 부족한 경우가 있다면, Confusion Matrix는 무엇을 더 보여 주나요?

<details>
<summary>답 보기</summary>

1. 학습에 쓰지 않은 데이터로 일반화 성능을 보기 위함입니다. 전부 학습하면 외운 것처럼 보일 수 있습니다.
2. 빈칸(결측)을 그 열의 평균값으로 채워, 모델이 학습할 수 있게 하는 전처리입니다.
3. 나무 개수(얼마나 많이 쌓을지) / 한 걸음 크기 / 한 나무의 복잡도(깊이)입니다.
4. 어디서 틀렸는지(예: 병인데 정상이라 함)를 표로 보여 줍니다. 단순 “몇 % 맞음”보다 실수 종류가 보입니다.

</details>
