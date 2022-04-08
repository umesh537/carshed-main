
from decimal import Context
from unicodedata import name
from django.contrib import messages
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from home.models import BTEMU, BTMEMU, CBHEL, EMEMO, HBDOWN, HBUP, MEMU, THBDOWN, THBUP, ACRetro, AcretroData, JointNotes22, MainlineDOWN, MainlineUP, Medha, MemuBT, MemuRCF, NewRake, ScheduleRake, Siemens, Techfiles21, register
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from .forms import ACRetroForm, AcretroDataForm, BTEmuForm, BTMemuForm, CBHELForm, FilesForm, GworkForm, HBDOWNForm, HBUPForm, JointNotes22Form, JointNotes21Form, KcsCGform, KcsPGform, KcsCGImage, KcsPGImage, MainlineDOWNForm, MainlineUPForm, MedhaForm, MemuBTForm, MemuForm, MemuRCFForm, ScheduleRakeFORM, SiemensDataForm, SiemensForm, THBDOWNForm, THBUPForm
from django.urls import reverse_lazy
from .forms import files, JointNotes21, pplanning, PPForm, Newsevent, NewseventForm
from home.models import Techfiles21, Techfiles22, Safety22, Safety23, JointNotes22
from .forms import Techfiles21Form, Techfiles22Form, Safety22Form, Safety23Form
from home.models import performance, lpc_sheets, Pcdo, Opr, Cee, Presentation, Good_works, Assistance
from .forms import PerformanceForm, LPCForm, PCDOForm, OPRForm, CEEForm, pptForm, AssistanceForm
from home.models import NewRake, ScheduleRake, EMEMO, SiemensData
from django.contrib.auth.decorators import  login_required
# Create your views here.
@login_required(login_url=reverse_lazy("login"))
def index(request):
	if request.user.is_anonymous:
		return redirect("/login")
	return render(request, 'index.html')

# login user or logout
def loginuser(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/")
		else:
			return render(request, 'login.html')
	return render(request, 'login.html')

def logoutuser(request):
	logout(request)
	return redirect('/login')


# Rake Master     
def editm(request):
	return render(request, 'Rake master/editmfile.html')
def addf(request):
	return render(request, 'Rake master/addfolder.html')
def masterf(request):
	return render(request, 'Rake master/masterfile.html')
def schedule_date(request):
	pdfs = ScheduleRake.objects.all()
	context = {
		'data':pdfs,
	}
	return render(request, 'Rake master/schedule_date.html', context)
# def schedule_upload(request):
# 	form = ScheduleRakeFORM()
# 	return render(request, 'Rake master/schedule_upload.html', {'form':form})
def newrake(request):
	pdfs = NewRake.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'Rake master/new_rake.html', context)

# Left Column

def kcs_layout(request):
	context = {}
	if request.method == 'POST':
		upload_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(upload_file.name, upload_file)
		context['url'] = fs.url(name)
	return render(request, 'left column/kcs_layout.html', context)
def pdfs_list(request):
	pdfs = files.objects.all()
	return render(request, 'left column/pdfs_list.html', {'pdfs': pdfs})
def upload_pdf(request):
	if request.method == 'POST':
		form = FilesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('pdfs_list')
	else:
		form = FilesForm()
	return render(request, 'left column/upload_pdf.html', {
		'form': form
	})
def delete_pdf(request, pk):
	if request.method == 'POST':
		pdf = files.objects.get(pk=pk)
		pdf.delete()
	return redirect('pdfs_list')
		
# joint notes
def joint_notes(request):
	pdfs = JointNotes21.objects.all()
	pdfs2 = JointNotes22.objects.all()
	return render(request, 'left column/joint_notes.html', {'pdfs': pdfs, 'pdfs2':pdfs2})
	# return render(request, 'left column/joint_notes_2022.html', context)
	# return render(request, 'left column/joint_notes.html')
def joint_notes_2021(request):
	pdfs = JointNotes21.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'left column/joint_notes_2021.html', context)	 
def jointnotes_upload(request):
	form = JointNotes21Form()
	if request.method == 'POST':
		form = JointNotes21Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('joint_notes_2021')
	else:
		form = JointNotes21Form()
	return render(request, 'left column/upload_pdf.html', {
		'form': form
	})
