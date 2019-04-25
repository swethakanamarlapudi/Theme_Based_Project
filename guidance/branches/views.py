from django.shortcuts import render,get_object_or_404
from .models import Departments,companies



def index(request):
  all_departments = Departments.objects.all()
  return render(request, 'branches/index.html', {'all_departments':all_departments})

def detail(request, departments_id):
 departments = get_object_or_404(Departments, pk=departments_id)
 return render(request, 'branches/detail.html', {'departments':departments})


def favorite(request, departments_id):
  departments = get_object_or_404(Departments, pk=departments_id)
  try:
	   selected_companies = departments.companies_set.get(pk=request.POST['companies'])
  except (KeyError, companies.DoesNotExist):
	    return render(request, 'branches/detail.html' , {
		       'departments':departments,
		       'error_message': "you did not select a valid song",
			   'companies':companies,
		})
  else:
   selected_companies.is_favorite = True
   selected_companies.save()
   return render(request, 'branches/detail.html', {'departments':departments})

