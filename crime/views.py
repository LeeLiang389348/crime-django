from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import crime
from django.core.paginator import Paginator
from .forms import VisitorForm
import smtplib
def contact_view(request):
    form = VisitorForm(request.POST)
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            #Save the form data to the database (optional)
            form.save()
    

            
            # Send an email with the form details
            subject = 'Contact Us Form Submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]  # Replace with your email address
            def send_email(subject, message, from_email, recipient_list):
                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = from_email
                msg['To'] = recipient_list
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                    smtp_server.login(sender, password)
                    smtp_server.sendmail(sender, recipients, msg.as_string())
                print("Message sent!")

            send_mail(subject, message, from_email, recipient_list)

           
            return render(request, 'contact.html')  
        form = VisitorForm()

    return render(request, 'crime/contact.html', {'form': form})


def list_crimes(request):
	crime_list = crime.objects.all()

	p = Paginator(crime.objects.all().order_by("year"), 20)
	page = request.GET.get('page')
	crimes = p.get_page(page)
	nums = "a" * crimes.paginator.num_pages
	return render(request, 'crime/show_crime.html', 
		{'crime_list': crime_list,
		'crimes': crimes,
		'nums':nums}
		)
