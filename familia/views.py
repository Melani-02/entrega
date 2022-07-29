from django.shortcuts import render

# Create your views here.
from familia.models import Family

# Create your views here.
def add_relative(request):
    #new_relative = Family.objects.create(full_name='Ariana Puello', age=17, genre='F', relative='Cousin')
    new_relative = Family.objects.create(full_name='Ricardo Macias', age=60, genre='M', relative='Father')
    context={
        'new_relative':new_relative
    }
    return render(request,'ingresarfamilia.html', context=context)

def list_family(request):
    family = Family.objects.all()
    context= {
        'family':family,
        'listVoid':len(family)==0
    }
    return render(request, 'listafamilia.html', context=context)