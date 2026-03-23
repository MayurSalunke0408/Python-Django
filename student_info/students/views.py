from django.shortcuts import render, redirect
from .forms import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_success')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_success(request):
    return render(request, 'students/student_success.html')