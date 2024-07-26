from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html' )
def list_products(request):
    """_summary_
    returns prouduct list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    return render(request,'products.html')

def detail_product(request,pk):
    return render(request,'product_detail.html')