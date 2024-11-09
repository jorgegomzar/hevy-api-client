from typing import Any


def are_dicts_equal(a_doc: dict[Any, Any], b_doc: dict[Any, Any]) -> bool:
    is_match = True
    for key, value in a_doc.items():
        if value != b_doc.get(key, None):
            is_match = False
            break

    return is_match
