from django.shortcuts import render
from .models import Roll  # Import the Roll model
# Create your views here.
def rolls(request):
    rolls = Roll.objects.all()  # Fetch all Roll objects from the database
    return render(request, 'rolls/rolls.html', {'rolls': rolls} )