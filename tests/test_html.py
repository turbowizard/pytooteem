from pytooteem import tag


def test_tag():
    '''Test tag wrap'''
    @tag('a')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a>link</a>'


def test_tag_attr():
    '''Test single attribute'''
    @tag('a', href='#')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a href="#">link</a>'


# python 3.6 preserving order!
# def test_tag_attrs():
#     '''Test multiple attributes'''
#     @tag('a', href='#', id='123', qwe='123')
#     def wrap_a(val):
#         return val
#
#     assert wrap_a('link') == '<a href="#" id="123" qwe="123">link</a>'


def test_tag_class():
    '''Test class attribute'''
    @tag('a', clas='class')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a class="class">link</a>'


def test_multiple_per_attr():
    '''Test multiple per attribute'''
    @tag('a', clas='class class')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a class="class class">link</a>'


def test_tag_stacking():
    '''Test tag stacking'''
    @tag('a')
    @tag('b')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a><b>link</b></a>'



