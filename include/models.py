
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP, TEXT, JSON

Base = declarative_base()


# class Snapshot(Base):
#     __tablename__ = "snapshot"
#     id = Column(Integer, primary_key=True)
#     snap_date = Column(TIMESTAMP)
#     usa = Column(TEXT)
#     canada = Column(TEXT)
#     europe = Column(TEXT)
#     britain = Column(TEXT)
#     new_zeland = Column(TEXT)
#     turkey = Column(TEXT)
#     brazil = Column(TEXT)
#     china = Column(TEXT)
#     russia = Column(TEXT)

#     def __repr__(self) -> str:
#         return f"date: {self.snap_date}"


class Snapshot_Json(Base):
    __tablename__ = "snapshot_json"
    id = Column(Integer, primary_key=True)
    snap_date = Column(TIMESTAMP)
    body = Column(JSON)

    def __repr__(self) -> str:
        return f"date: {self.snap_date}"