def jointnotes_delete21(request, pk):
	if request.method == 'POST':
		pdf = JointNotes21.objects.get(pk=pk)
		pdf.delete()
	return redirect('joint_notes_2021')

def joint_notes_2022(request):
	pdfs = JointNotes22.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'left column/joint_notes_2022.html', context)
def jointnotes_upload22(request):
	form = JointNotes22Form()
	if request.method == 'POST':
		form = JointNotes22Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('joint_notes_2022')
	else:
		form = JointNotes22Form()
	return render(request, 'left column/jointnotes_upload22.html', {
		'form': form
	})

def jointnotes_delete22(request, pk):
	if request.method == 'POST':
		pdf = JointNotes22.objects.get(pk=pk)
		pdf.delete()
	return redirect('joint_notes_2022')

	
#technical Files
def technical_files(request):
	return render(request, 'left column/technical_files.html')

def technical_files_2021(request):
	pdfs = Techfiles21.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'left column/technical_files_2021.html', context)	 

def tech_upload21(request):
	if request.method == 'POST':
		form = Techfiles21Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('technical_files_2021')
	else:
		form = Techfiles21Form()
	return render(request, 'left column/tech_upload21.html', {
		'form': form
	})
def techfiles21_delete(request, pk):
	if request.method == 'POST':
		pdf = Techfiles21.objects.get(pk=pk)
		pdf.delete()
	return redirect('technical_files_2021')


def technical_files_2022(request):
	pdfs = Techfiles22.objects.all()
	context = {
		'data1':pdfs
	}
	return render(request, 'left column/technical_files_2022.html', context)
def tech_upload22(request):
	if request.method == 'POST':
		form = Techfiles22Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('technical_files_2022')
	else:
		form = Techfiles22Form()
	return render(request, 'left column/tech_upload22.html', {
		'form': form
	})
def techfiles22_delete(request, pk):
	if request.method == 'POST':
		pdf = Techfiles22.objects.get(pk=pk)
		pdf.delete()
	return redirect('technical_files_2022')

#photo Gallery
def kcs_photo(request):
	form = KcsPGform(request.POST, request.FILES)
	if form.is_valid():
		form.save()
	form = KcsPGform()
	img = KcsPGImage.objects.all() 
	return render(request, 'left column/kcs_photo_gallery.html', {'img':img, 'form':form})

def kcs_cultural_g(request):
	form = KcsCGform(request.POST, request.FILES)
	if form.is_valid():
		form.save()
	form = KcsCGform()
	img = KcsCGImage.objects.all() 
	return render(request, 'left column/kcs_cultural_g.html', {'img':img, 'form':form})

#safety Drive
def safety_drive(request):
	return render(request, 'left column/safety_drive.html')
def safety_drive_2022(request):
	pdfs = Safety22.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'left column/safety_drive_2022.html', context)
def safety_upload22(request):
	if request.method == 'POST':
		form = Safety22Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('safety_drive_2022')
	else:
		form = Safety22Form()
	return render(request, 'left column/safety_upload22.html', {
		'form': form
	})
def safety_delete22(request, pk):
	if request.method == 'POST':
		pdf = Safety22.objects.get(pk=pk)
		pdf.delete()
	return redirect('safety_drive_2022')

def safety_drive_2023(request):
	pdfs = Safety23.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'left column/safety_drive_2023.html', context)
def safety_upload23(request):
	if request.method == 'POST':
		form = Safety23Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('safety_drive_2023')
	else:
		form = Safety23Form()
	return render(request, 'left column/safety_upload23.html', {
		'form': form
	})
def safety_delete23(request, pk):
	if request.method == 'POST':
		pdf = Safety23.objects.get(pk=pk)
		pdf.delete()
	return redirect('safety_drive_2023')

# proposed 
def pp(request):
	pdfs = pplanning.objects.all()
	context = {
		'data':pdfs
	}
	return render(request, 'left column/pp.html', context)
def pp_upload(request):
	if request.method == 'POST':
		form = PPForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('PP')
	else:
		form = PPForm()
	return render(request, 'left column/pp_upload.html', {
		'form': form
	})
def pp_delete(request, pk):
	if request.method == 'POST':
		pdf = pplanning.objects.get(pk=pk)
		pdf.delete()
	return redirect('PP')

