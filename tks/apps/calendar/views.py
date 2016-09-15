from django.views import generic
from django.shortcuts import render
from .models import task as Task


class CalendarMixin(object):
    def get_queryset(self):
        return Task.objects.all()


class CalendarListView(CalendarMixin, generic.ListView):
    paginate_by = 10
    template_name= 'calendar/task_list.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarListView, self).get_context_data(**kwargs)
        context['tasks'] = self.get_queryset()

        return context


class CalendarTaskView(generic.DetailView):
    model = Task
    template_name = 'calendar/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarTaskView, self).get_context_data(**kwargs)

        return context
