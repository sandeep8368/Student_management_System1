from django.shortcuts import render
from studentapp.models import studentModel
# Create your views here.
def display_view(request):
    student_data = studentModel.objects.all()
    my_dict = {
        'student':student_data
    }
    return render(request, 'html/index.html',my_dict)