from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, # 执行该操作的用户。
                             related_name='actions',
                             db_index=True)
    verb = models.CharField(max_length=255)  # 这是用户执行操作的动作描述。
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE,  # 一个ForeignKey字段指向ContentType模型（model）。
                                  blank=True,
                                  null=True,
                                  related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True,  # 一个PositiveIntegerField用来存储被关联对象的primary key。
                                            blank=True,
                                            db_index=True)
    # 一个GenericForeignKey字段指向被关联的对象基于前面两个字段的组合之上。
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True,  # 这个时间日期会在动作执行的时候创建
                                   db_index=True)

    class Meta:
        ordering = ('-created',)


# Django包含了一个内容类型框架位于django.contrib.contenttypes。这个应用可以跟踪你的项目中所有的模型（models）以及提供一个通用接口来与你的模型（models）进行交互。
# contenttypes应用包含一个ContentType模型（model）
# app_label：模型（model）属于的应用名，它会自动从模型（model）Meta选项中的app_label属性获取到。举个例子：我们的Image模型（model）属于images应用
# model：模型（model）类的名字
# name：模型的可读名，它会自动从模型（model）Meta选项中的verbose_name获取到。
