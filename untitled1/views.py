from django.shortcuts import render, redirect

from untitled1.forms import YourNumber
from untitled1.models import Prime




def home(request):
    if request.method == 'POST':
        form = YourNumber(request.POST)
        if form.is_valid():
            numbers = Prime('numbers')
        return render(request, 'numbers.html', {'numbers':numbers.primes})

    return render(request, 'numbers.html')
