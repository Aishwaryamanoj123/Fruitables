from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login, authenticate
from .models import UsercreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User






# Create your views here.

def home(request):

    return HttpResponse('welcome')

def page(request):
    return render(request, "404.html")

def cart(request):
    return render(request, "cart.html")



def index(request):
    
    category = categories.objects.all()
    
    categoryID = request.GET.get('category')
    if categoryID:
        product = prdct.objects.filter(category_id=categoryID)  # Filter products based on the category_id field
    else:
        product = prdct.objects.all()

    context = {
         'category': category,
         'product': product
    }
    return render(request, "index.html",context)




def chackout(request):
    if request.method=='POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        print(address,phone,pincode,cart,user)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b
            print(i)
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total
            )
            order.save()
            request.session['cart'] = {}
    return redirect("index")


def contact_page(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        contact.save()

    return render(request, "contact.html")



def shop_detail(request,id):
     product = prdct.objects.filter(id=id).first()
     context = {
         'product':product
     }
     
     return render(request, "shop-detail.html",context)

def shop(request):
    category = categories.objects.all()
    
    categoryID = request.GET.get('category')
    if categoryID:
        product = prdct.objects.filter(category_id=categoryID)  # Filter products based on the category_id field
    else:
        product = prdct.objects.all()

    context = {
         'category': category,
         'product': product
    }
    return render(request, "shop.html", context)


def testimonial(request):
     return render(request, "testimonial.html")



# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UsercreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('login')
    else:
        form = UsercreateForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'signup.html', context)

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
            else:
                error_message = 'Invalid username or password'
        else:
            error_message = 'Invalid form submission'
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form, 'error_message': error_message})






@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = prdct.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = prdct.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = prdct.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = prdct.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart.html')


def orderpage(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user)
    contex = {
        'order':order
    }
    return render(request, 'order.html',contex)

def product_page(request):
    category = categories.objects.all()
    
    categoryID = request.GET.get('category')
    if categoryID:
        product = prdct.objects.filter(category_id=categoryID)  # Filter products based on the category_id field
    else:
        product = prdct.objects.all()

    context = {
         'category': category,
         'product': product
    }
    return render(request, "product.html",context)


def search(request):
    query = request.GET.get('query', '')  # Get the 'query' parameter from GET request with default value ''
    if query:
        product = prdct.objects.filter(name__icontains=query)
    else:
        product = prdct.objects.all()
    context = {'product': product}
    return render(request, "search.html", context)




