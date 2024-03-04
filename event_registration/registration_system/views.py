from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RegistrationForm
from .models import Registration

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Perform server-side validation
            phone_number = form.cleaned_data['phone_number']
            if not phone_number.isdigit():
                form.add_error('phone_number', 'Phone number should only contain digits.')
                return render(request, 'registration_form.html', {'form': form})

            # Check if the email is a Gmail address
            email = form.cleaned_data['email']
            if not email.endswith('@gmail.com'):
                form.add_error('email', 'Please enter a Gmail address.')
                return render(request, 'registration_form.html', {'form': form})

            # Save the form data to the database
            registration = form.save()
            return redirect('confirmation', registration_id=registration.id)
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

def confirmation_view(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'confirmation.html', {'registration': registration})