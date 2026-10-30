# 레슨 5. 다대다(M:N) 관계매핑

## 이번 레슨에서 배울 내용

- 연결 테이블로 M:N 관계를 구현하는 방법
- 복합 primary key

---

## 1. 관계 다이어그램

한 노래는 여러 플레이리스트에 들어갈 수 있고, 한 플레이리스트에는 여러 노래가 들어갑니다.

```mermaid
erDiagram
    SONG ||--o{ SONGPLAYLIST : "1:N"
    PLAYLIST ||--o{ SONGPLAYLIST : "1:N"
    SONGPLAYLIST }o--|| SONG : "song_id FK"
    SONGPLAYLIST }o--|| PLAYLIST : "playlist_id FK"
    SONG {
        int id PK
        str title
    }
    PLAYLIST {
        int id PK
        str name
    }
    SONGPLAYLIST {
        int song_id PK
        int playlist_id PK
    }
```

- 다대다(M:N) 관계는 **연결 테이블**(`SONGPLAYLIST`)로 구현
- 연결 테이블은 두 외래키를 복합 primary_key로 가짐
- `Song.playlists` ↔ `SongPlaylist.song`, `Playlist.songs` ↔ `SongPlaylist.playlist`로 3자 관계 구성

---

## 2. M:N 매핑 코드

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy import String, ForeignKey, create_engine

DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine = create_engine(DATABASE_CONN)

# SessionLocal은 세션 자체가 아니라 세션을 만들어 주는 공장
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()  # 새로운 session 객체 생성
    try:
        yield db
    finally:
        db.close()


# Base는 sqlalchemy에서 가져오는 게 아니라 직접 만드는 클래스
class Base(DeclarativeBase):
    pass


class SongPlaylist(Base):
    __tablename__ = "songplaylists"

    song_id: Mapped[int] = mapped_column(ForeignKey("song.id"), primary_key=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlists.id"), primary_key=True)

    # SongPlaylist는 Song 하나를 가리킴(단수) -> Song에서 부르는 이름: playlists
    song: Mapped["Song"] = relationship(back_populates="playlists")
    # SongPlaylist는 Playlist 하나를 가리킴(단수) -> Playlist에서 부르는 이름: songs
    playlist: Mapped["Playlist"] = relationship(back_populates="songs")


class Song(Base):
    __tablename__ = "songs"
    # primary_key이고 + 정수형 -> 자동으로 auto_increment 적용
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))

    playlists: Mapped[list["SongPlaylist"]] = relationship(back_populates="song")


class Playlist(Base):
    __tablename__ = "playlists"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    songs: Mapped[list["SongPlaylist"]] = relationship(back_populates="playlist")


Base.metadata.create_all(bind=engine)
```

핵심:

- `SessionLocal`은 세션 자체가 아니라 세션을 만들어 주는 **공장**(`sessionmaker`)입니다
- 연결 테이블의 두 컬럼이 복합 primary key가 됩니다

```mermaid
flowchart LR
    S[Song] --> SPS[SongPlaylist]
    P[Playlist] --> SPS
    SPS -->|song_id| S
    SPS -->|playlist_id| P
```

---

## 연습 문제

1. Student–Exam M:N 연결 테이블을 설계하세요.
2. 연결 테이블에 복합 primary key를 지정하세요.
3. 양쪽 relationship를 `back_populates`로 연결하세요.
</contents>
