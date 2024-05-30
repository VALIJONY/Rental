from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import View,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password

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
    
    
from django.http import HttpResponse
from django.views import View
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from .models import Prokat

class ShartnomaDownloadView(View):
    def get(self, request, pk):
        shartnoma = Prokat.objects.get(id=pk)
        document = Document()

        # Heading
        heading = document.add_heading(level=0)
        run = heading.add_run('Хорезмская область прокатная компания ИНН 665899871416, 620102, г.\n'
                              'Аль Хорезми, ул. Телефон Радищевой: +998(99)-999-99-99')
        run.font.size = Pt(13)
        run.bold = True
        heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        title = document.add_paragraph('Квитанция об оплате')
        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        # Order details
        table = document.add_table(rows=3, cols=2)
        table.cell(0, 0).text = 'Номер заказа:'
        table.cell(0, 1).text = f'{shartnoma.id:08d}'
        table.cell(1, 0).text = 'Дата начала:'
        table.cell(1, 1).text = shartnoma.berilgan_sanasi.strftime('%d.%m.%Y %H:%M')
        table.cell(2, 0).text = 'Дата окончания:'
        table.cell(2, 1).text = shartnoma.qaytish_sanasi.strftime('%d.%m.%Y %H:%M')

        document.add_paragraph(f'ФИО заказчика: {shartnoma.mijoz.ism}')

        
        # Item details
        document.add_paragraph()
        table = document.add_table(rows=1, cols=4)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Название'
        hdr_cells[1].text = 'Залог (руб)'
        hdr_cells[2].text = 'Цена проката за сутки (руб)'
        hdr_cells[3].text = 'Количество'

        row_cells = table.add_row().cells
        row_cells[0].text = shartnoma.qurilma.nomi
        row_cells[1].text = str(shartnoma.avans)
        row_cells[2].text = str(shartnoma.kunlik_narxi)
        row_cells[3].text = str(shartnoma.miqdori)

        # Adding borders to the table
        for row in table.rows:
            for cell in row.cells:
                tc_pr = cell._element.get_or_add_tcPr()
                tc_borders = OxmlElement('w:tcBorders')
                for border_name in ['top', 'left', 'bottom', 'right']:
                    border = OxmlElement(f'w:{border_name}')
                    border.set(qn('w:val'), 'single')
                    tc_borders.append(border)
                tc_pr.append(tc_borders)

        # Summary details
        document.add_paragraph()
        document.add_paragraph(f'Сумма залога (руб): {shartnoma.avans}')
        document.add_paragraph(f'Стоимость проката с учётом количества дней (руб): {shartnoma.kunlik_narxi}')
        document.add_paragraph(f'Количество дней: {shartnoma.kunlar_soni}')
        document.add_paragraph()
        document.add_paragraph(f'Сумма к оплате: {shartnoma.umumiy_narx} (руб)')
        document.add_paragraph()

        # Signatures
        document.add_paragraph('Подпись заказчика: _____________________________________')
        document.add_paragraph(f'{shartnoma.mijoz.ism}')
        document.add_paragraph('Подпись сотрудника: ____________________________________')
        document.add_paragraph(f'{shartnoma.ishchi.ism}')

        # Response
        file_name = f'shartnoma_{shartnoma.id}.docx'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        document.save(response)

        return response



    
# class ShartnomaDownloadView(View):
#     def get(self, request, pk):
#         shartnoma = Prokat.objects.get(id=pk)
#         document = Document()

#         document.add_heading('Shartnoma', 0)

#         document.add_paragraph(f'Клиент: {shartnoma.mijoz.ism}')
#         document.add_paragraph(f'Устройство:  {shartnoma.qurilma.nomi}')
#         document.add_paragraph(f'Количество: {shartnoma.miqdori}')
#         document.add_paragraph(f'Работник:  {shartnoma.ishchi.ism}')
#         document.add_paragraph(f'Дата выдачи: {shartnoma.berilgan_sanasi}')
#         document.add_paragraph(f'Дата возврата: {shartnoma.qaytish_sanasi}')
#         document.add_paragraph(f'Количество дней: {shartnoma.kunlar_soni}')
#         document.add_paragraph(f'Монтаж  {shartnoma.montaj}')
#         document.add_paragraph(f'Цена услуги: {shartnoma.xizmat_narxi} сум')
#         document.add_paragraph(f'Залок: {shartnoma.avans} сум')
#         document.add_paragraph(f'Ежедневная цена: {shartnoma.kunlik_narxi} сум')
#         document.add_paragraph(f'Общая цена: {shartnoma.umumiy_narx} сум')


