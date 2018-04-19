from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.

from sorl.thumbnail import ImageField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='default.jpg')


from django.contrib.auth.models import User


class Contact(models.Model):#创建一个中介模型（intermediate model）用来在用户之间构建关系 beacuse 1.避免修改user 2.存储关系建立的时间
    user_from = models.ForeignKey(User,on_delete = models.CASCADE, #创建关系的用户
                                  related_name='rel_from_set')
    user_to = models.ForeignKey(User,on_delete = models.CASCADE,# 被关注的用户
                                related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True,  #创建时的时间
                                   db_index=True)

    class Meta: #元类就是创建类的类
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from,
                                      self.user_to)
                                
# Add following field to User dynamically monkey-patch
User.add_to_class('following',
                   models.ManyToManyField('self',
                                          through=Contact,
                                          related_name='followers',
                                          symmetrical=False))#不自动回关注
                        
