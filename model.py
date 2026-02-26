def predict(value: float) -> int:
    """
    Simple threshold classifier
    """
    if value > 0.5:
        return 1
    return 0
