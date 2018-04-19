from django import forms
from .models import Image
# 这是一个通过Image模型创建的ModelForm（模型表单），但是这个表单只包含了 title,url,description字段。
# 我们的用户不会在表单中直接为图片添加 URL。相反的，
# 他们将会使用一个 JavaScropt 工具来从其他网站中选择一张图片然后我们的表单将会以参数的形式接收这张图片的 URL。
# 我们覆写 url 字段的默认控件（widget）为一个HiddenInput控件，这个控件将会被渲染为属性是 type="hidden"的 HTML 元素。使用这个控件是因为我们不想让用户看见这个字段。
from urllib import request
import urllib
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url','tags', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }
    # 了验证提供的图片 URL 是否合法，我们将检查以.jpg或.jpeg结尾的文件名，来只允许JPG文件的上传

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not '
                                        'match valid image extensions.')
        return url
    #重载save
    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        "referer":"https://image.baidu.com"}

        image_url = self.cleaned_data['url']
        req = urllib.request.Request(url=image_url, headers=headers)
        
        # image_name = '{}.{}'.format(slugify(image.title),
        #                             image_url.rsplit('.', 1)[1].lower(),
        #                             )
        # 从给定的 URL 中下载图片
        response = request.urlopen(req)
        # image.image.save(image_name,
        #                  ContentFile(response.read()),
        #                  save=False)
        
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.rsplit('.', 1)[1].lower(),
                                    
                                    )
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
            image.save_m2m()
        return image
