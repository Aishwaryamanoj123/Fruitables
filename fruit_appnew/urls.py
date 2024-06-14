from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', views.home, name = 'home'),
    path('cart/', views.cart, name='cart'),
    path('chackout/', views.chackout, name='chackout'),
    path('contact/',views.contact_page, name='contact'),
    path('',views.index, name= 'index'),
    path('shop/', views.shop, name='shop'),
    path('test/',views.testimonial,name= 'test'),
    path('page/',views.page, name='page'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_view, name='login'),

   path("reset_password/", auth_views.PasswordResetView.as_view(), name='reset_password'),
   path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),




    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    path('order/', views.orderpage, name='order'),
    path('product/', views.product_page, name = 'product'),
    path('product/<str:id>',views.shop_detail, name='shopdetail'),

    path('search/', views.search, name='search')
] 