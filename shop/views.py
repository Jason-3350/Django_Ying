from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from shop.models import Goods


class Basket:

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity


# convenience method as used in several methods
def get_basket(request):
    basket = request.session.get('basket', [])
    print('get_basket is %s' % basket)
    print(type(basket))
    products = []
    for item in basket:
        product = Goods.objects.get(id=item[0])
        # create a new object of the class basket
        basket = Basket(item[0], product.g_name, product.g_price, item[1])
        # products include all those basket
        products.append(basket)
    return products


def basket(request):
    products = get_basket(request)
    return render(request, 'shop/basket.html', {'products': products})


#
# def product_list(request):
#     products = Goods.objects.all()
#     return render(request, 'shop/product_list.html', context={'products': products})

def product_list(request):
    products = Goods.objects.all()
    basket = request.session.get('basket', [])  # if dont have session of basket then make a new list
    request.session['basket'] = basket
    print('product_list basket is %s' % basket)
    print(type(basket))
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Goods, id=id)
    return render(request, 'shop/product_detail.html', context={'product': product})


def product_buy(request):
    if request.method == "POST":
        temp_id = int(request.POST.get('id', ''))
        quantity = int(request.POST.get('quantity', ''))
        basket = request.session['basket']  # *******************************
        print('product_buy basket is %s' % basket)
        basket.append([temp_id, quantity])
        request.session['basket'] = basket
    return redirect('product_list')


def purchase(request):
    if request.user.is_authenticated:
        user = request.user
        products = get_basket(request)
        total = 0
        for product in products:
            total += product.price * product.quantity
        return render(request, 'shop/purchase.html', {'products': products, 'user': user, 'total': total})
    else:
        return redirect('login')


# save order, clear basket and thank customer
def payment(request):
    products = get_basket(request)
    user = request.user
    order = Order.objects.create(customer=user.customer)
    order.refresh_from_db()
    for product in products:
        product_item = get_object_or_404(Product, id=product.id)
        cart = Cart.objects.create(product=product_item, quantity=product.quantity)
        cart.refresh_from_db()
        line_iten = LineItem.objects.create(quantity=product.quantity, product=product_item,
                                            cart=cart, order=order)

    request.session['basket'].clear()
    request.session['deleted'] = 'thanks for your purchase'
    return redirect('product_list')

# def payment(request):
#     products = get_basket(request)
#     user = request.user
#     order = Order.objects.create(customer=user.customer)
#     order.refresh_from_db()
#     for product in products:
#         product_item = get_object_or_404(Product, id=product.id)
#         cart = Cart.objects.create(product=product_item, quantity=product.quantity)
#         cart.refresh_from_db()
#         line_iten = LineItem.objects.create(quantity=product.quantity, product=product_item,
#                                             cart=cart, order=order)
#
#     request.session['basket'].clear()
#     request.session['deleted'] = 'thanks for your purchase'
#     return redirect('product_list')
