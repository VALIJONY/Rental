from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import View,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from docx import Document

from django.contrib.auth.views import LoginView, LogoutView
from .forms import IshchiForm, QurilmaForm, TamirlashForm, UserLoginForm,MijozForm,ProkotForm,QaytarishForm

from .models import CustomUser, Mijozlar, Qaytarish,Qurilmalar,Prokat, Tamirlash

class Loginview(View):
    def get(self,request):
        userlogin=UserLoginForm()
        return render(request,'registration/login.html',{'form':userlogin})
    
    def post(self,request):
        check=UserLoginForm(data=request.POST)
        if check.is_valid():
            user=check.get_user()
            login(request,user)
          
            return render(request,'home.html')
        else:
            return redirect('login')
class LogoutView(LoginRequiredMixin,View):
         def get(self,request):
             logout(request)
             return redirect('login')
class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'home.html')

class MijozView(LoginRequiredMixin,View):
    def get(self,request):
        mijozlar=Mijozlar.objects.all()
        mijoz=MijozForm()
        return render(request,'mijoz_qushish.html',{'form':mijoz,'mijoz':mijozlar})
    def post(self,request):
        mijozlar=Mijozlar.objects.all()
        mijoz=MijozForm(data=request.POST)
        if mijoz.is_valid():
            mijoz.save()
            return render(request, 'qurilmalar.html')
        else:
            return redirect('mijoz',{'message':'Malumot saqlanmadi','mijoz':mijozlar})
        
class MijozUpdateView(LoginRequiredMixin,UpdateView):
    model = Mijozlar
    form_class = MijozForm
    template_name = 'edit_mijoz.html'
    success_url = reverse_lazy('mijoz')

class QurilmaView(LoginRequiredMixin,View):
    def get(self,request):
        qurilma=Qurilmalar.objects.all()
        return render(request,'qurilmalar.html',{'qurilmalar':qurilma})
    
class QurilmaQushView(LoginRequiredMixin,View):
    def get(self, request):
        qurilma_form = QurilmaForm()
        qurilmalar = Qurilmalar.objects.all()
        return render(request, 'qurilmalar.html', {'form': qurilma_form, 'qurilmalar': qurilmalar})

    def post(self, request):
        qurilma_form = QurilmaForm(data=request.POST,files=request.FILES)
        qurilmalar = Qurilmalar.objects.all()
        if qurilma_form.is_valid():
            qurilma_form.save()
            return redirect('qurilmalar')
        else:
            return render(request, 'qurilmalar.html', {'form': qurilma_form, 'qurilmalar': qurilmalar, 'message': 'Qurilma saqlanmadi'})

class QurilmaUpdateView(UpdateView):
    model = Qurilmalar
    form_class=QurilmaForm
    template_name = 'qurilma_edit.html'
    success_url = reverse_lazy('qurilmalar')

class QurilmaDeleteView(View):
    def get(self, request, pk):
        qurilma = Qurilmalar.objects.get(id=pk)
        qurilma.delete()
        return redirect('qurilmalar')
    
class ShartnomaView(View):
    def get(self, request):
        shartnoma = ProkotForm()
        shartnomalar = Prokat.objects.all()
        return render(request, 'shartnoma.html', {'form': shartnoma, 'shartnomalar': shartnomalar})

    def post(self, request):
        shartnoma = ProkotForm(data=request.POST)
        shartnomalar = Prokat.objects.all()
        if shartnoma.is_valid():
            shartnoma.save()
            message = 'Shartnoma muaffaqiyatli tuzildi'
        else:
            message = "Shartnoma saqlanmadi"
        
        return render(request, 'shartnoma.html', {'form': shartnoma, 'shartnomalar': shartnomalar, 'message': message})
    
class ShartnomaEditView(UpdateView):
    model=Prokat
    form_class=ProkotForm
    template_name='edit_prokot.html'
    success_url=reverse_lazy('prokot')
class ShartnomaDeleteView(LoginRequiredMixin,View):
     def get(self, request, pk):
        shartnoma = Prokat.objects.get(id=pk)
        shartnoma.delete()
        return redirect('prokot')
