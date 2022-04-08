from pyexpat import model
from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict

from .models import EMEMO, SiemensData, files, KcsCGImage, KcsPGImage, Newsevent
from .models import JointNotes21, JointNotes22, pplanning
from .models import Techfiles21, Techfiles22, Safety22, Safety23
from .models import performance, lpc_sheets, Pcdo, Opr, Cee, Presentation, Good_works, Assistance
from .models import Siemens, ACRetro, MEMU, BTEMU, BTMEMU, Medha, CBHEL
from .models import MainlineUP, MainlineDOWN, HBUP, HBDOWN, THBUP, THBDOWN
from .models import ScheduleRake, SiemensData, MemuRCF, MemuBT, AcretroData

class FilesForm(forms.ModelForm):
    class Meta:
        model = files
        fields = ('title', 'supervisor', 'pdf')

class JointNotes21Form(forms.ModelForm):
    class Meta:
        model = JointNotes21
        fields = ('title', 'supervisor', 'pdf')
class JointNotes22Form(forms.ModelForm):
    class Meta:
        model = JointNotes22
        fields = ('title', 'supervisor', 'pdf')

class Techfiles21Form(forms.ModelForm):
    class Meta:
        model = Techfiles21
        fields = ('title', 'supervisor', 'pdf')
class Techfiles22Form(forms.ModelForm):
    class Meta:
        model = Techfiles22
        fields = ('title', 'supervisor', 'pdf')

class Safety22Form(forms.ModelForm):
    class Meta:
        model = Safety22
        fields = ('title', 'supervisor', 'pdf')
class Safety23Form(forms.ModelForm):
    class Meta:
        model = Safety23
        fields = ('title', 'supervisor', 'pdf')

class PPForm(forms.ModelForm):
    class Meta:
        model = pplanning
        fields = ('title', 'supervisor', 'pdf')

class NewseventForm(forms.ModelForm):
    class Meta:
        model = Newsevent
        fields = ('title', 'supervisor', 'pdf')

class KcsCGform(forms.ModelForm):
    class Meta:
        model = KcsCGImage
        fields = '__all__'
        labels = {'photo':''}

class KcsPGform(forms.ModelForm):
    class Meta:
        model = KcsPGImage
        fields = '__all__'
        labels = {'photo':''}

# performance Stats
class PerformanceForm(forms.ModelForm):
    class Meta:
        model = performance
        fields = ('title', 'supervisor', 'pdf')
class LPCForm(forms.ModelForm):
    class Meta:
        model = lpc_sheets
        fields = ('title', 'supervisor', 'pdf')
class PCDOForm(forms.ModelForm):
    class Meta:
        model = Pcdo
        fields = ('title', 'supervisor', 'pdf')
class OPRForm(forms.ModelForm):
    class Meta:
        model = Opr
        fields = ('title', 'supervisor', 'pdf')
class CEEForm(forms.ModelForm):
    class Meta:
        model = Cee
        fields = ('title', 'supervisor', 'pdf')
class pptForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ('title', 'supervisor', 'pdf')
class GworkForm(forms.ModelForm):
    class Meta:
        model = Good_works
        fields = ('title', 'supervisor', 'pdf')
class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance
        fields = ('title', 'supervisor', 'pdf')


# Databook
class SiemensForm(forms.ModelForm):
    class Meta:
        model = Siemens
        fields = ('title', 'supervisor', 'pdf')
class ACRetroForm(forms.ModelForm):
    class Meta:
        model = ACRetro
        fields = ('title', 'supervisor', 'pdf')
class MemuForm(forms.ModelForm):
    class Meta:
        model = MEMU
        fields = ('title', 'supervisor', 'pdf')
class BTMemuForm(forms.ModelForm):
    class Meta:
        model = BTMEMU
        fields = ('title', 'supervisor', 'pdf')
class BTEmuForm(forms.ModelForm):
    class Meta:
        model = BTEMU
        fields = ('title', 'supervisor', 'pdf')
class MedhaForm(forms.ModelForm):
    class Meta:
        model = Medha
        fields = ('title', 'supervisor', 'pdf')
class CBHELForm(forms.ModelForm):
    class Meta:
        model = CBHEL
        fields = ('title', 'supervisor', 'pdf')

# Timetable

class MainlineUPForm(forms.ModelForm):
    class Meta:
        model = MainlineUP
        fields = ('title', 'supervisor', 'pdf')
class MainlineDOWNForm(forms.ModelForm):
    class Meta:
        model = MainlineDOWN
        fields = ('title', 'supervisor', 'pdf')
class HBUPForm(forms.ModelForm):
    class Meta:
        model = HBUP
        fields = ('title', 'supervisor', 'pdf')
class HBDOWNForm(forms.ModelForm):
    class Meta:
        model = HBDOWN
        fields = ('title', 'supervisor', 'pdf')
class THBUPForm(forms.ModelForm):
    class Meta:
        model = THBUP
        fields = ('title', 'supervisor', 'pdf')
class THBDOWNForm(forms.ModelForm):
    class Meta:
        model = THBDOWN
        fields = ('title', 'supervisor', 'pdf')

class ScheduleRakeFORM(forms.ModelForm):
    class Meta:
        model = ScheduleRake
        fields = (
            'rake_type', 'coach_position','be_dtc','ke_dtc','unit_no',
            'datetime','schedule_at','shift','ia','ic_quaterly','ust', 
            'servicer_after','washing','mopping','ti','pdf'    
        )
        widgets = {
            'mopping': forms.TextInput(
                attrs={'class':('row', 'col','form-control'), 'style': 'max-width:300px'}),
            'washing': forms.TextInput(
                attrs={'class':('row', 'col','form-control'), 'style': 'max-width:300px'}),
            'unit_no': forms.TextInput(
                attrs={'class':('row', 'col','form-control'),'style': 'max-width:300px'})
        }


class EmemoForm(forms.ModelForm):
    class Meta:
        model = EMEMO
        fields = '__all__'
        labels = {'photo':''}


class SiemensDataForm(forms.ModelForm):
    class Meta:
        model = SiemensData
        fields = '__all__'
class MemuRCFForm(forms.ModelForm):
    class Meta:
        model = MemuRCF
        fields = '__all__'
class MemuBTForm(forms.ModelForm):
    class Meta:
        model = MemuBT
        fields = '__all__'
class AcretroDataForm(forms.ModelForm):
    class Meta:
        model = AcretroData
        fields = '__all__'
