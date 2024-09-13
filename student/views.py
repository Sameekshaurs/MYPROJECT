from django.shortcuts import render, redirect , get_object_or_404
from .models import Student
from .forms import StudentForm

#List students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students' : students})

#Add student
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html',{'form': form})
    
#Edit student
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
         form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})
#Delete student
def student_delete(request, pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html',{'student': student})
# Create your views here.
