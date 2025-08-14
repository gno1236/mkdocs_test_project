"""샘플 파이프라인 모듈.

mkdocstrings가 파싱할 수 있도록 Google 스타일 Docstring을 사용합니다.
"""

from typing import Any, Dict, List


def preprocess(data: List[int]) -> List[int]:
    """간단 전처리.

    Args:
        data: 정수 리스트 입력.

    Returns:
        음수를 제거하고 오름차순으로 정렬된 리스트.

    Raises:
        TypeError: 입력이 리스트가 아니거나 정수가 아닌 경우.
    """
    if not isinstance(data, list) or any(not isinstance(x, int) for x in data):
        raise TypeError("data must be a list of ints")
    return sorted([x for x in data if x >= 0])


def core_compute(a: int, b: int) -> int:
    """핵심 연산(비공개로 둘 수도 있음).

    Args:
        a: 피연산자 1.
        b: 피연산자 2.

    Returns:
        a와 b의 합.
    """
    return a + b


def postprocess(value: int) -> Dict[str, Any]:
    """후처리 및 포맷.

    Args:
        value: 결과 정수.

    Returns:
        결과 메타정보를 포함한 딕셔너리.
    """
    return {"result": value, "ok": True}


def run_pipeline(data: List[int]) -> Dict[str, Any]:
    """엔드-투-엔드 파이프라인.

    Args:
        data: 정수 리스트 입력.

    Returns:
        파이프라인 최종 결과 딕셔너리.
    """
    clean = preprocess(data)
    total = 0
    for x in clean:
        total = core_compute(total, x)
    return postprocess(total)
