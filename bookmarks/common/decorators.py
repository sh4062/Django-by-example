from django.http import HttpResponseBadRequest
#它定义一个当请求不是 AJAX 时返回HttpResponseBadRequest（HTTP 400）对象的wrap 函数，否则它将返回一个被装饰了的对象。

def ajax_required(f):
    def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseBadRequest()
            return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap