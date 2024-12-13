from django import forms
from django.db import models

from .models import CustomUser,Mijozlar,Qurilmalar,Prokat,Qaytarish, Tamirlash

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['ism', 'familiya', 'username', 'rasm']

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
        (ERKAK, 'ERKAK'),
        (AYOL, 'AYOL'),
    ]
    
    jinsi = forms.ChoiceField(
        choices=JINSI_CHOICES,
        widget=forms.RadioSelect,
        label='JINS'
    )
    class Meta:
        model=Mijozlar
        fields=['ism','familiya','username','telefon','jinsi','pasport','jshshir']
        labels = {
            'ism':'ISM',
            'familiya':'FAMILIYA',
            'username': 'FOYDALANUVCHI NOMI',
            'telefon':'TELEFON RAQAM',
            'pasport':'PASSPORT SERIYA VA RAQAM',
            'jshshir':'JSHSHIR'
        }
class QurilmaForm(forms.ModelForm):
    class Meta:
        model=Qurilmalar
        fields=['tur','nomi','tasnif','rasmi','holati','narxi']
        labels={
            'tur':'TUR',
            'nomi':'NOMI',
            'tasnif':'TASNIFI',
            'rasmi':'RASM',
            'holati':'HOLATI',
            'narxi':'NARX'
        }
        
class ProkotForm(forms.ModelForm):
    class Meta:
        model = Prokat
        fields = ['mijoz', 'qurilma', 'miqdori', 'ishchi', 'berilgan_sanasi', 'qaytish_sanasi', 'kunlar_soni', 'montaj', 'xizmat_narxi', 'avans', 'kunlik_narxi', 'umumiy_narx']
        labels = {
            'mijoz': 'MIJOZ',
            'qurilma': 'USKUNA',
            'ishchi': 'MASTER',
            'berilgan_sanasi': 'BERILGAN SANA',
            'qaytish_sanasi': 'QAYTARISH SANASI',
            'kunlar_soni': 'Kunlar soni',  
            'umumiy_narx': 'Umumiy narx',  
            'montaj': 'Montaj',            
            'xizmat_narxi': 'Xizmat narxi',  
            'avans': 'Avans',               
            'miqdori': 'Miqdori',            
            'kunlik_narxi': 'Kunlik narxi',  
        }
    def __init__(self, *args, **kwargs):
        super(ProkotForm, self).__init__(*args, **kwargs)
        self.fields['ishchi'].queryset = CustomUser.objects.filter(lavozimi='Master')

class QaytarishForm(forms.ModelForm):
    class Meta:
        model = Qaytarish
        fields = ['qaytarilgan_sana', 'miqdori', 'nosozlik', 'summa', 'prokat']
        labels = {
            'qaytarilgan_sana': 'Qaytarilgan sana',
            'miqdori': 'Miqdori',
            'nosozlik': 'Nosozlik',
            'summa': 'Narx',
            'prokat': 'Qurilma',
        }
    def __init__(self, *args, **kwargs):
        super(QaytarishForm, self).__init__(*args, **kwargs)
        self.fields['prokat'].queryset = Prokat.objects.all()
        
        


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
    def __init__(self, *args, **kwargs):
        super(TamirlashForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(lavozimi='Master')
