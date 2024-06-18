from django.shortcuts import render
from django.db import connection
from .models import PhoneNumber
from .forms import PhoneNumberForm


def number_finder(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['phone_number']
            prefix = number[1:4]
            code = number[4:]

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT region, operator
                    FROM phone_number
                    WHERE prefix = %s AND %s BETWEEN "from" AND "to"
                    """, [prefix, code])
                result = cursor.fetchone()

            if result:
                region, operator = result

                if not PhoneNumber.objects.filter(number=number).exists():
                    PhoneNumber.objects.create(number=number, region=region, operator=operator)

                info = PhoneNumber.objects.get(number=number)
                context = {
                    'phone_number': number,
                    'operator': info.operator,
                    'region': info.region
                }
                return render(request, 'result.html', context)
            else:
                error_message = 'Информация по данному номеру телефона не найдена!'
                return render(request, 'result.html', {'error_message': error_message})

    else:
        form = PhoneNumberForm()
    return render(request, 'form.html', {'form': form})


