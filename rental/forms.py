from django import forms
from django.db import models

from .models import CustomUser,Mijozlar,Qurilmalar,Prokat,Qaytarish, Tamirlash

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['ism', 'familiya', 'username', 'rasm']
        widgets = {
            'ism': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'}),
            'familiya': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'}),
            'username': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'}),
            'rasm': forms.FileInput(attrs={'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'}),
        }

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
        widget=forms.RadioSelect(attrs={
            'class': 'form-radio text-blue-600 focus:ring focus:ring-blue-300',
        }),
        label='JINS'
    )

    class Meta:
        model = Mijozlar
        fields = ['ism', 'familiya', 'username', 'telefon', 'jinsi', 'pasport', 'jshshir']
        labels = {
            'ism': 'ISM',
            'familiya': 'FAMILIYA',
            'username': 'FOYDALANUVCHI NOMI',
            'telefon': 'TELEFON RAQAM',
            'pasport': 'PASSPORT SERIYA VA RAQAM',
            'jshshir': 'JSHSHIR'
        }
        widgets = {
            'ism': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-blue-400 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300',
                'placeholder': 'Ismingizni kiriting'
            }),
            'familiya': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-blue-400 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300',
                'placeholder': 'Familiyangizni kiriting'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-blue-400 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300',
                'placeholder': 'Foydalanuvchi nomini kiriting'
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-blue-400 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300',
                'placeholder': 'Telefon raqamini kiriting'
            }),
            'pasport': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-blue-400 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300',
                'placeholder': 'Pasport seriya va raqami'
            }),
            'jshshir': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-blue-400 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300',
                'placeholder': 'JSHSHIRni kiriting'
            }),
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
        widgets = {
            'tur': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-lg shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200',
                'placeholder': 'Qurilma turini kiriting'
            }),
            'nomi': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-lg shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200',
                'placeholder': 'Qurilma nomini kiriting'
            }),
            'tasnif': forms.Textarea(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-lg shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200',
                'placeholder': 'Qurilma tasnifini kiriting',
                'rows': 3
            }),
            'holati': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-lg shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200',
                'placeholder': 'Holatini kiriting'
            }),
            'narxi': forms.NumberInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-lg shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200',
                'placeholder': 'Narxni kiriting',
                'min': '0'
            }),
            'rasmi': forms.FileInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-lg shadow-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200',
                'accept': 'image/*'
            }),
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
        widgets = {
    'berilgan_sanasi': forms.DateInput(attrs={
        'type': 'date',
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 appearance-none'
    }),
    'qaytish_sanasi': forms.DateInput(attrs={
        'type': 'date',
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 appearance-none'
    }),
    'kunlar_soni': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'miqdori': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'xizmat_narxi': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'avans': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'kunlik_narxi': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'umumiy_narx': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'ishchi': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'mijoz': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
    'qurilma': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
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
        widgets = {
            'qaytarilgan_sana': forms.DateInput(attrs={
                'type': 'date',  # Sana inputi uchun maxsus turi
                'class': 'w-full py-2 form-control border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'yyyy-mm-dd',  # Placeholder ko'rsatiladi
            }),
            'miqdori': forms.NumberInput(attrs={
                'class': 'w-full py-2 form-control border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Miqdor kiriting',
                'min': '1',  # Minimal qiymat
                'step': '1',  # Qiymatni bir birlikda oshirish
            }),
            'nosozlik': forms.TextInput(attrs={
                'class': 'w-full py-2 form-control border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Nosozlikni kiriting',
            }),
            'summa': forms.NumberInput(attrs={
                'class': 'w-full py-2 form-control border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Narxni kiriting',
                'min': '0',  # Minimal qiymat
                'step': '0.01',  # Qiymatni 0.01 bilan oshirish
            }),
            'prokat': forms.Select(attrs={
                'class': 'w-full py-2 form-control border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(QaytarishForm, self).__init__(*args, **kwargs)
        self.fields['prokat'].queryset = Prokat.objects.all()
        
        


from django import forms
from .models import CustomUser

class IshchiForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['ism', 'familiya', 'lavozimi', 'username', 'password',  'is_active']
        labels = {
            'ism': 'Ism',
            'familiya': 'Familiya',
            'lavozimi': 'Lavozim',
            'username': 'Username',
            'password': 'Parol',
            'is_active': 'Holat',
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control py-2 px-3 rounded-lg border-2 border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent w-full'}),
            'ism': forms.TextInput(attrs={'class': 'form-control py-2 px-3 rounded-lg border-2 border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent w-full'}),
            'familiya': forms.TextInput(attrs={'class': 'form-control py-2 px-3 rounded-lg border-2 border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent w-full'}),
            'lavozimi': forms.TextInput(attrs={'class': 'form-control py-2 px-3 rounded-lg border-2 border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent w-full'}),
            'username': forms.TextInput(attrs={'class': 'form-control py-2 px-3 rounded-lg border-2 border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent w-full'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600 focus:ring-2 focus:ring-blue-600'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600 focus:ring-2 focus:ring-blue-600'}),
        }


from .models import Tamirlash

class TamirlashForm(forms.ModelForm):
    class Meta:
        model = Tamirlash
        fields = ['qurilma', 'user', 'sana']
        labels = {
            'qurilma': 'Qurilma',
            'user': 'Usta',
            'sana': 'Sana',
        }
        widgets = {
            'qurilma': forms.Select(attrs={
                'class': 'block w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Qurilma tanlang'
            }),
            'user': forms.Select(attrs={
                'class': 'block w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Usta tanlang'
            }),
            'sana': forms.DateInput(attrs={
                'class': 'block w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(TamirlashForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(lavozimi='Master')
