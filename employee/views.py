from django.http import JsonResponse
from django.shortcuts import render
import json
from .serializers import EmployeeSerializers
from django.views.decorators.csrf import csrf_exempt

from . models import Employee
# Create your views here.

@csrf_exempt
def create(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    first_name = body.get("first_name")
    last_name = body.get("last_name")
    email = body.get("email")
    age = body.get("age")
    department = body.get("department")
    new_employee = Employee(first_name=first_name,last_name=last_name,email=email,age=age,department=department)
    new_employee.save()
    return JsonResponse({"success":"Employee details saved"})


def get(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializers(employees,many=True)
    return JsonResponse({'employee':serializer.data},safe=False)