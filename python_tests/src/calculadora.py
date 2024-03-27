def soma(a, b):
    '''Soma a e b

    >>> soma(10,20)
    30

    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: a precisa ser int ou float
    '''
    assert isinstance(a, (int, float)), 'a precisa ser int ou float'
    assert isinstance(b, (int, float)), 'a precisa ser int ou float'
    return a + b


def subtrai(a, b):
    '''subtrai a e b

    >>> subtrai(10,20)
    -10

    >>> subtrai('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: a precisa ser int ou float
    '''
    assert isinstance(a, (int, float)), 'a precisa ser int ou float'
    assert isinstance(b, (int, float)), 'a precisa ser int ou float'
    return a - b


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)