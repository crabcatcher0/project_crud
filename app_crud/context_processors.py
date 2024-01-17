
from .models import ContactNumber, AdmissionNumber

def contact_numbers(request):
    contact_numbers = ContactNumber.objects.values_list('phone_number', flat=True)
    admission_numbers = AdmissionNumber.objects.values_list('admission_number', flat=True)

    context={
        'contact_numbers': contact_numbers,
        'admission_numbers': admission_numbers
    }
    return (context)
