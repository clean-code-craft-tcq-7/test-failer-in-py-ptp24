from tshirts import size


def test_size_small():
    assert size(0) == 'S'
    assert size(37) == 'S'
    assert size(37.9) == 'S'

def test_size_medium():
    assert size(38) == 'M'
    assert size(39) == 'M'
    assert size(41.9) == 'M'
    assert size(40) == 'M'

def test_size_large():
    assert size(42) == 'L'
    assert size(50) == 'L'
    assert size(100) == 'L'

def test_size_boundaries():
    assert size(38) == 'M'
    assert size(42) == 'L'
    assert size(37.99) == 'S'
    assert size(41.99) == 'M'
    assert size(42.01) == 'L'