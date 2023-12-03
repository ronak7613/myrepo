from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import datetime

class sd(models.Model):
    si = models.CharField(max_length=50,default="")
    sr = models.CharField(max_length=50,default="")
    person_id = models.CharField(max_length=200,default="")
    Time = models.DateTimeField()
    off_Time = models.DateTimeField()
    ip= models.CharField(max_length=200,default="")
    Activity = models.CharField(max_length=200,default="Tap Tyag MM")
    First_Name = models.CharField(max_length=200,default="")
    Husband_Father_Name = models.CharField(max_length=200,default="")
    Surname = models.CharField(max_length=200,default="")
    Srimad_dasvekalik_RegistrationID_1 = models.CharField(max_length=200,default="")
    Srimad_dasvekalik_RegistrationID_2 = models.CharField(max_length=200,default="")
    full_name=models.CharField(max_length=200,default="")
    #Gender = models.CharField(max_length=200,default="")
    Age = models.IntegerField(default=0)
    Country = models.CharField(max_length=200,default="")
    Transalate = models.CharField(max_length=200,default="")
    Pincode = models.CharField(max_length=10)
    India_Whatsapp_No = models.CharField(max_length=30)
    Foreign_WhatsappNo = models.CharField(max_length=30, blank=True)
    Pincode_FR = models.CharField(max_length=10, blank=True)
    Sub_Region = models.CharField(max_length=200,default="")
    zila= models.CharField(max_length=200,default="")
    State = models.CharField(max_length=200,default="")
    Region = models.CharField(max_length=200,default="")    
    address = models.CharField(max_length=200,default="")
    C1 = models.CharField(max_length=200,default="")
    C2 = models.CharField(max_length=200,default="")
    C3 = models.CharField(max_length=100,default="")
    C4 = models.CharField(max_length=100,default="")
    C5 = models.CharField(max_length=100,default="")
    C6 = models.CharField(max_length=100,default="")
    # C7 = models.CharField(max_length=100,default="")
    # C8 = models.CharField(max_length=100,default="")
    # C9 = models.CharField(max_length=100,default="")
    C10 = models.CharField(max_length=100,default="")
    A1 = models.CharField(max_length=100,default="")
    A2 = models.CharField(max_length=100,default="")
    A3 = models.CharField(max_length=100,default="")
    A4 = models.CharField(max_length=100,default="")
    A5 = models.CharField(max_length=100,default="")
    A6 = models.CharField(max_length=100,default="")
    A7 = models.CharField(max_length=100,default="")
    A8 = models.CharField(max_length=100,default="")
    A9 = models.CharField(max_length=100,default="")
    # A10 = models.CharField(max_length=100,default="")
    # A11 = models.CharField(max_length=100,default="")
    # A12 = models.CharField(max_length=100,default="")
    # A13 = models.CharField(max_length=100,default="")
    # A14 = models.CharField(max_length=100,default="")    
    #score = models.IntegerField(default=0)

    def __str__(self):
        return f"Region: {self.Region} - Activity: {self.Activity} - Sub_Region: {self.Sub_Region} - A1: {self.A1} - A2: {self.A2} -A3: {self.A3} -A4: {self.A4} -A5: {self.A5} -A6: {self.A6} -A7: {self.A7} -A8: {self.A8} -A9: {self.A9} - Date: {self.Time}"
    
    