#         file_name = f'shartnoma_{shartnoma.id}.docx'

#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = f'attachment; filename={file_name}'
        
#         document.save(response)
        
#         return response
    
class QaytarishView(LoginRequiredMixin,View):
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

class QaytarishDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        malumot=Qaytarish.objects.get(id=pk)
        malumot.delete()
        return redirect ('qaytarish')
class QaytarishEditView(LoginRequiredMixin,UpdateView):
    model = Qaytarish
    form_class=QaytarishForm
    template_name = 'qaytarish_edit.html'
    success_url = reverse_lazy('qaytarish')
    
    
    
from django.http import HttpResponse
from django.views import View
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from .models import Qaytarish

class QaytarishDocxDownloadView(View):
    def get(self, request, pk):
        qaytarish = Qaytarish.objects.get(id=pk)
        document = Document()

        # Heading
        heading = document.add_heading(level=0)
        run = heading.add_run('Хорезмская область прокатная компания ИНН 665899871416, 620102, г.\n'
                              'Аль Хорезми, ул. Телефон Радищевой: +998(99)-999-99-99')
        run.font.size = Pt(13)  # Setting smaller font size
        run.bold = True
        heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        title = document.add_paragraph('Квитанция о возврате')
        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        # Order details
        table = document.add_table(rows=3, cols=2)
        table.cell(0, 0).text = 'Номер заказа:'
        table.cell(0, 1).text = f'{qaytarish.prokat.id:08d}'
        table.cell(1, 0).text = 'Дата начала:'
        table.cell(1, 1).text = qaytarish.prokat.berilgan_sanasi.strftime('%d.%m.%Y %H:%M')
        table.cell(2, 0).text = 'Дата возврата:'
        table.cell(2, 1).text = qaytarish.qaytarilgan_sana.strftime('%d.%m.%Y %H:%M')

        document.add_paragraph(f'ФИО заказчика: {qaytarish.prokat.mijoz.ism}')

        # Adding borders to the table
        

        # Item details
        document.add_paragraph()
        table = document.add_table(rows=1, cols=4)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Название'
        hdr_cells[1].text = 'Залог (сум)'
        hdr_cells[2].text = 'Цена проката за сутки (сум)'
        hdr_cells[3].text = 'Количество'

        row_cells = table.add_row().cells
        row_cells[0].text = qaytarish.prokat.qurilma.nomi
        row_cells[1].text = str(qaytarish.prokat.avans)
        row_cells[2].text = str(qaytarish.prokat.kunlik_narxi)
        row_cells[3].text = str(qaytarish.prokat.miqdori)

        # Adding borders to the table
        for row in table.rows:
            for cell in row.cells:
                tc_pr = cell._element.get_or_add_tcPr()
                tc_borders = OxmlElement('w:tcBorders')
                for border_name in ['top', 'left', 'bottom', 'right']:
                    border = OxmlElement(f'w:{border_name}')
                    border.set(qn('w:val'), 'single')
                    tc_borders.append(border)
                tc_pr.append(tc_borders)

        # Summary details
        document.add_paragraph()
        document.add_paragraph(f'Сумма залога (сум): {qaytarish.prokat.avans}')
        document.add_paragraph(f'Стоимость проката с учётом количества дней (сум): {qaytarish.prokat.kunlik_narxi}')
        document.add_paragraph(f'Количество дней: {qaytarish.prokat.kunlar_soni}')
        document.add_paragraph()
        document.add_paragraph(f'Сумма к оплате: {qaytarish.prokat.umumiy_narx} (сум)')
        document.add_paragraph()

        # Signatures
        document.add_paragraph('Подпись заказчика: _____________________________________')
        document.add_paragraph(f'{qaytarish.prokat.mijoz.ism}')
        document.add_paragraph('Подпись сотрудника: ____________________________________')
        document.add_paragraph(f'{qaytarish.prokat.ishchi.ism}')

        # Response
        file_name = f'qaytarish_{qaytarish.id}.docx'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        document.save(response)

        return response

    
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
            new_ishchi = ishchi_form.save(commit=False)
            new_ishchi.password = make_password(ishchi_form.cleaned_data['password'])
            new_ishchi.save()
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
    

