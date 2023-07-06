from django.urls import  path
from product_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('receipt/', views.receipt, name = "receipt"),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('login', views.connex, name='logine'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('register', views.sing_up, name='sing_up'), 
    path('modifier/<int:pk>/',views.Modification_Donnees.as_view(), name ='modifier'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name='logout'), 
    path('home/<int:product_id>/', views.product_detail, name='product_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),   
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('all_sales/', views.all_sales, name = 'all_sales'),
    path('produit/<int:produit_id>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
]


