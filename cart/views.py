from .models import Cart
from django.views.generic import DetailView

# Create your views here.
class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart/shooping_cart.html'