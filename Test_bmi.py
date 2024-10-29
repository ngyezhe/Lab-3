import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert bmi.calculator_bmi(1.75,70) == 0
def test_bmi_over_weight():
    assert bmi.calculator_bmi(1.75, 80) == 1
def test_bmi_under_weight():
    assert bmi.calculator_bmi(1.75, 50) == -1