from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Track, Artist

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

class TrackListView(ListView):
    model = Track
    template_name = 'dashboard/data.html'
    context_object_name = 'track'
    ordering = ['-year', 'rank']

class TrackYearListView(ListView):
    model = Track
    template_name = 'dashboard/track_year.html'
    context_object_name = 'track'

    def get_queryset(self):
       return Track.objects.filter(year=self.kwargs.get('year')).order_by('rank')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_fields=Track._meta.get_fields()
        ignore = ['id', 'track_name', 'rank', 'year', 'spotify_id', 'artist']
        for field in all_fields:
            if field.name in ignore:
                continue
            temp = list(Track.objects.filter(year=self.kwargs.get('year')).values_list(field.name))
            context[field.name] = [item for t in temp for item in t]
            for i in range(len(context[field.name])):
                 context[field.name][i] = float(context[field.name][i])
        return context