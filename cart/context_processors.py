from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id= _cart_id(request))
            cart_items=CartItem.objects.all().filter(cart=cart[:1]) #CartItem query you are about to make seems to expect a single Cart object rather than a QuerySet.
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
        return dict(item_count=item_count)
