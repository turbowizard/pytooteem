from pytooteem import wraptag, tag, plain, block


def test_wraptag():
    '''Test wraptag wrap'''
    @wraptag('a')
    def wrap_a(h):
        return h

    assert wrap_a('link') == '<a>link</a>'


def test_warptag_attr():
    '''Test single attribute'''
    @wraptag('a', href='#')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a href="#">link</a>'


# python 3.6 preserving order!
# def test_wraptag_attrs():
#     '''Test multiple attributes'''
#     @wraptag('a', href='#', id='123', qwe='123')
#     def wrap_a(val):
#         return val
#
#     assert wrap_a('link') == '<a href="#" id="123" qwe="123">link</a>'


def test_wraptag_class():
    '''Test class attribute'''
    @wraptag('a', clas='class')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a class="class">link</a>'


def test_wraptag_multiple_per_attr():
    '''Test multiple per attribute'''
    @wraptag('a', clas='class class')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a class="class class">link</a>'


def test_wraptag_stacking():
    '''Test wraptag stacking'''
    @wraptag('a')
    @wraptag('b')
    def wrap_a(val):
        return val

    assert wrap_a('link') == '<a><b>link</b></a>'


def test_tag():
    '''Test stacktag'''
    @tag('a')
    def wrap_a():
        return 'link'

    assert wrap_a() == '<a></a>link'


def test_stacktag_attr():
    '''Test single attribute'''
    @tag('a', href='#')
    def wrap_a():
        pass

    assert wrap_a() == '<a href="#"></a>'


def test_wrap_stack():
    @tag('li')
    @tag('li')
    @tag('li')
    def li():
        pass

    assert li() == '<li></li><li></li><li></li>'


def test_plain():
    @tag('li')
    @plain('plain')
    @tag('li')
    def plain_text():
        pass

    assert plain_text() == '<li></li>plain<li></li>'


def test_tag_with_html():
    @tag('li', 'html')
    def tag_with_html():
        pass

    assert tag_with_html() == '<li>html</li>'


def test_block():

    @plain('block')
    def myblock():
        pass

    @block(myblock)
    def make_block():
        pass

    assert make_block() == 'block'


def test_return_mupltiple():

    @tag('b', ['b1', 'b2'])
    def buttons():
        pass


    assert buttons() == '<b>b1</b><b>b2</b>'


def test_return_mupltiple_block():

    @tag('b', ['b1', 'b2'])
    def buttons():
        pass

    @block(buttons)
    def my_block():
        pass

    assert my_block() == '<b>b1</b><b>b2</b>'
