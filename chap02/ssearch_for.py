#for문으로 작성한 선형 검색 알고리즘


from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i #검색성공 (인덱스를 반환)
    return -1 #검색 실패 (-1을 반환)