#news Events
def news_events(request):
	pdfs = Newsevent.objects.all()
	form = NewseventForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'left column/news_events.html', context)
def nn_upload(request):
	if request.method == 'POST':
		form = NewseventForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('news_events')
	else:
		form = NewseventForm()
	return render(request, 'left column/upload_pdf.html', {
		'form': form
	})
def nn_delete(request, pk):
	if request.method == 'POST':
		pdf = Newsevent.objects.get(pk=pk)
		pdf.delete()
	return redirect('news_events')

#performance Target 
def Performance_Stats(request):
	pdfs = performance.objects.all()
	context = {
		'data1':pdfs
	}
	return render(request, 'Performance Target/performance_stats.html', context)

def Performance_upload(request):
	form = PerformanceForm()
	if request.method == 'POST':
		form = PerformanceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('performance_stats')
	else:
		form = PerformanceForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def Performance_delete(request, pk):
	if request.method == 'POST':
		pdf = performance.objects.get(pk=pk)
		pdf.delete()
	return redirect('performance_stats')

def c_pcdo(request):
	return render(request, 'Performance Target/edit_cpcdo.html')


def lpcsheets(request):
	pdfs = lpc_sheets.objects.all()
	form = LPCForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/lpc_sheets.html', context)
def lpc_upload(request):
	form = LPCForm()
	if request.method == 'POST':
		form = LPCForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('lpc_sheets')
	else:
		form = LPCForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def lpc_delete(request, pk):
	if request.method == 'POST':
		pdf = lpc_sheets.objects.get(pk=pk)
		pdf.delete()
	return redirect('lpc_sheets')

def opr_monthwise(request):
	pdfs = Opr.objects.all()
	form = OPRForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/opr_monthwise.html', context)
def opr_upload(request):
	form = OPRForm()
	if request.method == 'POST':
		form = OPRForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('opr_monthwise')
	else:
		form = OPRForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def opr_delete(request, pk):
	if request.method == 'POST':
		pdf = Opr.objects.get(pk=pk)
		pdf.delete()
	return redirect('opr_monthwise')

def pcdo_monthwise(request):
	pdfs = Pcdo.objects.all()
	form = PCDOForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/pcdo_monthwise.html', context)
def Performance_upload(request):
	form = PCDOForm()
	if request.method == 'POST':
		form = PCDOForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('pcdo_monthwise')
	else:
		form = PCDOForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def pcdo_delete(request, pk):
	if request.method == 'POST':
		pdf = Pcdo.objects.get(pk=pk)
		pdf.delete()
	return redirect('pcdo_monthwise')

def cee_data(request):
	pdfs = Cee.objects.all()
	form = CEEForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/cee_conf_data.html', context)

def cee_upload(request):
	form = CEEForm()
	if request.method == 'POST':
		form = CEEForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('cee_data')
	else:
		form = CEEForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def cee_delete(request, pk):
	if request.method == 'POST':
		pdf = Cee.objects.get(pk=pk)
		pdf.delete()
	return redirect('cee_data')

