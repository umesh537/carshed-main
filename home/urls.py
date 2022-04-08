from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import  include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.register, name='register'),
    
    #Rake Master
    path('editmfile', views.editm, name='editmfile'),
    path('masterfile', views.masterf, name='masterfile'),
    path('addfolder', views.addf, name='addfolder'),
    path('schedule_date', views.schedule_date, name='schedule_date'),
    path('schedule_date/schedule_upload', views.schedule_upload, name='schedule_upload'),
    path('newrake', views.newrake, name='newrake'),
    path('newrake/newrake_upload', views.newrake_upload, name='newrake_upload'),
    path('siemensdata', views.siemensdata, name='siemensdata'),
    path('rcfmemu_data', views.rcfmemu_data, name='rcfmemu_data'),
    path('btmemu_data', views.btmemu_data, name='btmemu_data'),
    path('acretro_data', views.acretro_data, name='acretro_data'),
    path('siemensdata/edit_siemens/<int:pk>/', views.edit_siemens, name='edit_siemens'),
    path('rcfmemu_data/edit_rcfmemu/<int:pk>/', views.edit_rcfmemu, name='edit_rcfmemu'),
    path('btmemu_data/edit_btmemu/<int:pk>/', views.edit_btmemu, name='edit_btmemu'),
    path('acretro_data/edit_acretro/<int:pk>/', views.edit_acretro, name='edit_acretro'),

    #Left Column
    path('kcs_layout', views.kcs_layout, name='kcs_layout'),
    path('pdfs_list', views.pdfs_list, name='pdfs_list'),
    path('pdfs_list/upload_pdf', views.upload_pdf, name='upload_pdf'),
    path('pdfs_list/<int:pk>/', views.delete_pdf, name='delete_pdf'),

    path('PP', views.pp, name='PP'),
    path('PP/pp_upload', views.pp_upload, name='pp_upload'),
    path('PP/<int:pk>/', views.pp_delete, name='pp_delete'),

    path('joint_notes', views.joint_notes, name='joint_notes'),
    path('joint_notes_2021', views.joint_notes_2021, name='joint_notes_2021'),
    path('joint_notes_2021/jointnotes_upload', views.jointnotes_upload, name='jointnotes_upload'),
    path('joint_notes_2021/<int:pk>/', views.jointnotes_delete21, name='jointnotes_delete21'),
    path('joint_notes_2022', views.joint_notes_2022, name='joint_notes_2022'),
    path('joint_notes_2022/jointnotes_upload22', views.jointnotes_upload22, name='jointnotes_upload22'),
    path('joint_notes_2022/<int:pk>/', views.jointnotes_delete22, name='jointnotes_delete22'),

    path('technical_files', views.technical_files, name='technical_files'),
    path('technical_files_2021', views.technical_files_2021, name='technical_files_2021'),
    path("technical_files_2021/tech_upload21", views.tech_upload21, name="tech_upload21"),
    path('technical_files_2021/<int:pk>/', views.techfiles21_delete, name='techfiles21_delete'),
    path('technical_files_2022', views.technical_files_2022, name='technical_files_2022'),
    path('technical_files_2022/tech_upload22', views.tech_upload22, name='tech_upload22'),
    path('technical_files_2022/<int:pk>/', views.techfiles22_delete, name='techfiles22_delete'),

    path('safety_drive', views.safety_drive, name='safety_drive'),
    path('safety_drive_2022', views.safety_drive_2022, name='safety_drive_2022'),
    path('safety_drive_2022/safety_upload22', views.safety_upload22, name='safety_upload22'),
    path('safety_drive_2022/<int:pk>', views.safety_delete22, name='safety_delete22'),

    path('safety_drive_2023', views.safety_drive_2023, name='safety_drive_2023'),
    path('safety_drive_2023/safety_upload23', views.safety_upload23, name='safety_upload23'),
    path('safety_drive_2023/<int:pk>', views.safety_delete23, name='safety_delete23'),

    path('kcs_photo_gallery', views.kcs_photo, name='kcs_photo_gallery'),
    path('kcs_cultural_g', views.kcs_cultural_g, name='kcs_cultural_g'),

    path('news_events', views.news_events, name='news_events'),
    path('news_events/nn_upload', views.nn_upload, name='nn_upload'),
    path('news_events/<int:pk>/', views.nn_delete, name='nn_delete'),



    #Performance target
    path('performance_stats', views.Performance_Stats, name='performance_stats'),
    path('performance_stats/pt_upload', views.Performance_upload, name='Performance_upload'),
    path('performance_stats/<int:pk>', views.Performance_delete, name='Performance_delete'),

    path('edit_cpcdo', views.c_pcdo, name='edit_cpcdo'),

    path('lpc_sheets', views.lpcsheets, name='lpc_sheets'),
    path('lpc_sheets/pt_upload', views.lpc_upload, name='lpc_upload'),
    path('lpc_sheets/<int:pk>', views.lpc_delete, name='lpc_delete'),

    path('opr_monthwise', views.opr_monthwise, name='opr_monthwise'),
    path('opr_monthwise/pt_upload', views.opr_upload, name='opr_upload'),
    path('opr_monthwise/<int:pk>', views.opr_delete, name='opr_delete'),

    path('pcdo_monthwise', views.pcdo_monthwise, name='pcdo_monthwise'),
    path('pcdo_monthwise/pt_upload', views.Performance_upload, name='Performance_upload'),
    path('pcdo_monthwise/<int:pk>', views.pcdo_delete, name='pcdo_delete'),

    path('presentation', views.presentation, name='presentation'),
    path('presentation/pt_upload', views.ppt_upload, name='ppt_upload'),
    path('presentation/<int:pk>', views.ppt_delete, name='ppt_delete'),

    path('assistance', views.assistance, name='assistance'),
    path('assistance/pt_upload', views.assist_upload, name='assist_upload'),
    path('assistance/<int:pk>', views.assist_delete, name='assist_delete'),

    path('goodworks', views.good_works, name='goodworks'),
    path('goodworks/pt_upload', views.gwork_upload, name='gwork_upload'),
    path('goodworks/<int:pk>', views.gwork_delete, name='gwork_delete'),

    path('cee_data', views.cee_data, name='cee_data'),
    path('cee_data/pt_upload', views.cee_upload, name='cee_upload'),
    path('cee_data/<int:pk>', views.cee_delete, name='cee_delete'),


