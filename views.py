from django.shortcuts import render
from django.views.generic import TemplateView
from models import Product
from models import Category


class HomePageView(TemplateView):

    def get(self, request, **kwargs):
    	products = Product.objects.all()
    	categories = Category.objects.all()
        return render(request, 'index.html', context={'products': products, 'categories': categories})


def Details(request, product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'details.html', context={'product': product})

def About(request):	
	product = Product.objects.all()
	return render(request, 'details.html', context={'product': product})

def Checkout(request):
	if request.method == 'POST':
		firstname = request.POST.firstname
		lastname = request.POST.lastname
	return render(request, 'checkout.html')

def add_product(request):
	if request.method == 'POST':
		product_vars = {}
		for field in request.POST:
			if field != 'csrfmiddlewaretoken':
				product_vars[field] = request.POST[field]
		product_vars['category_id'] = 1
		new_product = Product(**product_vars)
		new_product.save()
	return render(request, 'addproduct.html')


	


	
