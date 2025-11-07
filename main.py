from enum import Enum
class Status(Enum):
    OCCUPIED = 0 #데이터를 저장
    EMPTY = 1 # 비어 있음
    DELETED = 2 #삭제 완료


print(Status(0))  # OCCUPIED
print(Status(1))  # EMPTY
print(Status(2))  # DELETED
