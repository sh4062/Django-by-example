from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length= 200,db_index=True,unique = True)

    class Meta:
        #b_table = ''
        #managed = True
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='produtcs',on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length= 200,db_index=True,unique = True)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d',default = 'default2.jpg')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)#这个字段使用 Python 的 decimal.Decimal 元类来保存一个固定精度的十进制数。max_digits 属性可用于设定数字的最大值， decimal_places 属性用于设置小数位数。
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id,self.slug])



    
