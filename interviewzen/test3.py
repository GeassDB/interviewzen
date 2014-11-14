def d2(arg1, arg2):
    def deco_wrap(fn):
        def fn_wrap(*args, **kwargs):
            print('before test {} {}'.format(arg1, arg2))
            return fn(*args, **kwargs)
        return fn_wrap
    return deco_wrap

@d2('a', 'b')
def test(arg1, arg2):
        print 'test', arg1, arg2
