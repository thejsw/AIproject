# 📚 Today I Learned - SQL (SELECT)

## 🎯 Basic Query Structure

```sql
SELECT column
FROM table
WHERE condition;
```

- `SELECT` : 조회할 컬럼 선택
- `FROM` : 데이터를 가져올 테이블 지정
- `WHERE` : 조건에 맞는 데이터만 필터링

---

## 📝 BETWEEN / NOT BETWEEN

`BETWEEN`은 범위(이상 ~ 이하)를 조회할 때 사용합니다.

### Q. Find the movies not released in the years between 2000 and 2010

```sql
SELECT *
FROM movies
WHERE year NOT BETWEEN 2000 AND 2010;
```

✅ `NOT BETWEEN` : 지정한 범위를 제외한 데이터를 조회

---

## 🔍 LIKE

`LIKE`를 사용하면 문자열 패턴 검색이 가능합니다.

- `%` : 0개 이상의 모든 문자열

예시) `"%키워드%"`

### Q. Find all the WALL-* movies

```sql
SELECT *
FROM movies
WHERE title LIKE "WALL-%";
```

✅ `LIKE "WALL-%"` : `WALL-`로 시작하는 모든 영화 검색