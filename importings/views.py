from django.shortcuts import render

# Create your views here.
def Home(request):
    #shirts = get_object_or_404(shirts,pk=shirts_id)
    shirtss = "new"
    return render(request, 'home.html', {'shirts': shirtss})