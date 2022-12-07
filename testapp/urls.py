from django.urls import path
from .views import CartItemViews
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register()


urlpatterns = [
    path('cart-items/', CartItemViews.as_view())
    path('cart-items/<int:id>', CartItemViews.as_view())

]