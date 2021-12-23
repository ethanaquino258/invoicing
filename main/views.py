from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.


def index(request):
    print(Client.objects.all())
    return render(request, 'main/index.html', {'clients': Client.objects.all()})


def createNewClient(request):
    print('here')
    if request.method == 'POST':
        print(request.POST.get('zip'))
        print(type(int(request.POST.get('zip'))))
        client = Client(name=request.POST.get('clientName'),
                        email=request.POST.get('clientEmail'))
        print(client)
        client.save()

        address = Address(client=client, address=request.POST.get('address'), address2=request.POST.get('address2'), city=request.POST.get(
            'city'), state=request.POST.get('state'), zipcode=request.POST.get('zip'))

        print(address)
        address.save()

    else:
        return render(request, 'main/newClient.html')


def clientDetail(request, client_id):
    print(Client.objects.get(pk=client_id))
    return render(request, 'main/clientDetail.html', {'client': Client.objects.get(pk=client_id)})


def newInvoice(request, client_id):
    if request.method == 'POST':
        client = Client.objects.get(pk=client_id)
        print(request.POST)
        # r = request.POST
        # invoice = Invoice(title=r.get('title'), date=, due_date=, subtotal=, total=, amount_paid=, balance_due=, client=client)
        # invoice.save()

    else:
        return render(request, 'main/newInvoice.html', {'form': InvoiceForm})
