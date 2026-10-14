# Session 4 — NoSQL

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 3 — 정규화](unit3_advanced/session3.md) · 다음: [Session 5 — Redis](unit3_advanced/session5.md)

## 1. NoSQL 개요

- **RDB의 한계극복하기 위한 데이터 저장소의 새로운 형태**
- RDB와는 달리 **고정된 테이블 스키마가 없음**
- 데이터 구조를 **필요에 따라 변경할 수 있음** (JSON, XML 등)
- **대용량의 데이터를 저장**할 수 있음
- 대규모 데이터 처리할 때 적합

## 2. NoSQL의 유형

### 키-값 저장소 (Key-Value Store)
- 가장 단순한 구조, 키(key)를 통해 값(value) 조회
- 예: Redis, DynamoDB, Memcached
- 단순 조회 속도가 매우 빠름

### 문서 저장소 (Document Store)
- JSON/BSON 형태의 문서 단위로 저장
- 스키마가 유연하며 필드 추가/수정이 용이
- 예: MongoDB, CouchDB

### 열 저장소 (Column-Family Store)
- 칼럼을 그룹화하여 저장, 분석 워크로드에 최적화
- 예: Cassandra, HBase

### 그래프 저장소 (Graph Store)
- 노드와 엣지로 관계 표현, 연결된 데이터 쿼리에 최적화
- 예: Neo4j, Amazon Neptune

## 3. RDB vs NoSQL 비교

| 구분 | RDB | NoSQL |
|------|-----|-------|
| 스키마 | 고정된 테이블 스키마 | 유연한 스키마 |
| 트랜잭션 | ACID 지원 | BASE 모델, 최종 일관성 |
| 확장성 | 수직 확장 (Vertical) | 수평 확장 (Horizontal) |
| 조인 성능 | 조인 효율적 | 조인 비효율적 (애플리케이션 레벨 처리) |
| 사용 목적 | 트랜잭션 처리, 복잡한 쿼리 | 대용량 데이터, 실시간 웹, 모바일 |

## 4. 정리

1. **NoSQL**: RDB의 한계를 극복하기 위한 데이터 저장소의 새로운 형태
2. **고정된 테이블 스키마가 없음**, 데이터 구조를 유연하게 변경 가능
3. **대용량 데이터 처리**에 적합
4. 유형: 키-값, 문서, 열, 그래프 저장소
5. RDB와 다른 트레이드오프 존재 (ACID vs BASE)

---

## [이전: Session 3 — 정규화](unit3_advanced/session3.md) · [다음: Session 5 — Redis](unit3_advanced/session5.md)
