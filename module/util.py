"""
dictionary형을 받아서 value값 기준으로 정렬
"""
def sort_items(items: dict) -> list:
    return sorted(items.items(), reverse=True, key=lambda item: item[1])
