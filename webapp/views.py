from rest_framework.response import Response
from rest_framework.views import APIView
from . models import employees
from . serializers import employeesSerializers
class employeeList(APIView):
    def get(self, request):
        employee1 = employees.objects.all()
        serializer = employeesSerializers(employee1, many = True)
        return Response(serializer.data)

    def post(self):
        pass