def presentation(request):
	pdfs = Presentation.objects.all()
	form = pptForm()
	context = {
		'data1':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/ppt.html', context)
def ppt_upload(request):
	form = pptForm()
	if request.method == 'POST':
		form = pptForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('presentation')
	else:
		form = pptForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def ppt_delete(request, pk):
	if request.method == 'POST':
		pdf = Presentation.objects.get(pk=pk)
		pdf.delete()
	return redirect('presentation')

def assistance(request):
	pdfs = Assistance.objects.all()
	form = AssistanceForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/asistance_required.html', context)
def assist_upload(request):
	form = AssistanceForm()
	if request.method == 'POST':
		form = AssistanceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('assistance')
	else:
		form = AssistanceForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def assist_delete(request, pk):
	if request.method == 'POST':
		pdf = Assistance.objects.get(pk=pk)
		pdf.delete()
	return redirect('assistance')

def good_works(request):
	pdfs = Good_works.objects.all()
	form = GworkForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Performance Target/good_works.html', context)
def gwork_upload(request):
	form = GworkForm()
	if request.method == 'POST':
		form = GworkForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('goodworks')
	else:
		form = GworkForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def gwork_delete(request, pk):
	if request.method == 'POST':
		pdf = Good_works.objects.get(pk=pk)
		pdf.delete()
	return redirect('goodworks')


# Data Book

def siemens(request):
	pdfs = Siemens.objects.all()
	form = SiemensForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/siemens.html', context)
def siemens_upload(request):
	form = SiemensForm()
	if request.method == 'POST':
		form = SiemensForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('siemens')
	else:
		form = SiemensForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def siemens_delete(request, pk):
	if request.method == 'POST':
		pdf = lpc_sheets.objects.get(pk=pk)
		pdf.delete()
	return redirect('siemens')

def acbhel(request):
	pdfs = CBHEL.objects.all()
	form = CBHELForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/ac_bhel_emu.html', context)
def bhel_upload(request):
	form = CBHELForm()
	if request.method == 'POST':
		form = CBHELForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('acbhel')
	else:
		form = CBHELForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def bhel_delete(request, pk):
	if request.method == 'POST':
		pdf = CBHEL.objects.get(pk=pk)
		pdf.delete()
	return redirect('acbhel')

def acretro(request):
	pdfs = ACRetro.objects.all()
	form = ACRetroForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/ac_retro.html', context)
def acretro_upload(request):
	form = ACRetroForm()
	if request.method == 'POST':
		form = ACRetroForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('acretro')
	else:
		form = ACRetroForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def acretro_delete(request, pk):
	if request.method == 'POST':
		pdf = ACRetro.objects.get(pk=pk)
		pdf.delete()
	return redirect('acretro')

def bt_memu(request):
	pdfs = BTMEMU.objects.all()
	form = BTMemuForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/bt_memu.html', context)
def btmemu_upload(request):
	form = BTMemuForm()
	if request.method == 'POST':
		form = BTMemuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('bt_memu')
	else:
		form = BTMemuForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def btmemu_delete(request, pk):
	if request.method == 'POST':
		pdf = BTMEMU.objects.get(pk=pk)
		pdf.delete()
	return redirect('bt_memu')

def bt_emu(request):
	pdfs = BTEMU.objects.all()
	form = BTEmuForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/bt_emu.html', context)
def btemu_upload(request):
	form = BTEmuForm()
	if request.method == 'POST':
		form = BTEmuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('bt_emu')
	else:
		form = BTEmuForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def btemu_delete(request, pk):
	if request.method == 'POST':
		pdf = BTEMU.objects.get(pk=pk)
		pdf.delete()
	return redirect('bt_emu')

def memu(request):
	pdfs = MEMU.objects.all()
	form = MemuForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/memu.html', context)
def memu_upload(request):
	form = MemuForm()
	if request.method == 'POST':
		form = MemuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('memu')
	else:
		form = MemuForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def memu_delete(request, pk):
	if request.method == 'POST':
		pdf = MEMU.objects.get(pk=pk)
		pdf.delete()
	return redirect('memu')

def medha(request):
	pdfs = Medha.objects.all()
	form = MedhaForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'databook/medha.html', context)
def medha_upload(request):
	form = MedhaForm()
	if request.method == 'POST':
		form = MedhaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('medha')
	else:
		form = MedhaForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def medha_delete(request, pk):
	if request.method == 'POST':
		pdf = Medha.objects.get(pk=pk)
		pdf.delete()
	return redirect('medha')

# Timetable
def hb_down(request):
	pdfs = HBDOWN.objects.all()
	form = HBDOWNForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Timetable/hb_down.html', context)
def hbdown_upload(request):
	form = HBDOWNForm()
	if request.method == 'POST':
		form = HBDOWNForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('hb_down')
	else:
		form = HBDOWNForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def hbdown_delete(request, pk):
	if request.method == 'POST':
		pdf = HBDOWN.objects.get(pk=pk)
		pdf.delete()
	return redirect('hb_down')

def hb_up(request):
	pdfs = HBUP.objects.all()
	form = HBUPForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Timetable/hb_up.html', context)
def hbup_upload(request):
	form = HBUPForm()
	if request.method == 'POST':
		form = HBUPForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('hb_up')
	else:
		form = HBUPForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def hbup_delete(request, pk):
	if request.method == 'POST':
		pdf = HBUP.objects.get(pk=pk)
		pdf.delete()
	return redirect('hb_up')

