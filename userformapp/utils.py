from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_view(email):
    subject = 'Booking Successful'
    message = 'Your booking has been successfull and your bill invoice details as below.'
    from_email = 'hariharansha9854@gmail.com'
    recipient_list = [email]

    # render html email from template

    html_message = render_to_string('bill_email_template.html')

    # create plain text version by stripping html tags

    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        return HttpResponse('Email send successfully')
    except Exception as e:
        return HttpResponse(f'Error sending email L {str(e)}')