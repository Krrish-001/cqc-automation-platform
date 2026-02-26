from app.model import predict

def test_positive_prediction():
    assert predict(0.8) == 1

def test_negative_prediction():
    assert predict(0.2) == 0