class table_TapTyag(models.Model):
    
    sr1 = models.CharField(max_length=50,default="")
    sr2 = models.CharField(max_length=50,default="")
    person_id = models.CharField(max_length=200,default="")
    Time = models.DateTimeField()
    off_Time = models.DateTimeField()
    ip= models.CharField(max_length=200,default="")
    Activity = models.CharField(max_length=200,default="Tap Tyag MM")
    First_Name = models.CharField(max_length=200,default="")
    Husband_Father_Name = models.CharField(max_length=200,default="")
    Surname = models.CharField(max_length=200,default="")
    full_name=models.CharField(max_length=200,default="")
    Gender = models.CharField(max_length=200,default="")
    Age = models.IntegerField(default=0)
    Country = models.CharField(max_length=200,default="")
    Pincode = models.CharField(max_length=10)
    India_Whatsapp_No = models.CharField(max_length=30)
    Foreign_WhatsappNo = models.CharField(max_length=30, blank=True)
    Pincode_FR = models.CharField(max_length=10, blank=True)
    Sub_Region = models.CharField(max_length=200,default="")
    State = models.CharField(max_length=200,default="")
    Region = models.CharField(max_length=200,default="")
    A1 = models.CharField(max_length=200,default="")
    which_ladi = models.CharField(max_length=200,default="")
    ekasan= models.CharField(max_length=200,default="")
    upvas = models.CharField(max_length=200,default="")
    alymbit = models.CharField(max_length=200,default="")
    tela = models.CharField(max_length=200,default="")
    A2 = models.CharField(max_length=200,default="")
    A3 = models.CharField(max_length=100,default="")
    A4 = models.CharField(max_length=100,default="")
    A5 = models.CharField(max_length=100,default="")
    A6 = models.CharField(max_length=100,default="")
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Region: {self.Region} - Activity: {self.Activity} - Sub_Region: {self.Sub_Region} - A1: {self.A1} - A2: {self.A2} -A3: {self.A3} -A4: {self.A4} -A5: {self.A5} -A6: {self.A6} - Date: {self.Time}"



class table_Swadhyay(models.Model):
    si = models.CharField(max_length=50,default="")
    sr = models.CharField(max_length=50,default="")
    person_id = models.CharField(max_length=200,default="")
    Time = models.DateTimeField(blank=True,default=datetime.datetime(1, 1, 1, 0, 0))
    off_Time = models.DateTimeField(blank=True,default=datetime.datetime(1, 1, 1, 0, 0))
    ip= models.CharField(max_length=200,default="")
    Activity = models.CharField(max_length=200,default="Tap Tyag MM")
    First_Name = models.CharField(max_length=200,default="")
    Husband_Father_Name = models.CharField(max_length=200,default="")
    Surname = models.CharField(max_length=200,default="")
    Srimad_dasvekalik_RegistrationID_1 = models.CharField(max_length=200,default="")
    Srimad_dasvekalik_RegistrationID_2 = models.CharField(max_length=200,default="")
    full_name=models.CharField(max_length=200,default="")
    #Gender = models.CharField(max_length=200,default="")
    Age = models.IntegerField(default=0)
    Country = models.CharField(max_length=200,default="")
    Transalate = models.CharField(max_length=200,default="")
    Pincode = models.CharField(max_length=10)
    India_Whatsapp_No = models.CharField(max_length=30)
    Foreign_WhatsappNo = models.CharField(max_length=30, blank=True)
    Pincode_FR = models.CharField(max_length=10, blank=True)
    Sub_Region = models.CharField(max_length=200,default="")
    zila= models.CharField(max_length=200,default="")
    State = models.CharField(max_length=200,default="")
    Region = models.CharField(max_length=200,default="")    
    #address = models.CharField(max_length=200,default="")
    C1 = models.CharField(max_length=200,default="")
    C2 = models.CharField(max_length=200,default="")
    C3 = models.CharField(max_length=100,default="")
    C4 = models.CharField(max_length=100,default="")
    C5 = models.CharField(max_length=100,default="")
    C6 = models.CharField(max_length=100,default="")
    # C7 = models.CharField(max_length=100,default="")
    # C8 = models.CharField(max_length=100,default="")
    # C9 = models.CharField(max_length=100,default="")
    C10 = models.CharField(max_length=100,default="")
    A1 = models.CharField(max_length=100,default="")
    A2 = models.CharField(max_length=100,default="")
    A3 = models.CharField(max_length=100,default="")
    A4 = models.CharField(max_length=100,default="")
    A5 = models.CharField(max_length=100,default="")
    A6 = models.CharField(max_length=100,default="")
    A7 = models.CharField(max_length=100,default="")
    A8 = models.CharField(max_length=100,default="")
    A9 = models.CharField(max_length=100,default="")
    # A10 = models.CharField(max_length=100,default="")
    # A11 = models.CharField(max_length=100,default="")
    # A12 = models.CharField(max_length=100,default="")
    # A13 = models.CharField(max_length=100,default="")
    # A14 = models.CharField(max_length=100,default="")    
    #score = models.IntegerField(default=0)

    def __str__(self):
        return f"Region: {self.Region} - Activity: {self.Activity} - Sub_Region: {self.Sub_Region} - A1: {self.A1} - A2: {self.A2} -A3: {self.A3} -A4: {self.A4} -A5: {self.A5} -A6: {self.A6} -A7: {self.A7} -A8: {self.A8} -A9: {self.A9} - Date: {self.Time}"
        #return f"Region: {self.Region} - Activity: {self.Activity} - Sub_Region: {self.Sub_Region} - A1: {self.A1} - A2: {self.A2} -A3: {self.A3} -A4: {self.A4} -A5: {self.A5} -A6: {self.A6} -A7: {self.A7} -A8: {self.A8} -A9: {self.A9} -A10: {self.A10} -A11: {self.A11} -A12: {self.A12} -A13: {self.A13} -A14: {self.A14} - Date: {self.Time}"


