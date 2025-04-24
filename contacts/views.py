from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    contacts = request.user.contacts.all().order_by("-created_at")
    context = {"contacts": contacts}
    return render(request, "contacts.html", context)
