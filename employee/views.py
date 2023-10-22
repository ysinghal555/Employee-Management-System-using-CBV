from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView

from .forms import EmployeeForm
from .models import Employee


# This function will add new employee and show employees
class EmployeeAddShowView(TemplateView):
    template_name = 'employee/addandshow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = EmployeeForm()
        emp = Employee.objects.all()
        context = {'form': fm, 'emp': emp}
        return context

    def post(self, request):
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            salary = fm.cleaned_data['salary']
            department = fm.cleaned_data['department']
            role = fm.cleaned_data['role']
            phone_number = fm.cleaned_data['phone_number']
            reg = Employee(name=name, email=email, salary=salary, department=department, role=role,
                           phone_number=phone_number)
            reg.save()
        return HttpResponseRedirect('/')


# this function will delete the employee
class EmployeeDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Employee.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


# this function will update and edit
class EmployeeUpdateView(View):
    def get(self, request, id):
        emp = Employee.objects.get(pk=id)
        fm = EmployeeForm(instance=emp)
        return render(request, 'employee/updateemployee.html', {'form': fm})

    def post(self, request, id):
        emp = Employee.objects.get(pk=id)
        fm = EmployeeForm(request.POST, instance=emp)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

# def add_show(request):
#     if request.method == 'POST':
#         fm = EmployeeForm(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             salary = fm.cleaned_data['salary']
#             department = fm.cleaned_data['department']
#             role = fm.cleaned_data['role']
#             phone_number = fm.cleaned_data['phone_number']
#             reg = Employee(name=name, email=email, salary=salary, department=department, role=role,
#                            phone_number=phone_number)
#             reg.save()
#             # fm.save()
#
#         # Generally we render the success message page here, but for now we are returning the new form only
#         fm = EmployeeForm()
#     else:
#         fm = EmployeeForm()
#
#     emp = Employee.objects.all().order_by('id')
#     paginator = Paginator(emp, 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'employee/addandshow.html', {'form': fm, 'emp': page_obj})


# def update_emp(request, id):
#     if request.method == "POST":
#         emp = Employee.objects.get(pk=id)
#         fm = EmployeeForm(request.POST, instance=emp)
#         if fm.is_valid():
#             fm.save()
#         return HttpResponseRedirect('/')
#     else:
#         emp = Employee.objects.get(pk=id)
#         fm = EmployeeForm(instance=emp)
#
#     return render(request, 'employee/updateemployee.html', {'form': fm})


# def delete_emp(request, id):
#     if request.method == "POST":
#         deleted_emp = Employee.objects.get(pk=id)
#         deleted_emp.delete()
#
#     return HttpResponseRedirect('/')
