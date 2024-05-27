from django.urls import path

from rental.views import LoginView,HomeView,LogoutView,MijozView,MijozUpdateView,QurilmaView,QurilmaQushView,QurilmaDeleteView,QurilmaUpdateView,ShartnomaView,ShartnomaDownloadView,ShartnomaEditView,ShartnomaDeleteView,QaytarishView,QaytarishDeleteView,QaytarishEditView 
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/',HomeView.as_view(),name='home'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('mijoz/',MijozView.as_view(),name='mijoz'),
    path('mijoz/<int:pk>/edit/', MijozUpdateView.as_view(), name='edit_mijoz'),
    path('qurilmalar/',QurilmaView.as_view(),name='qurilmalar'),
    path('qurilma/qush/',QurilmaQushView.as_view(),name='qurilma_qush'),
    path('qurilma/<int:pk>/edit/', QurilmaUpdateView.as_view(), name='qurilma_edit'),
    path('qurilma/<int:pk>/delete/', QurilmaDeleteView.as_view(), name='qurilma_delete'),
    path('prokot/',ShartnomaView.as_view(),name='prokot'),
    path('shartnoma/download/<int:pk>/', ShartnomaDownloadView.as_view(), name='shartnoma_download'),
    path('editProkot/<int:pk>/',ShartnomaEditView.as_view(),name='edit_prokot'),
    path('DeleteProkot/<int:pk>/',ShartnomaDeleteView.as_view(),name='delete_prokot'),
    path('qaytarish/',QaytarishView.as_view(),name='qaytarish'),
    path('deleteqaytarish/<int:pk>/',QaytarishDeleteView.as_view(),name='qaytarish_delete'),
    path('qaytarish/<int:pk>/edit/', QaytarishEditView.as_view(), name='qaytarish_edit'),
    
    path('ishchilar/', IshchiView.as_view(), name='ishchilar'),
    path('ishchilar/qosh/', IshchiQoshishView.as_view(), name='ishchi_qoshish'),
    path('ishchi/<int:id>/edit/', IshchiEditView.as_view(), name='ishchi_edit'),
    path('ishchi/<int:id>/delete/', IshchiDeleteView.as_view(), name='ishchi_delete'),

    path('tamirlash/', TamirlashView.as_view(), name='tamirlash'),
    path('tamirlash/qosh/', TamirlashQoshView.as_view(), name='tamirlash_qosh'),
    path('tamirlash/edit/<int:pk>/', TamirlashEditView.as_view(), name='tamirlash_edit'),
    path('tamirlash/delete/<int:id>/', TamirlashDeleteView.as_view(), name='tamirlash_delete'),


    
    

]
