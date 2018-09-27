from django.shortcuts import render,get_object_or_404
from .models import Resturent
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from .mixins import FormUserNeededMixin
# Create your views here.





class GrabnGoDetailView(DetailView):
    queryset = Resturent.objects.all()



class GrabnGoListView(ListView):
    def get_queryset(self, *args, **kwargs):
        qs = Resturent.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query) |
                    Q(location__icontains=query)
                    )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(GrabnGoListView, self).get_context_data(*args, **kwargs)
        return context


def grabngo_detail_view(request, pk=None): # pk == id
    obj = get_object_or_404(Resturent, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "grabbngoapp/detail_view.html", context)



