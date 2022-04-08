from ntpath import join
from django.contrib import admin
from django.contrib.admin.decorators import register

from home.models import register, KcsCGImage, KcsPGImage, Newsevent
from home.models import JointNotes21, JointNotes22, files, pplanning
from home.models import Techfiles22, Techfiles21, Safety22, Safety23
from home.models import performance, lpc_sheets, Pcdo, Opr, Cee, Presentation, Good_works, Assistance
from home.models import Siemens, ACRetro, MEMU, BTEMU, BTMEMU, Medha, CBHEL
from home.models import HBUP, HBDOWN, MainlineDOWN, MainlineUP, THBUP, THBDOWN
from home.models import ScheduleRake, NewRake, EMEMO, SiemensData, MemuBT, MemuRCF, AcretroData
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(register)

@admin.register(files)
class Kcslayout(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
    list_per_page = 10
@admin.register(JointNotes21)
class Joint21admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(JointNotes22)
class Joint22admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Techfiles21)
class Techfiles21admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Techfiles22)
class Techfiles22admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Safety22)
class Safety22admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Safety23)
class Safety23admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(pplanning)
class ppadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Newsevent)
class Newseventadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(KcsCGImage)
class KcsImageAdmin(admin.ModelAdmin):
   list_display = ['id', 'title', 'supervisor','photo', 'date']
@admin.register(KcsPGImage)
class KcsPGImageAdmin(admin.ModelAdmin):
   list_display = ['id', 'title', 'supervisor','photo', 'date']

#performance stats
@admin.register(performance)
class performanceadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(lpc_sheets)
class lpcadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Pcdo)
class pcdoadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Opr)
class opradmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Cee)
class ceeadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Presentation)
class pptadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Good_works)
class goodworksadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Assistance)
class assistanceadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']

# Databook
@admin.register(Siemens)
class siemensadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(ACRetro)
class ACRetroadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(MEMU)
class Memuadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(BTMEMU)
class BTMemuadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(BTEMU)
class BTEmuadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(Medha)
class Medhaadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(CBHEL)
class Cbheladmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']

# Timetable 

@admin.register(MainlineUP)
class MainlineUPadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(MainlineDOWN)
class MainlineDOWNadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(HBUP)
class HBUPadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(HBDOWN)
class HBDOWNadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(THBUP)
class THBUPadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']
@admin.register(THBDOWN)
class THBDOWNadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'supervisor','pdf']


@admin.register(ScheduleRake)
class SCHEDULERAKEAdmin(admin.ModelAdmin):
    list_display = ['id', 'rake_type', 'schedule_at', 'shift', 'washing', 'mopping']
    list_per_page = 10

@admin.register(NewRake)
class NEWRAKEAdmin(admin.ModelAdmin):
    list_display = ['id', 'rake_type', 'unit_no', 'coach_position', 'make', 'comm_date']
    list_per_page = 10

@admin.register(EMEMO)
class EMEMOAdmin(admin.ModelAdmin):
    list_display = ['id', 'unit_no', 'coach_no', 'line_no', 'report_by','report_signee']
    list_per_page = 10

@admin.register(SiemensData, MemuRCF, MemuBT, AcretroData)
class SIEMENSAdmin(ImportExportModelAdmin):
    list_display = ['id', 'Rake_Type', 'Coach_No', 'Comm_Date', 'Age_in_Yrs', 'Life_Left', 'Latest_POH_Date']
    list_per_page = 10