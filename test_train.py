# tests/test_train.py
from src.train import train

def test_train_runs():
    assert train() is None
