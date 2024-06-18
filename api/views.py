from django.shortcuts import render
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import PhoneNumber
from .serializers import PhoneNumberInfoSerializer


@api_view(['GET'])
def number_finder_api(request, phone_number):
    try:
        prefix = phone_number[1:4]
        code = phone_number[4:]

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT region, operator
                FROM phone_number
                WHERE prefix = %s AND %s BETWEEN "from" AND "to"
                """, [prefix, code])
            result = cursor.fetchone()

        if result:
            region, operator = result

            if not PhoneNumber.objects.filter(number=phone_number).exists():
                PhoneNumber.objects.create(number=phone_number, region=region, operator=operator)

            info = PhoneNumber.objects.get(number=phone_number)

            serializer = PhoneNumberInfoSerializer(info)
            return Response(serializer.data)
    except PhoneNumber.DoesNotExist:
        return Response({'error': 'Информация по данному номеру телефона не найдена!'}, status=404)
