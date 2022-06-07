from django.shortcuts import render

# Create your views here.
def watch(request, *args, **kwargs):
    return render(request, "watch.html", {})