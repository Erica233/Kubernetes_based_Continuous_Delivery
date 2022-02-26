from main import add, sum_list

def test_add():
    assert add(3, 1) == {"total":4}
    
def test_sum_list():
    assert sum_list([1, 2, 2]) == {"total":5}