class ShartnomaDownloadView(View):
    def get(self, request, pk):
        shartnoma = Prokat.objects.get(id=pk)
        document = Document()

        document.add_heading('Shartnoma', 0)

        document.add_paragraph(f'Mijoz: {shartnoma.mijoz.ism}')
        document.add_paragraph(f'Qurilma: {shartnoma.qurilma.nomi}')
        document.add_paragraph(f'Ishchi: {shartnoma.ishchi.ism}')
        document.add_paragraph(f'Berilgan sana: {shartnoma.berilgan_sanasi}')
        document.add_paragraph(f'Qaytarish sana: {shartnoma.qaytish_sanasi}')
        document.add_paragraph(f'Kunlar soni: {shartnoma.kunlar_soni}')
        document.add_paragraph(f'Umumiy narx: {shartnoma.umumiy_narx} so`m')
        document.add_paragraph(f'Montaj: {shartnoma.montaj}')
        document.add_paragraph(f'Xizmat narxi: {shartnoma.xizmat_narxi} so`m')
        document.add_paragraph(f'Avans: {shartnoma.avans} so`m')
        document.add_paragraph(f'Miqdori: {shartnoma.miqdori}')
        document.add_paragraph(f'Kunlik narxi: {shartnoma.kunlik_narxi} so`m')

        file_name = f'shartnoma_{shartnoma.id}.docx'

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        
        document.save(response)
        
        return response
    
class QaytarishView(View):
    def get(self,request):
        form=QaytarishForm()
        malumot=Qaytarish.objects.all()
        return render(request,'qaytarish.html',{'form':form,'malumotlar':malumot})
    def post(self,request):
        form=QaytarishForm(data=request.POST)
        malumot=Qaytarish.objects.all()
        if form.is_valid():
            form.save()
            return redirect('qaytarish')
        else:
            message='Saqlanmadi'
            return redirect('qaytarish',{'message':message,'malumotlar':malumot})

class QaytarishDeleteView(View):
    def get(self,request,pk):
        malumot=Qaytarish.objects.get(id=pk)
        malumot.delete()
        return redirect ('qaytarish')
class QaytarishEditView(UpdateView):
    model = Qaytarish
    form_class=QaytarishForm
    template_name = 'qaytarish_edit.html'
    success_url = reverse_lazy('qaytarish')
    
class TamirlashView(LoginRequiredMixin, View):
    def get(self, request):
        tamirlash = Tamirlash.objects.all()
        return render(request, 'tamirlash.html', {'tamirlash': tamirlash})

class TamirlashQoshView(LoginRequiredMixin,View):
    def get(self, request):
        tamirlash_form = TamirlashForm()
        tamirlash = Tamirlash.objects.all()
        return render(request, 'tamirlash_form.html', {'form': tamirlash_form, 'tamirlash': tamirlash})

    def post(self, request):
        tamirlash_form = TamirlashForm(data=request.POST)
        tamirlash = Tamirlash.objects.all()
        if tamirlash_form.is_valid():
            tamirlash_form.save()
            return redirect('tamirlash')
        else:
            return render(request, 'tamirlash_form.html', {'form': tamirlash_form, 'tamirlash': tamirlash, 'message': 'tamirlash saqlanmadi'})

class TamirlashEditView(LoginRequiredMixin, UpdateView):
    model = Tamirlash
    form_class = TamirlashForm
    template_name = 'tamirlash_edit.html'
    success_url = reverse_lazy('tamirlash')


class TamirlashDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        tamirlash = Tamirlash.objects.get(id=id)
        tamirlash.delete()
        return redirect('tamirlash')

class IshchiView(LoginRequiredMixin, View):
    def get(self, request):
        ishchi = CustomUser.objects.all()
        return render(request, 'ishchi.html', {'ishchi': ishchi})

class IshchiQoshishView(LoginRequiredMixin, View):
    def get(self, request):
        ishchi_form = IshchiForm()
        ishchilar = CustomUser.objects.all()
        return render(request, 'ishchi_form.html', {'form': ishchi_form, 'ishchilar': ishchilar})

    def post(self, request):
        ishchi_form = IshchiForm(data=request.POST)
        ishchilar = CustomUser.objects.all()
        if ishchi_form.is_valid():
            ishchi_form.save()
            return redirect('ishchilar')
        else:
            return render(request, 'ishchi_form.html', {'form': ishchi_form, 'ishchilar': ishchilar, 'message': 'Ishchi saqlanmadi'})

class IshchiEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = IshchiForm
    template_name = 'ishchi_edit.html'
    success_url = reverse_lazy('ishchilar')

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, id=self.kwargs['id'])


class IshchiDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        ischi = CustomUser.objects.get(id=id)
        ischi.delete()
        return redirect('ishchilar')
