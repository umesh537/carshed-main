from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from emu.settings import DATE_FORMAT

# Create your models here.

class register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)

#left columns

class files(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/kcs_layout/')

    def __str__(self):
        return self.title
    
class JointNotes21(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/joint_notes_2021_pdf/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class JointNotes22(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/joint_notes_2022_pdf/')

    def __str__(self):
        return self.title

class Techfiles21(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/technical_files_2021_pdf/')

    def __str__(self):
        return self.title
class Techfiles22(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/technical_files_2022_pdf/')

    def __str__(self):
        return self.title

class Safety22(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/safety_drive_2022_pdf/')

    def __str__(self):
        return self.title
class Safety23(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/safety_drive_2023_pdf/')

    def __str__(self):
        return self.title

class pplanning(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pp_pdf/')

    def __str__(self):
        return self.title

class Newsevent(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/news_events/')

    def __str__(self):
        return self.title

class KcsCGImage(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    photo = models.ImageField(upload_to = 'pdfs/kcs_cultural_g_pdf/')
    date = models.DateTimeField(auto_now_add=True)

class KcsPGImage(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    photo = models.ImageField(upload_to = 'pdfs/kcs_Photo_g_pdf/')
    date = models.DateTimeField(auto_now_add=True)

# Performance Statstics

class performance(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/performance')

    def __str__(self):
        return self.title
class lpc_sheets(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/lpc')

    def __str__(self):
        return self.title
class Pcdo(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/pcdo')

    def __str__(self):
        return self.title
class Opr(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/opr')

    def __str__(self):
        return self.title
class Cee(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/cee')

    def __str__(self):
        return self.title
class Presentation(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/ppt')

    def __str__(self):
        return self.title
class Good_works(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/gworks')

    def __str__(self):
        return self.title
class Assistance(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/pt/assistance')

    def __str__(self):
        return self.title

# Databook
class Siemens(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/siemens')

    def __str__(self):
        return self.title
class ACRetro(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/ac_retro')

    def __str__(self):
        return self.title
class MEMU(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/memu')

    def __str__(self):
        return self.title
class BTMEMU(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/bt_memu')

    def __str__(self):
        return self.title
class BTEMU(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/bt_emu')

    def __str__(self):
        return self.title
class Medha(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/medha')

    def __str__(self):
        return self.title
class CBHEL(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/data_book/cbhel_emu')

    def __str__(self):
        return self.title

# Timetable

class MainlineUP(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/Timetable/mainline_up')

    def __str__(self):
        return self.title
class MainlineDOWN(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/Timetable/mainline_down')

    def __str__(self):
        return self.title
class HBUP(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/Timetable/hb_up')

    def __str__(self):
        return self.title
class HBDOWN(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/Timetable/hb_down')

    def __str__(self):
        return self.title
class THBUP(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/Timetable/thb_up')

    def __str__(self):
        return self.title
class THBDOWN(models.Model):
    title = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    pdf = models.FileField(upload_to= 'pdfs/Timetable/thb_down')

    def __str__(self):
        return self.title




RAKETYPES_SIEMENS = 'S1'
RAKETYPES_MEMU = 'M1'
RAKETYPES_BTMEMU = 'BTM1'
RAKETYPES_ACRETRO = 'R1'

RAKETYPES_CHOICES = [
    (RAKETYPES_SIEMENS, 'SIEMENS'),
    (RAKETYPES_MEMU, 'MEMU'),
    (RAKETYPES_BTMEMU, 'BTMEMU'),
    (RAKETYPES_ACRETRO, 'ACRETRO'),
]

SCHEDULE_DONE_AFTER_KCS = 'KCS'
SCHEDULE_DONE_AFTER_SCS = 'SCS'
SCHEDULE_DONE_AFTER_NCS = 'NCS'
SCHEDULE_DONE_AFTER_PA = 'PA'

SCHEDULE_DONE_AFTER_CHOICES = [
    (SCHEDULE_DONE_AFTER_KCS, 'KCS'),
    (SCHEDULE_DONE_AFTER_SCS, 'SCS'),
    (SCHEDULE_DONE_AFTER_NCS, 'NCS'),
    (SCHEDULE_DONE_AFTER_PA, 'PA'),
]

SHIFT_MORNING = 'M'
SHIFT_NIGHT = 'N'
SHIFT_AFTERNOON = 'AF'

SHIFT_CHOICES = [
    (SHIFT_MORNING, 'MORNING'),
    (SHIFT_AFTERNOON, 'AFTERNOON'),
    (SHIFT_NIGHT, 'NIGHT'),
]

IA_1 = '1'
IA_2 = '2'
IA_3 = '3'
IA_4 = '4'
IA_5 = '5'
IA_6 = '6'
IA_7 = '7'
IA_8 = '8'
IA_9 = '9'
IA_10 = '10'
IA_11 = '11'
IA_12 = '12'

IA_CHOICES = [
    (IA_1, 'IA-1'),
    (IA_2, 'IA-2'),
    (IA_3, 'IA-3'),
    (IA_4, 'IA-4'),
    (IA_5, 'IA-5'),
    (IA_6, 'IA-6'),
    (IA_7, 'IA-7'),
    (IA_8, 'IA-8'),
    (IA_9, 'IA-9'),
    (IA_10, 'IA-10'),
    (IA_11, 'IA-11'),
    (IA_12, 'IA-12'),
]

TI_1 = '1'
TI_2 = '2'
TI_3 = '3'
TI_4 = '4'
TI_5 = '5'
TI_6 = '6'
TI_7 = '7'
TI_8 = '8'
TI_9 = '9'
TI_10 = '10'
TI_11 = '11'
TI_12 = '12'

TI_CHOICES = [
    (TI_1, 'TI-1'),
    (TI_2, 'TI-2'),
    (TI_3, 'TI-3'),
    (TI_4, 'TI-4'),
    (TI_5, 'TI-5'),
    (TI_6, 'TI-6'),
    (TI_7, 'TI-7'),
    (TI_8, 'TI-8'),
    (TI_9, 'TI-9'),
    (TI_10, 'TI-10'),
    (TI_11, 'TI-11'),
    (TI_12, 'TI-12'),
]

IC_SIEMENS_1 = '1'
IC_SIEMENS_2 = '2'
IC_SIEMENS_3 = '3'
IC_SIEMENS_4 = '4'

IC_SIEMENS_CHOICES = [
    (IC_SIEMENS_1, 'IC-1'),
    (IC_SIEMENS_2, 'IC-2'),
    (IC_SIEMENS_3, 'IC-3'),
    (IC_SIEMENS_4, 'IC-4'),
]

IC_QUATERLY_1 = '1'
IC_QUATERLY_2 = '2'
IC_QUATERLY_3 = '3'
IC_QUATERLY_4 = '4' 
IC_QUATERLY_CHOICES = [
    (IC_QUATERLY_1, 'IC-1'),
    (IC_QUATERLY_2, 'IC-2'),
    (IC_QUATERLY_3, 'IC-3'),
    (IC_QUATERLY_4, 'IC-4'),  
]

UST_1 = '1'
UST_2 = '2'
UST_3 = '3'
UST_CHOICES = [
    (UST_1, 'UST-1'),
    (UST_2, 'UST-2'),
    (UST_3, 'UST-3'),
]

COACH_POSITION_CHOICES = [
    ("1", "ONE"),
    ("2", "TWO"),
    ("3", "THREE"),
    ("4", "THREE"),
    ("5", "THREE"),
    ("6", "THREE"),
    ("7", "THREE"),
    ("8", "THREE"),
    ("9", "THREE"),   
]

RAKEID_CHOICES = [
    (RAKETYPES_SIEMENS, 'S1'),
    (RAKETYPES_MEMU, 'M1'),
    (RAKETYPES_BTMEMU, 'BTM1'),
    (RAKETYPES_ACRETRO, 'R1'),
]

MAKE_1 = '1'
MAKE_2 = '2'
MAKE_3 = '3'
MAKE_CHOICES = [
    (MAKE_1, 'RCF'),
    (MAKE_2, 'ICF'),
    (MAKE_3, 'BHEL'),
]



class ScheduleRake(models.Model):
    RAKETYPES_SIEMENS = 'S1'
    RAKETYPES_MEMU = 'M1'
    RAKETYPES_BTMEMU = 'BTM1'
    RAKETYPES_ACRETRO = 'R1'

    RAKETYPES_CHOICES = [
        (RAKETYPES_SIEMENS, 'SIEMENS'),
        (RAKETYPES_MEMU, 'MEMU'),
        (RAKETYPES_BTMEMU, 'BTMEMU'),
        (RAKETYPES_ACRETRO, 'ACRETRO'),
    ]

    SCHEDULE_DONE_AFTER_KCS = 'KCS'
    SCHEDULE_DONE_AFTER_SCS = 'SCS'
    SCHEDULE_DONE_AFTER_NCS = 'NCS'
    SCHEDULE_DONE_AFTER_PA = 'PA'

    SCHEDULE_DONE_AFTER_CHOICES = [
        (SCHEDULE_DONE_AFTER_KCS, 'KCS'),
        (SCHEDULE_DONE_AFTER_SCS, 'SCS'),
        (SCHEDULE_DONE_AFTER_NCS, 'NCS'),
        (SCHEDULE_DONE_AFTER_PA, 'PA'),
    ]

    SHIFT_MORNING = 'M'
    SHIFT_NIGHT = 'N'
    SHIFT_AFTERNOON = 'AF'

    SHIFT_CHOICES = [
        (SHIFT_MORNING, 'MORNING'),
        (SHIFT_AFTERNOON, 'AFTERNOON'),
        (SHIFT_NIGHT, 'NIGHT'),
    ]

    IA_1 = '1'
    IA_2 = '2'
    IA_3 = '3'
    IA_4 = '4'
    IA_5 = '5'
    IA_6 = '6'
    IA_7 = '7'
    IA_8 = '8'
    IA_9 = '9'
    IA_10 = '10'
    IA_11 = '11'
    IA_12 = '12'

    IA_CHOICES = [
        (IA_1, 'IA-1'),
        (IA_2, 'IA-2'),
        (IA_3, 'IA-3'),
        (IA_4, 'IA-4'),
        (IA_5, 'IA-5'),
        (IA_6, 'IA-6'),
        (IA_7, 'IA-7'),
        (IA_8, 'IA-8'),
        (IA_9, 'IA-9'),
        (IA_10, 'IA-10'),
        (IA_11, 'IA-11'),
        (IA_12, 'IA-12'),
    ]

    TI_1 = '1'
    TI_2 = '2'
    TI_3 = '3'
    TI_4 = '4'
    TI_5 = '5'
    TI_6 = '6'
    TI_7 = '7'
    TI_8 = '8'
    TI_9 = '9'
    TI_10 = '10'
    TI_11 = '11'
    TI_12 = '12'

    TI_CHOICES = [
        (TI_1, 'TI-1'),
        (TI_2, 'TI-2'),
        (TI_3, 'TI-3'),
        (TI_4, 'TI-4'),
        (TI_5, 'TI-5'),
        (TI_6, 'TI-6'),
        (TI_7, 'TI-7'),
        (TI_8, 'TI-8'),
        (TI_9, 'TI-9'),
        (TI_10, 'TI-10'),
        (TI_11, 'TI-11'),
        (TI_12, 'TI-12'),
    ]

    IC_SIEMENS_1 = '1'
    IC_SIEMENS_2 = '2'
    IC_SIEMENS_3 = '3'
    IC_SIEMENS_4 = '4'

    IC_SIEMENS_CHOICES = [
        (IC_SIEMENS_1, 'IC-1'),
        (IC_SIEMENS_2, 'IC-2'),
        (IC_SIEMENS_3, 'IC-3'),
        (IC_SIEMENS_4, 'IC-4'),
    ]

    IC_QUATERLY_1 = '1'
    IC_QUATERLY_2 = '2'
    IC_QUATERLY_3 = '3'
    IC_QUATERLY_4 = '4' 
    IC_QUATERLY_CHOICES = [
        (IC_QUATERLY_1, 'IC-1'),
        (IC_QUATERLY_2, 'IC-2'),
        (IC_QUATERLY_3, 'IC-3'),
        (IC_QUATERLY_4, 'IC-4'),  
    ]

    UST_1 = '1'
    UST_2 = '2'
    UST_3 = '3'
    UST_CHOICES = [
        (UST_1, 'UST-1'),
        (UST_2, 'UST-2'),
        (UST_3, 'UST-3'),
    ]

    rake_type = models.CharField(
        max_length=100, choices = RAKETYPES_CHOICES, default='S1')
    coach_position = models.IntegerField(max_length=100)
    be_dtc = models.IntegerField(max_length=4)
    ke_dtc = models.IntegerField(max_length=4)
    unit_no = models.IntegerField(max_length=500)
    datetime = models.DateField(max_length=224)
    schedule_at = models.CharField(
        max_length=4, choices= SCHEDULE_DONE_AFTER_CHOICES)
    shift = models.CharField(
        max_length=4, choices=SHIFT_CHOICES)
    ia = models.CharField(
        max_length=100, choices=IA_CHOICES, default='1')
    ic_quaterly = models.CharField(
        max_length=4, choices= IC_QUATERLY_CHOICES)
    ust = models.CharField(
        max_length=1, choices=UST_CHOICES, default='1')
    servicer_after = models.CharField(max_length=224)
    washing = models.DateTimeField(max_length=224)
    mopping = models.DateTimeField(max_length=224)
    ti = models.CharField(max_length=100, choices=TI_CHOICES, default='1')
    pdf = models.FileField(upload_to= 'pdfs/rake_master')

    def __str__(self):
        return self.rake_type

    
class NewRake(models.Model):
    RAKETYPES_SIEMENS = 'S1'
    RAKETYPES_MEMU = 'M1'
    RAKETYPES_BTMEMU = 'BTM1'
    RAKETYPES_ACRETRO = 'R1'

    RAKETYPES_CHOICES = [
        (RAKETYPES_SIEMENS, 'SIEMENS'),
        (RAKETYPES_MEMU, 'MEMU'),
        (RAKETYPES_BTMEMU, 'BTMEMU'),
        (RAKETYPES_ACRETRO, 'ACRETRO'),
    ]
    RAKEID_CHOICES = [
        (RAKETYPES_SIEMENS, 'S1'),
        (RAKETYPES_MEMU, 'M1'),
        (RAKETYPES_BTMEMU, 'BTM1'),
        (RAKETYPES_ACRETRO, 'R1'),
    ]
    COACH_POSITION_CHOICES = [
        ("1", "ONE"),
        ("2", "TWO"),
        ("3", "THREE"),
        ("4", "THREE"),
        ("5", "THREE"),
        ("6", "THREE"),
        ("7", "THREE"),
        ("8", "THREE"),
        ("9", "THREE"),
        
    ]
    MAKE_1 = '1'
    MAKE_2 = '2'
    MAKE_3 = '3'
    MAKE_CHOICES = [
        (MAKE_1, 'RCF'),
        (MAKE_2, 'ICF'),
        (MAKE_3, 'BHEL'),
    ]

    rake_type = models.CharField(
        max_length=100, choices = RAKETYPES_CHOICES, default='S1')
    coach_position = models.IntegerField(max_length=100)
    unit_no = models.BigIntegerField(max_length=500)
    rake_id = models.CharField(max_length=100, choices=RAKEID_CHOICES)
    make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    coach_no = models.IntegerField(max_length=100)
    comm_date = models.DateTimeField(max_length=100)

    def __str__(self):
        return self.rake_type

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class EMEMO(models.Model):
    unit_no = models.BigIntegerField(max_length=500)
    coach_no = models.IntegerField(max_length=100)
    line_no = models.IntegerField(max_length=100)
    rake_formation = models.BigIntegerField(max_length=224)
    poh = models.DateField(blank=True, null= True)
    IA = models.DateField(blank=True, null= True)
    TI = models.DateField(blank=True ,null= True)
    W = models.DateField(blank=True, null= True)
    M = models.DateField(blank=True, null= True)
    IC = models.DateField(blank=True, null= True)
    UST = models.DateField(blank=True, null= True)
    defects_reported = models.CharField(max_length=224)
    train_no = models.IntegerField(max_length=224)
    report_by = models.CharField(max_length=224)
    nature_of_defects = models.CharField(max_length=224)
    repercussion = models.CharField(max_length=224)
    place_of_failure = models.CharField(max_length=224)
    failure_report = models.TextField(max_length=224)
    report_signee = models.CharField(max_length=224, null=True, default = None)
    investigation = models.TextField(max_length=224, blank=True)
    image = models.ImageField(upload_to = 'pdfs/ememo/', blank=True)
    investigation_signee = models.CharField(max_length=224, null=True, default = None)
    remarks = models.TextField(max_length=224)
    
class SiemensData(models.Model):

    RAKETYPES_SIEMENS = 'S1'
    RAKETYPES_MEMU = 'M1'
    RAKETYPES_BTMEMU = 'BTM1'
    RAKETYPES_ACRETRO = 'R1'

    RAKETYPES_CHOICES = [
        (RAKETYPES_SIEMENS, 'SIEMENS'),
        (RAKETYPES_MEMU, 'MEMU'),
        (RAKETYPES_BTMEMU, 'BTMEMU'),
        (RAKETYPES_ACRETRO, 'ACRETRO'),
    ]
    RAKEID_CHOICES = [
        (RAKETYPES_SIEMENS, 'S1'),
        (RAKETYPES_MEMU, 'M1'),
        (RAKETYPES_BTMEMU, 'BTM1'),
        (RAKETYPES_ACRETRO, 'R1'),
    ]

    MAKE_1 = '1'
    MAKE_2 = '2'
    MAKE_3 = '3'
    MAKE_CHOICES = [
        (MAKE_1, 'RCF'),
        (MAKE_2, 'ICF'),
        (MAKE_3, 'BHEL'),
    ]


    Rake_ID = models.CharField(max_length=10, choices=RAKEID_CHOICES, default='S1')
    Rake_Type = models.CharField(
        max_length=100, choices=RAKETYPES_CHOICES, default='S1')
    Coach_Position = models.IntegerField()
    Coach_No = models.CharField(max_length=100)
    Unit_No = models.SlugField(max_length=500)
    Make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    Coach_Type = models.CharField(max_length=100)
    Comm_Date = models.DateField(max_length=100)
    Age_in_Yrs = models.FloatField(max_length=10)
    Life_Left = models.FloatField(max_length=10)
    Coach_Condemn_Date = models.DateField(max_length=100)
    Latest_POH_Date = models.DateField(max_length=100)
    EIS_after_POH_Date = models.DateField(max_length=100)
    POH_over_Due = models.DateField(max_length=100)

    def __str__(self):
        return self.Rake_Type
     
class MemuRCF(models.Model):

    RAKETYPES_SIEMENS = 'S1'
    RAKETYPES_MEMU = 'M1'
    RAKETYPES_BTMEMU = 'BTM1'
    RAKETYPES_ACRETRO = 'R1'

    RAKETYPES_CHOICES = [
        (RAKETYPES_SIEMENS, 'SIEMENS'),
        (RAKETYPES_MEMU, 'MEMU'),
        (RAKETYPES_BTMEMU, 'BTMEMU'),
        (RAKETYPES_ACRETRO, 'ACRETRO'),
    ]
    RAKEID_CHOICES = [
        (RAKETYPES_SIEMENS, 'S1'),
        (RAKETYPES_MEMU, 'M1'),
        (RAKETYPES_BTMEMU, 'BTM1'),
        (RAKETYPES_ACRETRO, 'R1'),
    ]

    MAKE_1 = '1'
    MAKE_2 = '2'
    MAKE_3 = '3'
    MAKE_CHOICES = [
        (MAKE_1, 'RCF'),
        (MAKE_2, 'ICF'),
        (MAKE_3, 'BHEL'),
    ]


    Rake_ID = models.CharField(max_length=10, choices=RAKEID_CHOICES, default='M1')
    Rake_Type = models.CharField(
        max_length=100, choices=RAKETYPES_CHOICES, default='M1')
    Coach_Position = models.IntegerField()
    Coach_No = models.CharField(max_length=100)
    Unit_No = models.SlugField(max_length=500)
    Make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    Coach_Type = models.CharField(max_length=100)
    Comm_Date = models.DateField(max_length=100)
    Age_in_Yrs = models.FloatField(max_length=10)
    Life_Left = models.FloatField(max_length=10)
    Coach_Condemn_Date = models.DateField(max_length=100)
    Latest_POH_Date = models.DateField(max_length=100)
    EIS_after_POH_Date = models.DateField(max_length=100)
    POH_over_Due = models.DateField(max_length=100)

    def __str__(self):
        return self.Rake_Type

class MemuBT(models.Model):

    RAKETYPES_SIEMENS = 'S1'
    RAKETYPES_MEMU = 'M1'
    RAKETYPES_BTMEMU = 'BTM1'
    RAKETYPES_ACRETRO = 'R1'

    RAKETYPES_CHOICES = [
        (RAKETYPES_SIEMENS, 'SIEMENS'),
        (RAKETYPES_MEMU, 'MEMU'),
        (RAKETYPES_BTMEMU, 'BTMEMU'),
        (RAKETYPES_ACRETRO, 'ACRETRO'),
    ]
    RAKEID_CHOICES = [
        (RAKETYPES_SIEMENS, 'S1'),
        (RAKETYPES_MEMU, 'M1'),
        (RAKETYPES_BTMEMU, 'BTM1'),
        (RAKETYPES_ACRETRO, 'R1'),
    ]

    MAKE_1 = '1'
    MAKE_2 = '2'
    MAKE_3 = '3'
    MAKE_CHOICES = [
        (MAKE_1, 'RCF'),
        (MAKE_2, 'ICF'),
        (MAKE_3, 'BHEL'),
    ]


    Rake_ID = models.CharField(max_length=10, choices=RAKEID_CHOICES, default='BTM1')
    Rake_Type = models.CharField(
        max_length=100, choices=RAKETYPES_CHOICES, default='BTM1')
    Coach_Position = models.IntegerField()
    Coach_No = models.CharField(max_length=100)
    Unit_No = models.SlugField(max_length=500)
    Make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    Coach_Type = models.CharField(max_length=100)
    Comm_Date = models.DateField(max_length=100)
    Age_in_Yrs = models.FloatField(max_length=10)
    Life_Left = models.FloatField(max_length=10)
    Coach_Condemn_Date = models.DateField(max_length=100)
    Latest_POH_Date = models.DateField(max_length=100)
    EIS_after_POH_Date = models.DateField(max_length=100)
    POH_over_Due = models.DateField(max_length=100)

    def __str__(self):
        return self.Rake_Type
      
class AcretroData(models.Model):

    RAKETYPES_SIEMENS = 'S1'
    RAKETYPES_MEMU = 'M1'
    RAKETYPES_BTMEMU = 'BTM1'
    RAKETYPES_ACRETRO = 'R1'

    RAKETYPES_CHOICES = [
        (RAKETYPES_SIEMENS, 'SIEMENS'),
        (RAKETYPES_MEMU, 'MEMU'),
        (RAKETYPES_BTMEMU, 'BTMEMU'),
        (RAKETYPES_ACRETRO, 'ACRETRO'),
    ]
    RAKEID_CHOICES = [
        (RAKETYPES_SIEMENS, 'S1'),
        (RAKETYPES_MEMU, 'M1'),
        (RAKETYPES_BTMEMU, 'BTM1'),
        (RAKETYPES_ACRETRO, 'R1'),
    ]

    MAKE_1 = '1'
    MAKE_2 = '2'
    MAKE_3 = '3'
    MAKE_CHOICES = [
        (MAKE_1, 'RCF'),
        (MAKE_2, 'ICF'),
        (MAKE_3, 'BHEL'),
    ]


    Rake_ID = models.CharField(max_length=10, choices=RAKEID_CHOICES, default='R1')
    Rake_Type = models.CharField(
        max_length=100, choices=RAKETYPES_CHOICES, default='R1')
    Coach_Position = models.IntegerField()
    Coach_No = models.CharField(max_length=100)
    Unit_No = models.SlugField(max_length=500)
    Make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    Coach_Type = models.CharField(max_length=100)
    Comm_Date = models.DateField(max_length=100)
    Age_in_Yrs = models.FloatField(max_length=10)
    Life_Left = models.FloatField(max_length=10)
    Coach_Condemn_Date = models.DateField(max_length=100)
    Latest_POH_Date = models.DateField(max_length=100)
    EIS_after_POH_Date = models.DateField(max_length=100)
    POH_over_Due = models.DateField(max_length=100)

    def __str__(self):
        return self.Rake_Type
