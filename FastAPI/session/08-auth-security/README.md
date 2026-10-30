# 단원 08. 인증과 보안

## 학습 목표

- 비밀번호 해싱과 사용자 등록/로그인 흐름을 이해합니다.
- OAuth2 Password Flow와 JWT를 구현합니다.
- CORS·미들웨어 등 기본 보안 설정을 적용합니다.

## 레슨 목록

| 레슨 | 제목                     | 파일                                                   |
| ---- | ------------------------ | ------------------------------------------------------ |
| 1    | 비밀번호 해싱과 회원가입 | [01-password-hashing.md](./01-password-hashing.md)     |
| 2    | OAuth2와 JWT             | [02-oauth2-jwt.md](./02-oauth2-jwt.md)                 |
| 3    | CORS와 미들웨어          | [03-cors-middleware.md](./03-cors-middleware.md)       |
| 4    | JWT + DB 실전 통합       | [04-jwt-db-integration.md](./04-jwt-db-integration.md) |

## 단원 체크리스트

- [ ] 평문 비밀번호를 저장하지 않는다
- [ ] Bearer 토큰으로 보호된 엔드포인트를 만들 수 있다
- [ ] CORS를 프론트 도메인에 맞게 설정할 수 있다
