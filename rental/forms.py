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
        fields=['tur','nomi','tasnif','rasmi','holati','narxi']
        labels={
            'tur':'Тип',
            'nomi':'Название',
            'tasnif':'Классификация',
            'rasmi':'Картина',
            'holati':'Положение',
            'narxi':'Цена'
        }
        
class ProkotForm(forms.ModelForm):
    class Meta:
        model = Prokat
        fields = ['mijoz', 'qurilma','miqdori', 'ishchi', 'berilgan_sanasi', 'qaytish_sanasi', 'kunlar_soni',  'montaj', 'xizmat_narxi', 'avans',  'kunlik_narxi','umumiy_narx']
        labels = {
            'mijoz': 'Клиент',
            'qurilma': 'Устройство',
            'ishchi': 'Работник',
            'berilgan_sanasi': 'Дата выдачи',
            'qaytish_sanasi': 'Дата возврата',
            'kunlar_soni': 'Количество дней',
            'umumiy_narx': 'Общая цена',
            'montaj': 'Монтаж',
            'xizmat_narxi': 'Цена услуги',
            'avans': 'Залок',
            'miqdori': 'Количество',
            'kunlik_narxi': 'Ежедневная цена',
        }

class QaytarishForm(forms.ModelForm):
    class Meta:
        model = Qaytarish
        fields = ['qaytarilgan_sana', 'miqdori', 'nosozlik', 'summa', 'prokat']
        labels = {
            'qaytarilgan_sana': 'Дата возврата',
            'miqdori': 'Количество',
            'nosozlik': 'Дефект',
            'summa': 'Цена',
            'prokat': 'Прокат',
        }
        
        


class IshchiForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['ism','familiya','lavozimi','username','password','is_staff','is_active']
        labels = {
            'ism': 'Имя',
            'familiya': 'Фамилия',
            'lavozimi':'Должност',
            'username': 'Имя пользователя',
            'password':'Пароль',
            'is_staff': 'Персонал',
            'is_active': 'Активный ',

        }

class TamirlashForm(forms.ModelForm):
    class Meta:
        model = Tamirlash
        fields = ['qurilma','user','sana']
        labels = {
            'qurilma':'Оборудования',
            'user':'Мастер',
            'sana':'Дата'
        }
