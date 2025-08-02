from src.math_operations import add,sub

def test_add():
    a, b = 2, 3
    result = add(a, b)
    print(f"add({a}, {b}) = {result}")
    assert result == 6

    a, b = -1, 1
    result = add(a, b)
    print(f"add({a}, {b}) = {result}")
    assert result == 0
    
def test_sub():
    cases = [(5, 3), (4, 3), (3, 3), (2, 3)]
    for a, b in cases:
        result = sub(a, b)
        print(f"sub({a}, {b}) = {result}")
        expected = a - b
        assert result == expected