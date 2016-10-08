from django.views import generic
from django.shortcuts import render
from models import gallery as Gallery


class GalleryMixin(object):
    def get_queryset(self):
        return Gallery.objects.all()


class GalleryListView(GalleryMixin, generic.ListView):
    paginate_by = 10
    template_name = 'gallery/list.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['photos'] = self.get_queryset()

        return context


class GalleryView(generic.DetailView):
    model = Gallery
