from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RegistrationForm
from .models import Registration
from django.conf import settings
from django.core.mail import send_mail

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
              
            subject = 'Welcome to the Grand Event!'
            message = f'Hi {registration.full_name},\n\nThank you for registering for the Grand Event.\n\nWe look forward to seeing you there!\n\nBest regards,\nThe Event Team'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [registration.email]  # Use the email from the registration
            send_mail(subject, message, email_from, recipient_list)
            return redirect('confirmation', registration_id=registration.id)
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

def confirmation_view(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'confirmation.html', {'registration': registration})
