from django.shortcuts import render
from .forms import ContactFormForm
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        contact_form = ContactFormForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Contact request received! We are quite busy but we aim to reply within 2 working days.")
            storage = messages.get_messages(request)
            storage.used = True
    else:
        contact_form = ContactFormForm()
    return render(request, 'contact/contact.html', {'form': contact_form})
