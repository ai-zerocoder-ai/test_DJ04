from django import forms
from .models import Film  # Импорт модели Film из models.py

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film  # Связь формы с моделью Film
        fields = ['title', 'description', 'review']  # Поля формы
