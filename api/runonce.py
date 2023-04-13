from .serializers import EmployeeSerializer
from .models import Employee

empp = Employee.objects.create(
    id=1,
    name="No current User",
    employee_id=1,
    email_id="NO EMAIL",
)
empp.save()
print("empp", empp)
