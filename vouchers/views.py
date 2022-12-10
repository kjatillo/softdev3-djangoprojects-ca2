from django.shortcuts import redirect
from django.utils import timezone
from .forms import VoucherApplyForm
from .models import Voucher


def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code,
            valid_from__lte=now, valid_to__gte=now, active=True)
            request.session['voucher_id'] = voucher.id
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
    
    return redirect('cart:cart_detail')
