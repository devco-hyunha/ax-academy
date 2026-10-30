# 단원 03. 요청 본문과 Pydantic

## 학습 목표

- Pydantic 모델로 JSON Body를 정의합니다.
- 필드 검증, 중첩 모델, 예제를 다룹니다.
- Body와 Path/Query를 함께 사용하는 방법을 익힙니다.

## 레슨 목록

| 레슨 | 제목                  | 파일                                                 |
| ---- | --------------------- | ---------------------------------------------------- |
| 1    | Pydantic 모델 기초    | [01-pydantic-basics.md](./01-pydantic-basics.md)     |
| 2    | Request Body 다루기   | [02-request-body.md](./02-request-body.md)           |
| 3    | 중첩 모델과 고급 검증 | [03-nested-validation.md](./03-nested-validation.md) |
| 4    | Form 데이터 처리      | [04-form-data.md](./04-form-data.md)                 |

## 단원 체크리스트

- [ ] `BaseModel`로 요청 스키마를 정의할 수 있다
- [ ] POST/PUT에서 JSON Body를 받을 수 있다
- [ ] `Field`, `model_validator`로 검증할 수 있다
