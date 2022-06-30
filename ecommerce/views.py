import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

from ecommerce.models import Product, User, CartItem, Category

# Create your views here.
def index(request):
    param = request.GET.get('q', '')
    category = request.GET.get('category', '')

    if param == 'watchlist':
        products = request.user.watchlist.all()
    elif category:
        products = Category.objects.get(name=category).products.all()
    else:
        products = Product.objects.all()

    return render(request, 'ecommerce/index.html', {
        'products': products
    })


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'ecommerce/product.html', {
        "product": product
    })


def cart(request):
    if request.user.is_authenticated:
        return render(request, 'ecommerce/cart.html')
    return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def add_to_cart(request, product_id):
    if request.method == 'POST':
        body = json.loads(request.body)
        quantity = body['quantity']
        product = Product.objects.get(id=product_id)
        if product and request.user.is_authenticated:
            cartItem = CartItem(product=product, quantity=quantity)
            if cartItem not in request.user.cart.all():
                cartItem.save()
                price = float(product.price) * float(quantity)

                request.user.cart.add(cartItem)
                request.user.total += price
                request.user.save()

        return HttpResponse("OK")


@csrf_exempt
def remove_from_cart(request, id):
    if request.method == 'PUT' and request.user.is_authenticated:
        cartItem = CartItem.objects.get(id=id)
        request.user.cart.remove(cartItem)
        price = float(cartItem.product.price) * float(cartItem.quantity)
        request.user.total -= price
        request.user.save()
        cartItem.remove()
        return HttpResponse("OK")


@csrf_exempt
def watchlist(request, id):
    if request.method == 'PUT':
        product = Product.objects.get(id=id)

        if product and request.user.is_authenticated:
            if product not in request.user.watchlist.all():
                request.user.watchlist.add(product)
            else:
                request.user.watchlist.remove(product)

        return HttpResponse("OK")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "registration/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "registration/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "registration/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "registration/login.html")