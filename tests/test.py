from mypackage import myModule

def test_top_n():
    '''
    make sure top_n works correctly
    '''

    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect'
    assert myModule.top_n([10,4,5,6,7], 2) == [10,7], 'incorrect'
    assert myModule.top_n([1,2,3,4,5], 5) == [5,4,3,2,1], 'incorrect'
    