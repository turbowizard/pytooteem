# html.py


def __build_attr(arg, val):
    '''Convert key, value to key="value"

        Execpetions:
            1. arg == 'clas' -> arg = 'class'
            disabled:
            2. arg == 'attrs_withdash' -> arg = 'attrs-withdash'
    '''

    # support class as attribute
    if arg == 'clas':
        arg = 'class'
    # enable key underscore to dash
    # if '_' in arg:
    #     arg = arg.replace('_', '-')
    return '{arg}="{val}"'.format(arg=arg, val=val)


def __build_attrs(kwargs):
    '''Converts kwargs to tag attributes'''

    return ' '.join(__build_attr(arg, kwargs[arg]) for arg in kwargs)


def __build_tag(tag, *args, **kwargs):
    '''Converts argumets to tag'''
    return '<{tag}{attrs}>{html}</{tag}>'.format(tag=tag,
                                                 attrs=' ' + __build_attrs(kwargs) if kwargs else '',
                                                 html=args[0] if args else '')


def __stack(block, next=''):
    '''stack format'''
    return '{block}{next}'.format(block=block, next=next)


def __make_next(func):
    '''Create next element if exists'''
    try:
        next = func()
        if next:
            return next
    except Exception as e:
        print e
    return ''


def wraptag(tag_name, **kwargs):
    '''Wraps next element with tag

        @wraptag('div')
        @wraptag('div', id='div1')
        @wraptag('div', clas='container')
        @wraptag('div', at-tr='value')
    '''

    def decorator(func):
        def wrapper():
            return '<{tag}{attrs}>{next}</{tag}>'.format(tag=tag_name,
                                                         next=__make_next(func),
                                                         attrs=' '+__build_attrs(kwargs) if kwargs else '')
        return wrapper
    return decorator


def tag(tag_name, *args, **kwargs):
    '''Stacks next element current tag

        @tag('div')
        @tag('div', 'content')
        @tag('div', style='background:Green;')
        @tag('div', 'content', 'background:Green;')
        @tag('button', ('Home', 'about'))
    '''
    def decorator(func):
        if not args:
            def wrapper_no_args():
                return __stack(__build_tag(tag_name, **kwargs), __make_next(func))
            return wrapper_no_args
        elif isinstance(args[0], str):
            def wrapper():
                return __stack(__build_tag(tag_name, args[0], **kwargs), __make_next(func))
            return wrapper
        try:
            html = type(args[0])
            if hasattr(html, '__len__') and hasattr(html, '__getitem__'):
                def wrapper():
                    res = ''
                    for val in args[0]:
                        res += '<{tag}{attrs}>{html}</{tag}>{val}'.format(tag=tag_name,
                                                                          val=__make_next(func),
                                                                          attrs=' ' + __build_attrs(kwargs) if kwargs else '',
                                                                          html=val)
                    return res

                return wrapper
        except Exception as e:
            raise e
    return decorator


def plain(text):
    '''Stacks plain text

        @plain('<plain>')
    '''

    def decorator(func):
        def wrapper():
            return __stack(text, next=__make_next(func))
        return wrapper
    return decorator


def block(block_func):
    '''Stacks block

        @block(block_function)
    '''
    def decorator(func):
        def wrapper():
            return __stack(block_func(), next=__make_next(func))
        return wrapper
    return decorator


def data(dataa):
    '''Stacks data-recipe combination

        @data(((d11, d11),(d21, d22)))
    '''

    def decorator(func):
        def wrapper():
            a = ''
            for element in dataa:
                a += '{block}'.format(block=func(element))
            return a
        return wrapper
    return decorator