#---------------------------------old model---------------
# sr = models.IntegerField(default=0)
#     person_id = models.CharField(max_length=200,default="")
#     Time = models.DateTimeField()
#     off_Time = models.DateTimeField()
#     Activity = models.CharField(max_length=200,default="")
#     First_Name = models.CharField(max_length=200,default="")
#     Husband_Father_Name = models.CharField(max_length=200,default="")
#     Surname = models.CharField(max_length=200,default="")
#     Gender = models.CharField(max_length=200,default="")
#     Age = models.IntegerField(default=0)
#     Country = models.CharField(max_length=200,default="")
#     India_Whatsapp_No = models.CharField(max_length=30)
#     Pincode = models.CharField(max_length=10)
#     Foreign_WhatsappNo = models.CharField(max_length=30, blank=True)
#     Pincode_FR = models.CharField(max_length=10, blank=True)
#     Sub_Region = models.CharField(max_length=200,default="")
#     State = models.CharField(max_length=200,default="")
#     Region = models.CharField(max_length=200,default="")
#     A1 = models.CharField(max_length=200,default="")
#     which_ladi = models.CharField(max_length=200,default="")
#     A2 = models.CharField(max_length=200,default="")
#     A3 = models.CharField(max_length=100,default="")
#     A4 = models.CharField(max_length=100,default="")
#     a5 = models.CharField(max_length=100,default="")
#     a6 = models.CharField(max_length=100,default="")
#     score = models.IntegerField(default=0)
#----------------------------------------------------

# class table_Gyanarjan(models.Model):
#     sr	प्रत्युत्तर ID	प्रत्युत्तर प्रारंभ	प्रत्युत्तर पूर्ण	IP पता	संग्राहक का नाम	पहला नाम / First Name	पिता / पति का नाम /  Husband / Father Name	सरनेम / Surname	उम्र / Age 	लिंग 	देश - Country	व्हाट्सअप नंबर	पिनकोड - Pincode	मोबाइल नंबर - विदेश - Foreign_Whatsapp No	Pincode_FR	शहर/ गांव  	जिला	State / राज्य 	Anchal / अंचल 	Adress	प्रकल्प चुनिए	A1	A2	A3	क्या आप  श्रुत आरोहक  प्रकल्प से जुड़ना चाहते हैं  नोट_ 3 वर्षीय पाठ्यक्रम	All Is Well - प्रतिक्रमणक्या आप All is Well - प्रतिक्रमण प्रकल्प से जुड़ना चाहते हैं _ नोट_  इसमें 18 वर्ष से लेकर 45 वर्ष के युवा ही भाग ले सकते हैं	All Is Well - प्रतिक्रमण प्रतिक्रमण कंठस्थ करके गुरु चरणों में भेंट देने के लिए संकल्पित हूँ	क्या आप वर्तमान में आगमों का वांचन कर रहे हैं_ एवम् कौन से आगम	क्या आप श्रुत रमण _22 आगमों के अर्थ का वांचन _ प्रकल्प से जुड़ना चाहते हैं	क्या आपको आगमों की आवश्यकता है	क्या आप  श्रुत भ्रमण _घर बैठे ओपन बुक परीक्षा _  प्रकल्प से जुड़ना चाहते हैं  इस परीक्षा में जिणधम्मो _साधु धर्म _ श्रावक धर्म कोर्स  आयेगा	श्रीमद् अंतगड़दसाओं सूत्र की पुस्तक आपको चाहिए	क्या आप थोकडो का कार्निवल_20 थोकडे का अध्ययन_ प्रकल्प से जुड़ना चाहते हैं?	कर्मा क्विज़	स्कोर 

