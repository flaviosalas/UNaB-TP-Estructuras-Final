import pytest

@pytest.fixture
def valor_entrada():
   input = 42
   return input

def test_dividible_por_2(valor_entrada):
   assert valor_entrada % 2 == 0

def test_dividible_por_4(valor_entrada):
   assert valor_entrada % 4 == 0

def test_dividible_por_6(valor_entrada):
   assert valor_entrada % 6 == 0

def test_dividible_por_8(valor_entrada):
   assert valor_entrada % 8 == 0





   