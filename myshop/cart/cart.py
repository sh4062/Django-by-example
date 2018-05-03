from decimal import Decimal
from django.conf import settings
from shop.models import Product
#session购物车的增删改查
class Cart(object):
    def __init__(self,request):
        """
        Init the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # new
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product,quantity = 1,update_quantity = False):
        """
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self,product):
        """
        Remove
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def __iter__(self):
        """
        Define a iterator
        在 __iter__() 方法中，我们检索购物车中的 Product 实例来把他们添加进购物车的物品中。
        之后，我们迭代所有的购物车物品，把他们的 price 转换回十进制数，
        然后为每个添加一个 total_price 属性。现在我们就可以很容易的在购物车当中迭代物品了。
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in = product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
