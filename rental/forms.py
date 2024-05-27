from django import forms
from django.db import models

from .models import CustomUser,Mijozlar,Qurilmalar,Prokat,Qaytarish, Tamirlash

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль'
        }
class MijozForm(forms.ModelForm):
    ERKAK = 'ERKAK'
    AYOL = 'AYOL'
    JINSI_CHOICES = [
        (ERKAK, 'Мужской'),
        (AYOL, 'Женский'),
    ]
    
    jinsi = forms.ChoiceField(
        choices=JINSI_CHOICES,
        widget=forms.RadioSelect,
        label='Полъ'
    )
    class Meta:
        model=Mijozlar
        fields=['ism','familiya','username','telefon','jinsi','pasport','jshshir']
        labels = {
            'ism':'Имя',
            'familiya':'Фамилия',
            'username': 'Имя пользователя',
            'telefon':'Номер телефона',
            'pasport':'Серия и номер паспорта',
            'jshshir':'Джшшир'
        }
class QurilmaForm(forms.ModelForm):
    class Meta:
        model=Qurilmalar
        fields=['tur','nomi','tasnif','rasmi','holati']
        labels={
            'tur':'Тип',
            'nomi':'Название',
            'tasnif':'Классификация',
            'rasmi':'Картина',
            'holati':'Положение'
        }
        
class ProkotForm(forms.ModelForm):
    class Meta:
        model=Prokat
        fields=['mijoz','qurilma','ishchi','berilgan_sanasi','qaytish_sanasi','kunlar_soni','umumiy_narx','montaj','xizmat_narxi','avans','miqdori','kunlik_narxi']
class QaytarishForm(forms.ModelForm):
    class Meta:
        model=Qaytarish
        fields=['qaytarilgan_sana','miqdori','nosozlik','summa','prokat']
        
        


class IshchiForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['ism','familiya','lavozimi','username','password','is_staff','is_active']
        labels = {
            'ism': 'Имя',
            'familiya': 'Фамилия',
            'lavozimi':'позиция',
            'username': 'Имя пользователя',
            'password':'Пароль',
            'is_staff': 'персонал',
            'is_active': 'активный ',

        }

class TamirlashForm(forms.ModelForm):
    class Meta:
        model = Tamirlash
        fields = ['qurilma','user']
        labels = {
            'qurilma':'Оборудования',
            'user':'мастер'
        }
