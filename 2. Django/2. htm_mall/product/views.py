from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from order.forms import RegisterForm as OrderForm
from htmuser.decorators import login_required, admin_required
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins
from .serializers import ProductSerializer
# Create your views here.


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, * args, **kwargs)

    def get_queryset(self):
        return Product.objects.all().order_by('id')


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, * args, **kwargs)

    def get_queryset(self):
        return Product.objects.all().order_by('id')


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
