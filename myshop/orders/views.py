from django.shortcuts import render

# Create your views here.
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
#GET 请求：实例化 OrderCreateForm 表单然后渲染模板 orders/order/create.html
#POST 请求：验证提交的数据。如果数据是合法的，我们将使用 order = form.save() 来创建一个新的 Order 实例。
# 然后我们将会把它保存进数据库中，之后再把它保存进 order 变量里。在创建 order 之后，
# 我们将迭代无购车的物品然后为每个物品创建 OrderItem。最后，我们清空购物车。


def order_create(request):
    cart = Cart(request)
    if(request.method == 'POST'):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order}
                          )
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart,
                   'form': form})
