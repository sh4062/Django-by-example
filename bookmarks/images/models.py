from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.
from django.conf import settings
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,#标记了这张图片 User 对象。这是一个 ForeignKey字段
    related_name='images_created')
    title = models.CharField(max_length=200)#图片的标题
    slug = models.SlugField(max_length=200,blank=True)#一个只包含字母、数字、下划线、和连字符的标签， 用于创建优美的 搜索引擎友好（SEO-friendly）的 URL
    url = models.URLField()#这张图片的源 URL
    image = models.ImageField(upload_to='images/%Y/%m/%d')#图片文件
    description = models.TextField(blank=True)#一个可选的图片描述字段
    tags = TaggableManager()
    created = models.DateField(auto_now_add=True,#用于表明一个对象在数据库中创建时的时间和日期。
                               db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,#建立多对多关系 我们将要在 Image 模型中再添加一个字段来保存喜欢这张图片的用户。
                                   related_name='images_liked',
                                   blank=True)#Django 会用两张表主键（primary key）创建一个中介联接表（译者注：就是新建一张普通的表，只是这张表的内容是由多对多关系双方的主键构成的）
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)#我们使用了 Django 提供的slugify()函数在没有提供slug字段时根据给定的图片标题自动生slug,然后，我们保存了这个对象。我们自动生成slug，
            super(Image, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('images:detail',args=(self.id,self.slug))