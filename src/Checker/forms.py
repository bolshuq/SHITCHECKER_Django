from django.forms import ModelForm
from .models import card_data
class MyCard(ModelForm):
    class Meta:
          model = card_data
          fields = '__all__'
