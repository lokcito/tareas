from django.shortcuts import render
from listar.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.
@login_required(login_url = '/admin/login')
#modulo.can_modelo
@permission_required('listar.view_task', login_url = '/admin/')
def v_index(request):
    context = {
        'tareas': Task.objects.all()
    }
    return render(request, 'index.html', context)