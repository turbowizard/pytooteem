
def __build_attr(arg, val):
    return '{arg}s="{val}"'.format(arg=arg, val=val) if arg == 'clas' else '{arg}="{val}"'.format(arg=arg, val=val)


def __build_attrs(kwargs):
    return ' '.join(__build_attr(arg, kwargs[arg]) for arg in kwargs)


def tag(tag, **kwargs):
    def decorator(func):
        def wrapper(wrap_this):
            if kwargs:
                return '<{tag} {attrs}>{val}</{tag}>'.format(val=func(wrap_this), tag=tag, attrs=__build_attrs(kwargs))
            return '<{tag}>{val}</{tag}>'.format(tag=tag, val=func(wrap_this))
        return wrapper
    return decorator