#     sr = models.IntegerField(default=0)
#     person_id = models.CharField(max_length=200,default="")
#     Time = models.DateTimeField()
#     off_Time = models.DateTimeField()
#     Activity = models.CharField(max_length=200,default="")
#     First_Name = models.CharField(max_length=200,default="")
#     Husband_Father_Name = models.CharField(max_length=200,default="")
#     Surname = models.CharField(max_length=200,default="")
#     Gender = models.CharField(max_length=200,default="")
#     Age = models.IntegerField(default=0)
#     Country = models.CharField(max_length=200,default="")
#     India_Whatsapp_No = models.CharField(max_length=30)
#     Pincode = models.CharField(max_length=10)
#     Foreign_WhatsappNo = models.CharField(max_length=30, blank=True)
#     Pincode_FR = models.CharField(max_length=10, blank=True)
#     Sub_Region = models.CharField(max_length=200,default="")
#     State = models.CharField(max_length=200,default="")
#     Region = models.CharField(max_length=200,default="")
#     A1 = models.CharField(max_length=200,default="")
#     which_ladi = models.CharField(max_length=200,default="")
#     A2 = models.CharField(max_length=200,default="")
#     A3 = models.CharField(max_length=100,default="")
#     A4 = models.CharField(max_length=100,default="")
#     a5 = models.CharField(max_length=100,default="")
#     a6 = models.CharField(max_length=100,default="")
#     score = models.IntegerField(default=0)

#     def __str__(self):
#         return f"Region: {self.Region} - Activity: {self.Activity} - Sub_Region: {self.Sub_Region} - A2: {self.A2} - A1: {self.A1} - Date: {self.Time}"

# class table_TapTyag(models.Model):
#     sr=models.IntegerField()
#     ID=models.CharField( max_length=200)
#     Time=models.DateField()
#     off_Time=models.DateField()
#     Activity=models.CharField( max_length=200)
#     पहला_नाम_First_Name=models.CharField( max_length=200)
#     पिता_पति_का_नाम_Husband_Father_Name=models.CharField( max_length=200)
#     सरनेम_Surname=models.CharField( max_length=200)
#     लिंग_Gender=models.CharField( max_length=200)
#     उम्र_Age=models.IntegerField()
#     देश_Country=models.CharField( max_length=200)
#     मोबाइल_नंबर_भारत_India_Whatsapp_No=models.CharField( max_length=200)
#     Pincode=models.CharField(max_length=10)
#     मोबाइल_नंबर_विदेश_Foreign_WhatsappNo=models.CharField( max_length=200)
#     Pincode_FR=models.CharField(max_length=10)
#     Sub_Region=models.CharField( max_length=200)
#     State_राज्य=models.CharField( max_length=200)
#     Region=models.CharField( max_length=200)
#     A1=models.CharField( max_length=200)
#     इनमे_से_किस_लड़ी_में_भाग_लेंगे=models.CharField( max_length=200)
#     A2=models.CharField( max_length=200)
#     आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_प्रतिदिन_1_घंटा_मौन_आराधना_करेंगे=models.CharField(max_length=100)
#     आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_प्रतिमाह_4_रात्रि_चौविहार_प्रत्याख्यान_सूर्यास्त_से_अगले_दिन_तक_नवकारसी_पक्की_नवकारसी_कर_जीवो_को_अभय_दान_देंगे=models.CharField(max_length=100)
#     आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_50_दिन_पूर्ण_सूर्य_अस्त_से_सूर्य_उदय_संवर_पौषध_पूर्ण_दया_करेंगे=models.CharField(max_length=100)
#     आप_महत्तम_महोत्सव_में_फरवरी_2025_तक_दूध_दही_घी_तेल_मीठा_में_से_किसी_भी_एक_विगय_का_प्रतिदिन_त्याग_करेंगे=models.CharField(max_length=100)
#     स्कोर = models.FloatField()

