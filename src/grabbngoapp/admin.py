from django.contrib import admin

# Register your models here.
from .forms import GrabModelForm
from .models import Resturent


#admin.site.register(Tweet)


class GrabModelAdmin(admin.ModelAdmin):
    form = GrabModelForm
    # class Meta:
    #     model = Tweet
        


admin.site.register(Resturent, GrabModelAdmin)
