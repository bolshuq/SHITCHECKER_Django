from django.shortcuts import render
from .models import *
from .forms import MyCard
import pycard

# Create your views here.
def checkmyvisa(request,pk):
    visa = card_data.objects.get(id=pk)
    Number = visa.number
    Month = visa.month
    Year = visa.year
    Cvc = visa.cvc
    card_valid = "This Card is not Valid"

    Check_status = pycard.Card(Number,Month,Year,Cvc)
    brand = Check_status.friendly_brand
    if Check_status.is_valid == True:
        card_valid = "This Card is Valid"
    context={'visa':visa,'card_valid':card_valid,'brand':brand}
    return render(request,'mycard.html',context)
def add_card(request):
    cards = card_data.objects.all()
    form = MyCard()
    if request.method == "POST":
        form = MyCard(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form,'cards':cards}
    return render(request,'index.html',context)
