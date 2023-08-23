from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index-2.html')

def CreateTicket(request):
    return render(request, 'create-ticket.html')


def AllTicket(request):
    return render(request, 'all-ticket.html')

def Dashcards(request):
    return render(request, 'dashcards.html')