# class subactivity(models.Model):
#     TapTyag_MM = models.CharField(max_length=100)
#     Gyanarjan_MM = models.CharField(max_length=100)

class subregion(models.Model):
    jaipur =models.CharField(max_length=100)
    ajmer = models.CharField(max_length=100)
    bhilwara =models.CharField(max_length=100)
    International = models.CharField(max_length=100)
    karnataka = models.CharField(max_length=100)
    mumbai = models.CharField(max_length=100)
    jhunjhunun = models.CharField(max_length=100)


class Data(models.Model):
    Date = models.DateField()
    Activity = models.CharField(max_length=100)
    Region = models.CharField(max_length=100)
    Sub_Region = models.CharField(max_length=100)
    Full_name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Whatsapp_India = models.CharField(max_length=15)
    Pincode = models.CharField(max_length=10)
    Village = models.CharField(max_length=100)
    SUB_ACTIVITY1 = models.CharField(max_length=100)
    SA2 = models.CharField(max_length=100)
    SA3 = models.CharField(max_length=100)
    SA4 = models.CharField(max_length=100)

    def __str__(self):
        return f"Region: {self.Region} - Activity: {self.Activity} - Sub_Region: {self.Sub_Region} - SA2: {self.SA2} - SA3: {self.SA3} - SA4: {self.SA4} - Date: {self.Date}"






from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class myUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class myUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Add your custom fields here
    is_admin = models.BooleanField(default=False)
    is_regional_head = models.BooleanField(default=False)
    is_activity_head = models.BooleanField(default=False)
    is_sub_regional_head = models.BooleanField(default=False)
    region = models.CharField(max_length=100, blank=True)
    activity = models.CharField(max_length=100, blank=True)
    sub_region = models.CharField(max_length=100, blank=True)

    objects = myUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
        
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     is_admin = models.BooleanField(default=False)
#     is_regional_head = models.BooleanField(default=False)
#     is_activity_head = models.BooleanField(default=False)
#     is_sub_regional_head = models.BooleanField(default=False)
##     region = models.CharField(max_length=100, blank=True)
#     activity = models.CharField(max_length=100, blank=True)
#     sub_region = models.CharField(max_length=100, blank=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
    
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_users',
#         blank=True,
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_users',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Specific permissions for this user.',
#     )

#     def __str__(self):
#         return self.username


# from django.db import models


# class Data(models.Model):
#     Date = models.DateField()
#     Activity = models.CharField(max_length=100)
#     Region = models.CharField(max_length=100)
#     Sub_Region = models.CharField(max_length=100)
#     Full_name = models.CharField(max_length=100)
#     Age = models.IntegerField()
#     Gender = models.CharField(max_length=10)
#     Whatsapp_India = models.CharField(max_length=15)
#     Pincode = models.CharField(max_length=10)
#     Village = models.CharField(max_length=100)
#     SUB_ACTIVITY1 = models.CharField(max_length=100)
#     SA2 = models.CharField(max_length=100)
#     SA3 = models.CharField(max_length=100)
#     SA4 = models.CharField(max_length=100)




# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
        
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     is_admin = models.BooleanField(default=False)
#     is_regional_head = models.BooleanField(default=False)
#     is_activity_head = models.BooleanField(default=False)
#     is_sub_regional_head = models.BooleanField(default=False)

##     region = models.CharField(max_length=100, blank=True)
#     activity = models.CharField(max_length=100, blank=True)
#     sub_region = models.CharField(max_length=100, blank=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     # Add related_name to avoid conflicts
#     groups_rel = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',
#         blank=True,
#         verbose_name='groups',
#     )
#     user_permissions_rel = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Specific permissions for this user.',
#     )

#     def __str__(self):
#         return self.username
