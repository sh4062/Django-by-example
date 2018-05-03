from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem
#OrderItem 使用 ModelInline 来把它引用为 OrderAdmin 类的内联元素。一个内联元素允许你在同一编辑页引用模型，并且将这个模型作为父模型。
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
