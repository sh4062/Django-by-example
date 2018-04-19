from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action


# 我们给image_create视图添加了一个login_required装饰器，来阻止未认证的用户的连接。这段代码完成下面的工作：

# 我们先从 GET 中获取初始数据来创建一个表单实例。这个数据由来自外部网站图片的url和title属性构成，并且将由我们等会儿要创建的 JavaScript 工具提供。现在我们只是假设这里有初始数据。
# 如果表单被提交我们将检查它是否合法。如果这个表单是合法的，我们将新建一个Image实例，但是我们通过传递commit=False来保证这个对象将不会保存到数据库中。
# 我们将绑定当前用户（user）到一个新的iamge对象。这样我们就可以知道是谁上传了每一张图片。
# 我们把 image 对象保存到了数据库中
#####最后，我们使用 Django 的信息框架创建了一条上传成功的消息然后重定向用户到新图像的规范 URL 。我们没有在 Image 模型中实现get_absolute_url()方法，我们等会儿将编写它。#


@login_required
def image_create(request):
    """
    View for creating an Image using the JavaScript Bookmarklet.
    """
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data['tags']
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = request.user

            new_item.save()
            for x in cd:
                new_item.tags.add(x)
            new_item.save()
            create_action(request.user, 'bookmarked image', new_item)

            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images',
                                                        'form': form})


from django.shortcuts import get_object_or_404



def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.user_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 12)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'section': 'images', 'images': images})
    return render(request,
                  'images/image/list.html',
                  {'section': 'images', 'images': images})
