from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class Home(TemplateView):
    template_name = 'mamazon/home.html'

class ProductListView(ListView):
    model = Product
    template_name = 'mamazon/list.html'

    #検索窓の実装
    def get_queryset(self):
        queryset = Product.objects.all()#全ての商品情報を取得
        if 'query' in self.request.GET:#検索されたとき
            qs = self.request.GET['query']#検索された情報を格納
            queryset = queryset.filter(name__contains=qs)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'mamazon/detail.html'