# Data Book
    path('acbhel/', views.acbhel, name='acbhel'),
    path('acbhel/pt_upload', views.bhel_upload, name='bhel_upload'),
    path('acbhel/<int:pk>', views.bhel_delete, name='bhel_delete'),

    path('acretro/',views.acretro, name='acretro'),
    path('acretro/pt_upload', views.acretro_upload, name='acretro_upload'),
    path('acretro/<int:pk>', views.acretro_delete, name='acretro_delete'),

    path('memu/', views.memu, name='memu'),
    path('memu/pt_upload', views.memu_upload, name='memu_upload'),
    path('memu/<int:pk>', views.memu_delete, name='memu_delete'),

    path('bt_memu/', views.bt_memu, name='bt_memu'),
    path('bt_memu/pt_upload', views.btmemu_upload, name='btmemu_upload'),
    path('bt_memu/<int:pk>', views.btmemu_delete, name='btmemu_delete'),

    path('bt_emu/', views.bt_emu, name='bt_emu'),
    path('bt_emu/pt_upload', views.btemu_upload, name='btemu_upload'),
    path('bt_emu/<int:pk>', views.btemu_delete, name='btemu_delete'),

    path('medha/', views.medha, name='medha'),
    path('medha/pt_upload', views.medha_upload, name='medha_upload'),
    path('medha/<int:pk>', views.medha_delete, name='medha_delete'),

    path('siemens/', views.siemens, name='siemens'),
    path('siemens/pt_upload', views.siemens_upload, name='siemens_upload'),
    path('siemens/<int:pk>', views.siemens_delete, name='siemens_delete'),


# Timetable
   path("hb_up/", views.hb_up, name="hb_up"),
   path('hb_up/pt_upload', views.hbup_upload, name='hbup_upload'),
   path('hb_up/<int:pk>', views.hbup_delete, name='hbup_delete'),

   path("hb_down/", views.hb_down, name="hb_down"),
   path('hb_down/pt_upload', views.hbdown_upload, name='hbdown_upload'),
   path('hb_down/<int:pk>', views.hbdown_delete, name='hbdown_delete'),

   path("mainline_up/", views.mainline_up, name="mainline_up"),
   path('mainline_up/pt_upload', views.mainlineup_upload, name='mainlineup_upload'),
   path('mainline_up/<int:pk>', views.mainlineup_delete, name='mainlineup_delete'),

   path("mainline_down/", views.mainline_down, name="mainline_down"),
   path('mainline_down/pt_upload', views.mainlinedown_upload, name='mainlinedown_upload'),
   path('mainline_down/<int:pk>', views.mainlinedown_delete, name='mainlinedown_delete'),

   path("thb_up/", views.thb_up, name="thb_up"),
   path('thb_up/pt_upload', views.thbup_upload, name='thbup_upload'),
   path('thb_up/<int:pk>', views.thbup_delete, name='thbup_delete'),

   path("thb_down/", views.thb_down, name="thb_down"),
   path('thb_down/pt_upload', views.thbdown_upload, name='thbdown_upload'),
   path('thb_down/<int:pk>', views.thbdown_delete, name='thbdown_delete'),

   # EMEMO
   path("ememo/", views.ememo, name='ememo'),
   path("ememo/ememo_form", views.ememo_upload, name='ememo_upload')
    
]