def mainline_up(request):
	pdfs = MainlineUP.objects.all()
	form = MainlineUPForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Timetable/mainline_up.html', context)
def mainlineup_upload(request):
	form = MainlineUPForm()
	if request.method == 'POST':
		form = MainlineUPForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('mainline_up')
	else:
		form = MainlineUPForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def mainlineup_delete(request, pk):
	if request.method == 'POST':
		pdf = MainlineUP.objects.get(pk=pk)
		pdf.delete()
	return redirect('mainline_up')

def mainline_down(request):
	pdfs = MainlineDOWN.objects.all()
	form = MainlineDOWNForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Timetable/mainline_down.html', context)
def mainlinedown_upload(request):
	form = MainlineDOWNForm()
	if request.method == 'POST':
		form = MainlineDOWNForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('mainline_down')
	else:
		form = MainlineDOWNForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def mainlinedown_delete(request, pk):
	if request.method == 'POST':
		pdf = MainlineDOWN.objects.get(pk=pk)
		pdf.delete()
	return redirect('mainline_down')

def thb_up(request):
	pdfs = THBUP.objects.all()
	form = THBUPForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Timetable/thb_up.html', context)
def thbup_upload(request):
	form = THBUPForm()
	if request.method == 'POST':
		form = THBUPForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('thb_up')
	else:
		form = THBUPForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def thbup_delete(request, pk):
	if request.method == 'POST':
		pdf = THBUP.objects.get(pk=pk)
		pdf.delete()
	return redirect('thb_up')

def thb_down(request):
	pdfs = THBDOWN.objects.all()
	form = THBDOWNForm()
	context = {
		'data':pdfs,
		'form': form
	}
	return render(request, 'Timetable/thb_down.html', context)
def thbdown_upload(request):
	form = THBDOWNForm()
	if request.method == 'POST':
		form = THBDOWNForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('thb_down')
	else:
		form = THBDOWNForm()
	return render(request, 'Performance Target/pt_upload.html', {
		'form': form
	})
def thbdown_delete(request, pk):
	if request.method == 'POST':
		pdf = THBDOWN.objects.get(pk=pk)
		pdf.delete()
	return redirect('thb_down')


def schedule_upload(request):
	if request.method == 'POST':
		rake_type = request.POST.get('select_rake')
		be_dtc = request.POST.get('be_dtc')
		ke_dtc = request.POST.get('ke_dtc')
		unit_no = request.POST.get('unit_no')
		datetime = request.POST.get('datetime')
		shift = request.POST.get('shift')
		coach_position = 1233
		schedule_at = request.POST.get('schedule_at')
		ia = request.POST.get('ia')
		washing = request.POST.get('washing')
		mopping = request.POST.get('mopping')
		schedulerake = ScheduleRake(rake_type=rake_type, be_dtc=be_dtc, 
		ke_dtc=ke_dtc, unit_no=unit_no, datetime=datetime, shift=shift,
		schedule_at=schedule_at, ia=ia, coach_position= coach_position, 
		washing=washing, mopping=mopping)
		schedulerake.save()
		messages.success(request, 'Your message has been sent1')
		return schedule_date(request)
	context = {'raketype':ScheduleRake.RAKETYPES_CHOICES, 
	           'schedule_at': ScheduleRake.SCHEDULE_DONE_AFTER_CHOICES,
			   'ia':ScheduleRake.IA_CHOICES,
			   'ti':ScheduleRake.TI_CHOICES,
			   'shift':ScheduleRake.SHIFT_CHOICES,
			   'ic_quaterly': ScheduleRake.IC_QUATERLY_CHOICES,
			   'ust':ScheduleRake.UST_CHOICES,	  
	}
	return render(request, 'Rake master/schedule_upload.html', context=context)

