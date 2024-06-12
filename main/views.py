from django.views.generic import ListView
from main.models import Todo


class HomePage(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'articles'
    queryset = Todo.objects.all()
