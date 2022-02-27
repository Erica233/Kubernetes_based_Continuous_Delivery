from main import add, cal_profit

def test_add():
    assert add(3, 1) == {"total":4}
    
def test_cal_profit():
    assert cal_profit(100, 120) == {"profit_margin":0.2}