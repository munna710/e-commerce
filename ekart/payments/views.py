from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        payment = Order.objects.get(razorpay_order_id=razorpay_order_id)
        payment.razorpay_payment_id = razorpay_payment_id
        payment.razorpay_signature = razorpay_signature

        # Verify payment signature
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            razorpay_client.utility.verify_payment_signature(params_dict)
            payment.status = 1  # Payment completed
            payment.save()
            return redirect('payment_success')
        except razorpay.errors.SignatureVerificationError:
            payment.status = 2  # Payment failed
            payment.save()
            return redirect('payment_failed')
    return redirect('cart')

def payment_success(request):
    return render(request, 'success.html')

def payment_failed(request):
    return render(request, 'failed.html')