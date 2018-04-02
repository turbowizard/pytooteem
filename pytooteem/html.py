# html.py


def __build_attr(arg, val):
    '''Convert key, value to key="value"'''

    return '{arg}s="{val}"'.format(arg=arg, val=val) if arg == 'clas' else '{arg}="{val}"'.format(arg=arg, val=val)


def __build_attrs(kwargs):
    '''Convert args to tag attributes'''

    return ' '.join(__build_attr(arg, kwargs[arg]) for arg in kwargs)


def wraptag(tag_name, **kwargs):
    '''Value wrapper'''

    def decorator(func):
        def wrapper(*inargs):
            return '<{tag}{attrs}>{val}</{tag}>'.format(tag=tag_name,
                                                        val=func(*inargs) if func(*inargs) else '',
                                                        attrs=' '+__build_attrs(kwargs) if kwargs else '')
        return wrapper
    return decorator


def tag(tag_name, *args, **kwargs):
    '''tag stack'''

    def decorator(func):
        if not args:
            def wrapper(*inargs):
                return '<{tag}{attrs}>{html}</{tag}>{val}'.format(tag=tag_name,
                                                                  val=func(*inargs) if func(*inargs) else '',
                                                                  attrs=' ' + __build_attrs(kwargs) if kwargs else '',
                                                                  html='')

            return wrapper
        if isinstance(args[0], str):
            def wrapper(*inargs):
                return '<{tag}{attrs}>{html}</{tag}>{val}'.format(tag=tag_name,
                                                                  val=func(*inargs) if func(*inargs) else '',
                                                                  attrs=' ' + __build_attrs(kwargs) if kwargs else '',
                                                                  html=args[0])

            return wrapper
        try:
            html = type(args[0])
            if hasattr(html, '__len__') and hasattr(html, '__getitem__'):
                def wrapper(*inargs):
                    res = ''
                    for val in args[0]:
                        res += '<{tag}{attrs}>{html}</{tag}>{val}'.format(tag=tag_name,
                                                                          val=func(*inargs) if func(*inargs) else '',
                                                                          attrs=' ' + __build_attrs(kwargs) if kwargs else '',
                                                                          html=val)
                    return res

                return wrapper
        except e:
            raise e



    return decorator


def plain(text):
    '''plain text'''

    def decorator(func):
        def wrapper(*inargs):
            return '{text}{val}'.format(text=text, val=func(*inargs) if func(*inargs) else '')
        return wrapper
    return decorator


def block(block_creator):
    '''tag stack'''
    def decorator(func):
        def wrapper(*inargs):
            return '{block}{val}'.format(block=block_creator(), val=' '.join(func(inarg) for inarg in inargs) if func(*inargs) else '')
        return wrapper
    return decorator


def multiple(*args):
    '''tag stack'''
    print args
    def decorator(func):
        for arg in args:
            def wrapper(*inargs):
                return arg
            return wrapper
    return decorator
