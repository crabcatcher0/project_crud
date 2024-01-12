from .models import ContactNumber

def contact_numbers(request):
    contact_numbers = ContactNumber.objects.values_list('phone_number', flat=True)
    return {'contact_numbers': contact_numbers}
