from django import forms


from .models import Resturent

class GrabModelForm(forms.ModelForm):
    class Meta:
        model = Resturent
        fields = [
            "user",
            "content" 
        ]
        #exclude = ['user']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "abc":
            raise forms.ValidationError("Cannot be ABC")
        return content