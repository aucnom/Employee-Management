from django.shortcuts import redirect, render
from .models import Job, Employee
from .forms import JobForm, EmployeeForm

def home(request):
    employees = Employee.objects.all()
    jobs = Job.objects.all()
    context = {'employees': employees, 'jobs': jobs}
    return render(request, "base/index.html", context=context)

def createJob(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            form = JobForm()

    context = {'form': form}
    return render(request, 'base/job_form.html', context=context)

def createEmployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()

    context = {'form': form}
    return render(request, 'base/employee_form.html', context=context)

def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'base/delete_employee.html', {'obj': employee})

def updateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/employee_form.html', context=context)

def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('home')
    return render(request, 'base/delete_employee.html', {'obj': job})

def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/job_form.html', context=context)