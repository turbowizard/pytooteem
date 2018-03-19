from pytooteem import tag


def test_tag():
    @tag('a')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a>link</a>'


def test_tag_attr():
    @tag('a', href='#')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a href="#">link</a>'


# python 3.6 preserving order!
# def test_tag_attrs():
#     @tag('a', href='#', id='123', qwe='123')
#     def wrap_a(val):
#         return val
#
#     assert wrap_a('link') == '<a href="#" id="123" qwe="123">link</a>'


def test_tag_class():
    @tag('a', clas='class')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a class="class">link</a>'


def test_multiple_per_attr():
    @tag('a', clas='class class')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a class="class class">link</a>'


def test_tag_stacking():
    @tag('a')
    @tag('b')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a><b>link</b></a>'



