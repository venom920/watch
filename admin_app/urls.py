from django.urls import path 
from admin_app import views

urlpatterns = [
  path('category',views.category,name='category'),
  path('view_categories',views.view_categories,name='view_categories'),
  path('update_category/<int:id>',views.update_category,name='update_category'),
  path('delete_category/<int:id>',views.delete_category,name='delete_category'),



  path('items',views.items,name='items'),
  path('view_items',views.view_items,name='view_items'),


  path('main',views.main,name='main'),

  path('products',views.products,name='products'),

  path('filter_watch/<int:id>',views.filter_watch,name='filter_watch'),

  path('single_product/<int:id>',views.single_product,name='single_product'),

  path('add_cart/<int:product_id>',views.add_cart,name='add_cart'),
  path('view_cart',views.view_cart,name='view_cart'),
  path('delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
  path('confirm_checkout',views.confirm_checkout,name = 'confirm_checkout'),


  
]