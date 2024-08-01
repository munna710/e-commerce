from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def show_cart(request):
    user=request.user
    customer=user.customer_profile
    print("user",user)
    print("customer",customer)
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}

    return render(request,'cart.html',context)


def remove_item_from_cart(request,pk):

    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')


def checkout_cart(request):
    
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            print(total)
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                # Create Razorpay order
                amount = int(total * 100)  # Convert to paisa
                razorpay_order = razorpay_client.order.create(dict(amount=amount, currency='INR', payment_capture='1'))
                razorpay_order_id = razorpay_order['id']

                # Save order details
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.razorpay_order_id = razorpay_order_id
                order_obj.save()

                context = {
                    'order': order_obj,
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
                    'amount': amount,
                    'currency': 'INR'
                }
                return render(request, 'create_payment.html', context)
            else:
                status_message = "Unable to process. No items in cart"
                messages.error(request, status_message)
        except Exception as e:
            status_message = "Unable to process. No items in cart"
            messages.error(request, status_message)
    return redirect('cart')

@login_required(login_url='account')        
def show_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request,'orders.html',context)



@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        print(user)
        customer=user.customer_profile
        print(customer)
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')