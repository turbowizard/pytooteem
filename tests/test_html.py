from pytooteem import wraptag, tag, plain, block, data


def test_wraptag_wrap_return():
    '''Test wraptag wrap'''
    @wraptag('a')
    def link():
        return 'link'

    assert link() == '<a>link</a>'


def test_warptag_attr_return():
    '''Test single attribute'''
    @wraptag('a', href='#')
    def ahref():
        return 'link'

    assert ahref() == '<a href="#">link</a>'


# python 3.6 preserving order- not passing on 2.7!
# def test_wraptag_attrs():
#     '''Test multiple attributes'''
#     @wraptag('a', href='#', id='123', qwe='123')
#     def wrap_a(val):
#         return val
#
#     assert wrap_a('link') == '<a href="#" id="123" qwe="123">link</a>'


def test_wraptag_underscore_to_dash_attrs():
    '''Test dash attribute'''
    @wraptag('a', at_tr='attr')
    def aclass():
        return 'link'

    # assert aclass() == '<a at-tr="attr">link</a>'
    assert aclass() == '<a at_tr="attr">link</a>'


def test_wraptag_class_attribure():
    '''Test class attribute'''
    @wraptag('a', clas='class')
    def aclass():
        return 'link'

    assert aclass() == '<a class="class">link</a>'


def test_wraptag_multiple_per_attr():
    '''Test multiple per attribute'''
    @wraptag('a', clas='class class')
    def aclassdouble():
        pass

    assert aclassdouble() == '<a class="class class"></a>'


def test_wrap_chain():
    '''Test wraptag stacking'''
    @wraptag('a')
    @wraptag('b')
    def b_in_a():
        pass

    assert b_in_a() == '<a><b></b></a>'


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
    @tag('li1')
    @tag('li2')
    @tag('li3')
    def li():
        pass

    assert li() == '<li1></li1><li2></li2><li3></li3>'


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


def test_block_stacking():

    @plain('block1')
    def myblock1():
        pass

    @plain('block2')
    def myblock2():
        pass

    @block(myblock1)
    @block(myblock2)
    def make_block():
        pass

    assert make_block() == 'block1block2'


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


def test_return_mupltiple_block_wrapped():

    @wraptag('ul')
    @tag('li', ['l1', 'l2'])
    def buttons():
        pass


    @block(buttons)
    def my_block():
        pass

    assert my_block() == '<ul><li>l1</li><li>l2</li></ul>'


def test_block_from_recipe():

    def thumbnail_blueprint():
        @wraptag('li')
        @tag('a', 'a')
        @tag('p', ['p1', 'p2'])
        def make_thumbnail():
            pass
        return make_thumbnail()

    @block(thumbnail_blueprint)
    def my_block():
        pass

    assert my_block() == '<li><a>a</a><p>p1</p><p>p2</p></li>'


def test_block_from_recipe_with_data():

    @data((('11', '12'), ('21', '22')))
    def thumbnail_blueprint(element):
        @wraptag('ul')
        @tag('li', element[0])
        @tag('li', element[1])
        def make_thumbnail():
            pass
        return make_thumbnail()

    @block(thumbnail_blueprint)
    def my_block():
        pass

    assert my_block() == '<ul><li>11</li><li>12</li></ul><ul><li>21</li><li>22</li></ul>'
