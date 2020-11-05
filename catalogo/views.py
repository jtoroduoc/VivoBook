from django.contrib.admin import autodiscover
from django.shortcuts import render
from .models import Libro, Inventario, Autor
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    numero_libros = Libro.objects.all().count()
    numero_inventario = Inventario.objects.all().count()
    numero_inventario_disponible = Inventario.objects.filter(estatus__exact='d').count()
    numero_autores = Autor.objects.count() # El all() esta implicido por defecto.

    # Numero de visitas a esta view, como está contado en la variable sesión
    numero_visitas = request.session.get('numero_visitas',0)
    request.session['numero_visitas'] = numero_visitas + 1

    # Renderiza la plantilla HTML index.html con los en la variable contexto
    return render(request, 
                 'index.html', 
                 context={'numero_libros': numero_libros,
                            'numero_inventario': numero_inventario,
                            'numero_inventario_disponible': numero_inventario_disponible, 
                            'numero_autores': numero_autores,
                            'numero_visitas': numero_visitas,})

class LibroListView(generic.ListView):
    model = Libro
    paginate_by = 10   

class LibroDetailView(generic.DetailView):
    model = Libro