def newrake_upload(request):
	if request.method == 'POST':
		raketype = request.POST.get('select_rake')
		coach_position = request.POST.get('coach_position')
		unit_no = request.POST.get('unit_no')
		rake_id = request.POST.get('rake_id')
		make = request.POST.get('make')
		coach_no = request.POST.get('coach_no')
		comm_date = request.POST.get('comm_date')
		newrake = NewRake(rake_type=raketype, coach_position=coach_position, 
		coach_no=coach_no,rake_id=rake_id, make=make, comm_date=comm_date, unit_no=unit_no)
		newrake.save()
		messages.success(request, 'Your message has been sent')
		return redirect('newrake')
	context = {'raketype':NewRake.RAKETYPES_CHOICES, 
	           'rake_id':NewRake.RAKEID_CHOICES,
	           'make':NewRake.MAKE_CHOICES,
	}
	return render(request, 'Rake master/newrake_upload.html', context=context)

def ememo(request):
	pdfs = EMEMO.objects.all()
	context = {
		'data':pdfs,
	}
	return render(request, 'EMEMO/ememo.html', context=context)

def ememo_upload(request):
	if request.method == 'POST':
		coach_no = request.POST.get('coach_no')
		line_no = request.POST.get('line_no')
		unit_no = request.POST.get('unit_no')
		rake_formation = request.POST.get('rake_formation')
		poh = request.POST.get('poh') if request.POST.get('poh') != "" else None 
		IA = request.POST.get('IA') if request.POST.get('IA') != "" else None
		TI = request.POST.get('TI') if request.POST.get('TI') != "" else None
		W = request.POST.get('W') if request.POST.get('W') != "" else None
		M = request.POST.get('M') if request.POST.get('M') != "" else None
		IC = request.POST.get('IC') if request.POST.get('IC') != "" else None
		UST = request.POST.get('UST') if request.POST.get('UST') != "" else None
		defects_reported = request.POST.get('defects_reported')
		train_no = request.POST.get('train_no')
		report_by = request.POST.get('report_by')
		nature_of_defects = request.POST.get('nature_of_defects')
		place_of_failure = request.POST.get('place_of_failure')
		failure_report = request.POST.get('failure_report')
		report_signee = request.POST.get('report_signee')
		investigation = request.POST.get('investigation')
		image = request.FILES.get('image')
		investigation_signee = request.POST.get('investigation_signee')
		remarks = request.POST.get('remarks')
		ememo = EMEMO(coach_no=coach_no, unit_no=unit_no,rake_formation=rake_formation, 
		poh=poh, IA=IA, TI=TI, W=W, M=M, IC=IC, UST=UST, defects_reported=defects_reported,
		train_no=train_no, report_by=report_by, nature_of_defects=nature_of_defects, 
		place_of_failure=place_of_failure, failure_report=failure_report, report_signee=report_signee,
		image=image, investigation_signee=investigation_signee, remarks=remarks, line_no=line_no,
		investigation = investigation )
		ememo.save()
		messages.success(request, 'Your message has been sent')
		return redirect('ememo')
	return render(request, 'EMEMO/ememo_form.html')

def siemensdata(request):
	items = SiemensData.objects.all()
	context = {
		'data':items,
	}
	return render(request, 'Rake master/siemens_data.html', context=context)
def rcfmemu_data(request):
	items = MemuRCF.objects.all()
	context = {
		'data':items,
	}
	return render(request, 'Rake master/siemens_data.html', context=context)
def btmemu_data(request):
	items = MemuBT.objects.all()
	context = {
		'data':items,
	}
	return render(request, 'Rake master/siemens_data.html', context=context)
def acretro_data(request):
	items = AcretroData.objects.all()
	context = {
		'data':items,
	}
	return render(request, 'Rake master/siemens_data.html', context=context)

def edit_data(request, pk, model, cls):
	item = get_object_or_404(model, pk=pk)
	if request.method == "POST":
		form = cls(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('siemensdata')
	else:
		form = cls(instance=item)
	return render(request, 'Rake master/edit_data.html', {'form':form})

def edit_siemens(request, pk):
	return edit_data(request, pk, SiemensData, SiemensDataForm)
def edit_rcfmemu(request, pk):
	return edit_data(request, pk, MemuRCF, MemuRCFForm)
def edit_btmemu(request, pk):
	return edit_data(request, pk, MemuBT, MemuBTForm)
def edit_acretro(request, pk):
	return edit_data(request, pk, AcretroData, AcretroDataForm)




def register(request):
	if request.method == "POST":
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		person = register(firstname=firstname, lastname=lastname,username=username, email=email, password=password)
		person.save()
	return render(request, 'register.html')
