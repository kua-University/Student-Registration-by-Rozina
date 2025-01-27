from django.shortcuts import render
def payment(request):
    amount = 2100
    ctx = { 'amount': amount}
    return render(request, "payment/chapa.html", ctx)

def next(request):
    return render(request, "payment/next.html")