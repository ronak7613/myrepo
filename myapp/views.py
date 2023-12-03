from django.shortcuts import render
import pandas as pd
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import requests
from django.http import JsonResponse
from django.contrib.staticfiles import finders
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from myapp.forms import CustomUserCreationForm

from django.views.generic.edit import CreateView
from myapp.forms import CustomUserCreationForm  # Adjust import as needed
from django.contrib.auth.forms import AuthenticationForm

def newhome(request):
    return render(request,'test.html')



from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Additional actions on successful form submission if needed
        return response

    def form_invalid(self, form):
        # Handle invalid form submission
        return self.render_to_response(self.get_context_data(form=form, error='Invalid username or password'))

    def get(self, request, *args, **kwargs):
        # Render the form with an error message if provided in the URL
        error = request.GET.get('error', None)
        return self.render_to_response(self.get_context_data(error=error))

    def get_success_url(self):
        # Specify the URL to redirect to upon successful login
        # Adjust this based on your application's requirements
        return reverse_lazy('home')  # Redirect to the home page or a different URL as needed

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_active:
            return self.form_valid(self.get_form())
        else:
            messages.error(request, "Invalid credentials")
            return self.form_invalid(self.get_form())


class CustomLogoutView(LogoutView):
    next_page = '/'


class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        # Handle invalid form submission
        return self.render_to_response(self.get_context_data(form=form, error='Invalid form submission'))

    def form_valid(self, form):
        response = super().form_valid(form)
        # Additional actions on successful form submission if needed
        return response

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout  

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Validate input data if needed

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect the user to an appropriate page after a successful login
            # Example: Redirect to the user's profile page
            return redirect("/")  # Replace 'profile' with your desired URL name

        else:
            # Provide a more specific error message
            messages.info(request,'invalid credentials')
            return redirect('login')

    # Render the login form
    return render(request, 'login.html')

# from .models import CustomUser  

# def login(request):
     
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         try:
#             user = CustomUser.objects.get(username=username)            
            
#             if user.password == password:
#                  # Authentication successful
#                  messages.success(request, "Login successful")
#                  # TODO: Perform any additional actions after successful login
#                  return redirect('/')
                
#             else:
#                 print(user.check_password(password))
#                 messages.error(request, "Invalid credentials")
#         except CustomUser.DoesNotExist:
#             messages.error(request, "Invalid")
        
#         return redirect('login')
    
#     else:
    
#         return render(request, 'login.html')
# from django.contrib import messages, auth
# from django.shortcuts import render, redirect
# from .models import CustomUser

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         try:
#             user = CustomUser.objects.get(username=username)
#         except CustomUser.DoesNotExist:
#             user = None

#         if user is not None and user.check_password(password):
#                 print(f"Username: {username}, Password: {password}")
#                 auth.login(request, user)
#                 messages.success(request, "Login successful")
#                 return redirect('/')
#         else:
#                 print(f"Invalid login attempt - Username: {username}, Password: {password}")
#                 messages.error(request, "Invalid credentials")

#     return render(request, 'login.html')


def custom_logout(request):
    logout(request)  
    return redirect('login')



from django.shortcuts import render
from .models import table_TapTyag,table_Swadhyay
from django.utils import timezone
from datetime import datetime
from django.db.models import Q


def filtered_table(request):
    filter_start_date = request.GET.get('start_date', '')
    filter_end_date = request.GET.get('end_date', '')
    filter_region = request.GET.get('filterregion', '')
    filter_activity = request.GET.get('filteractivity', '')
    filter_subactivity = request.GET.getlist('filtersubactivity', [])
    filter_subregion = request.GET.get('filtersubregion', '')

    # Filter data based on the filter parameters
    if(filter_activity == "Tap Tyag MM"):
        filtered_data_TapTyag = table_TapTyag.objects.all()

        # Convert filter_start_date and filter_end_date to datetime objects
        if filter_start_date:
            filter_start_date = datetime.strptime(filter_start_date, "%Y-%m-%d").date()
        if filter_end_date:
            filter_end_date = datetime.strptime(filter_end_date, "%Y-%m-%d").date()

        # Filter based on start and end date
        if filter_start_date:
            filtered_data_TapTyag = filtered_data_TapTyag.filter(Time__gte=filter_start_date)
        if filter_end_date:
            # Add one day to filter_end_date to include that day as well
            filter_end_date = filter_end_date + timezone.timedelta(days=1)
            filtered_data_TapTyag = filtered_data_TapTyag.filter(Time__lt=filter_end_date)

        if filter_region:
            filtered_data_TapTyag = filtered_data_TapTyag.filter(Region__icontains=filter_region)

        if filter_activity:
            filtered_data_TapTyag = filtered_data_TapTyag.filter(Activity__icontains=filter_activity)

        if filter_subactivity:
            for sub_activity in filter_subactivity:
                # Assuming the sub-activities are stored as boolean fields in the model
                
                filtered_data_TapTyag = filtered_data_TapTyag.filter(**{sub_activity: 'Yes'})


        if filter_subregion:
            filtered_data_TapTyag = filtered_data_TapTyag.filter(Sub_Region__icontains=filter_subregion)

        return render(request, 'filtered_table.html', {'filtered_data_TapTyag': filtered_data_TapTyag ,'filter_activity' :filter_activity})

    elif(filter_activity == "Swadhay MM"):
        filtered_data_swadhyay = table_Swadhyay.objects.all()

        # Convert filter_start_date and filter_end_date to datetime objects
        if filter_start_date:
            filter_start_date = datetime.strptime(filter_start_date, "%Y-%m-%d").date()
        if filter_end_date:
            filter_end_date = datetime.strptime(filter_end_date, "%Y-%m-%d").date()

        # Filter based on start and end date
        if filter_start_date:
            filtered_data_swadhyay = filtered_data_swadhyay.filter(Time__gte=filter_start_date)
        if filter_end_date:
            # Add one day to filter_end_date to include that day as well
            filter_end_date = filter_end_date + timezone.timedelta(days=1)
            filtered_data_swadhyay = filtered_data_swadhyay.filter(Time__lt=filter_end_date)

        if filter_region:
            filtered_data_swadhyay = filtered_data_swadhyay.filter(Region__icontains=filter_region)
            
        if filter_activity:
            filtered_data_swadhyay = filtered_data_swadhyay.filter(Activity__icontains=filter_activity)
            
        # if filter_subactivity:
        #     for sub_activity in filter_subactivity:
        #         # Assuming the sub-activities are stored as boolean fields in the model
                
        #         filtered_data_swadhyay = filtered_data_swadhyay.filter(**{sub_activity: 'yes'})

        

        if filter_subactivity:
            # Create an empty Q object to start with
            or_condition = Q()
            print(filter_subactivity)
            for sub_activity in filter_subactivity:
                # Assuming the sub-activities are stored as boolean fields in the model
                or_condition |= Q(**{sub_activity: 'yes'})

            # Apply the OR condition to the queryset
            filtered_data_swadhyay = filtered_data_swadhyay.filter(or_condition)

        
        
        #-------------------------------                
        if filter_subregion:
            filtered_data_swadhyay = filtered_data_swadhyay.filter(Sub_Region__icontains=filter_subregion)

        
        return render(request, 'filtered_table.html', {'filtered_data_swadhyay': filtered_data_swadhyay,'filter_activity':filter_activity,'filter_subactivity_name':filter_subactivity})
    
    else:
        pass
    # Define a list of column names you want to display
    # display_columns =[
    # 'sr', 'person_id', 'Time', 'off_Time', 'Activity', 'First_Name', 
    # 'Husband_Father_Name', 'Surname', 'Gender', 'Age', 'Country', 
    # 'India_Whatsapp_No', 'Pincode', 'Foreign_WhatsappNo', 'Pincode_FR', 
    # 'Sub_Region', 'State', 'Region', 'A1', 'इनमे_से_किस_लड़ी_में_भाग_लेंगे', 'A2', 'A3', 
    # 'A4', 'a5', 'a6', 'score'
    # ]

    
    # #['sr','ID','Time','off Time	','Activity','पहला नाम / First Name	पिता / पति का नाम /  Husband / Father Name','सरनेम / Surname','लिंग / Gender','उम्र / Age','देश - Country','मोबाइल नंबर_भारत _Invdia _Whatsapp No','Pincode','मोबाइल नंबर_विदेश _ Foreign _WhatsappNo','Pincode_FR','Sub Region','State / राज्य','Region','A1','इनमे से किस लड़ी में भाग लेंगे','A2','आप महत्तम महोत्सव में फरवरी 2025 तक  प्रतिदिन 1 घंटा मौन आराधना करेंगे','आप महत्तम महोत्सव में फरवरी 2025 तक  प्रतिमाह 4 रात्रि चौविहार प्रत्याख्यान_सूर्यास्त से अगले दिन तक नवकारसी_पक्की नवकारसी कर जीवो को अभय दान देंगे','आप महत्तम महोत्सव में फरवरी 2025 तक 50 दिन पूर्ण सूर्य अस्त से सूर्य उदय संवर/पौषध/ पूर्ण दया करेंगे','आप महत्तम महोत्सव में फरवरी 2025 तक दूध_दही_घी_तेल_मीठा  में से किसी भी एक विगय का प्रतिदिन त्याग करेंगे','स्कोर',]
    # #['Time', 'Activity', 'Region', 'Sub_Region', 'First_Name', 'Age', 'Gender','India_Whatsapp_No', 'Pincode']
    # for sub_activity in filter_subactivity:
    #     display_columns.append(sub_activity)

    # # Retrieve the specified columns from the filtered data
    # filtered_data = filtered_data.values(*display_columns)

    # # Create a dictionary to pass to the template with the filtered data and display columns
    # context = {
    #     'filtered_data': filtered_data,
    #     'display_columns': display_columns,
    # }

    # return render(request, 'filtered_table.html', context)
        
#-----------------------------------
# from django.shortcuts import render
# from .models import table_TapTyag
# from django.utils import timezone
# from datetime import datetime


# def filtered_table(request):
        
#     filter_start_date = request.GET.get('start_date', '')
#     filter_end_date = request.GET.get('end_date', '')
#     #filter_time = request.GET.get('filtertime', '')
#     filter_region = request.GET.get('filterregion', '')
#     filter_activity = request.GET.get('filteractivity', '')
#     filter_subactivity = request.GET.getlist('filtersubactivity', [])
#     filter_subregion = request.GET.get('filtersubregion', '')

#     # Filter data based on the filter parameters
#     filtered_data = table_TapTyag.objects.all()
    
#     # Convert filter_start_date and filter_end_date to datetime objects
#     if filter_start_date:
#         filter_start_date = datetime.strptime(filter_start_date, "%Y-%m-%d").date()
#     if filter_end_date:
#         filter_end_date = datetime.strptime(filter_end_date, "%Y-%m-%d").date()
    
#     # Filter based on start and end date
#     if filter_start_date:
#         filtered_data = filtered_data.filter(Date__gte=filter_start_date)
#     if filter_end_date:
#         # Add one day to filter_end_date to include that day as well
#         filter_end_date = filter_end_date + timezone.timedelta(days=1)
#         filtered_data = filtered_data.filter(Date__lt=filter_end_date)
#     # if filter_time:
#     #     filtered_data = filtered_data.filter(Date=filter_time)

#     if filter_region:
#         filtered_data = filtered_data.filter(Region__icontains=filter_region)

#     if filter_activity:
#         filtered_data = filtered_data.filter(Activity__icontains=filter_activity)

#     # if filter_subactivity:
#     #     # Filter based on a list of subactivities
#     #     filtered_data = filtered_data.filter(SUB_ACTIVITY1__in=filter_subactivity)

#     if filter_subactivity:        
#         if "SA2" in filter_subactivity:
#             filtered_data = filtered_data.filter(SA2__icontains='Y')            
#         if "SA3" in filter_subactivity:
#             filtered_data = filtered_data.filter(SA3__icontains='Y')
#         if "SA4" in filter_subactivity:
#             filtered_data = filtered_data.filter(SA4__icontains='Y')
    

#     if filter_subregion:
        
#         filtered_data = filtered_data.filter(Sub_Region__icontains=filter_subregion)

#     # Define a list of column names you want to display
#     display_columns = ['Date','Activity','Region','Sub_Region','Full_name','Age','Gender','Whatsapp_India','Pincode','Village',]

#     for i in filter_subactivity:
#         display_columns.append(i)

#     print(display_columns)
#     # Retrieve the specified columns from the filtered data
#     filtered_data = filtered_data.values(*display_columns)

#     # Create a dictionary to pass to the template with the filtered data and display columns
#     context = {
#         'filtered_data': filtered_data,
#         'display_columns': display_columns,
#     }

#     return render(request, 'filtered_table.html', context)
    #return render(request, 'filtered_table.html', {'filtered_data': filtered_data})

# {% for column_name in display_columns %}
#             {% comment %} <th>{{ column_name }}</th> {% endcomment %}
#             <th data-field={{ column_name }}>{{ column_name }}</th>            
#           {% endfor %}

#*******************************home page fun**********8

from django.http import JsonResponse
from .models import table_TapTyag, table_Swadhyay


def filtered_table_view(request):
    filter_activity = request.GET.get('filteractivity', 'default_activity')
    
    if filter_activity == "Tap Tyag MM":
        region_options = list(table_TapTyag.objects.values_list('Region', flat=True).distinct())        
    elif filter_activity == "Swadhay MM":
        region_options = list(table_Swadhyay.objects.values_list('Region', flat=True).distinct())        
    else:
        region_options = []
        

    return JsonResponse({'region_options': region_options})


# from django.shortcuts import render
# from .models import table_TapTyag,table_Swadhyay
# from django.http import JsonResponse


# def filtered_table_view(request):
#     filter_activity = request.GET.get('filteractivity', 'default_activity')
#     print(filter_activity)
#     if filter_activity == "Tap Tyag MM":
#         region_options = table_TapTyag.objects.values_list('Region', flat=True).distinct()
#     elif filter_activity == "swadhyay MM":
#         region_options = table_Swadhyay.objects.values_list('Region', flat=True).distinct()
#     else:
#         region_options = []

#     return JsonResponse({'region_options': region_options})
    # return render(request, 'test.html', {
    #     'region_options': region_options,
    # })



# def filtered_table_view(request):
    
#     # Fetch unique options from the databas    
#        #time_options = table_TapTyag.objects.values_list('Date', flat=True).distinct()
#         #activity_options = table_TapTyag.objects.values_list('Activity', flat=True).distinct()
#     region_options = table_TapTyag.objects.values_list('Region', flat=True).distinct()
#         #subregion_options = table_TapTyag.objects.values_list('Sub_Region', flat=True).distinct()

#     return render(request, 'test.html', {
#        #'time_options': time_options,
#         #'activity_options': activity_options,
#         'region_options': region_options,
#         #'subregion_options': subregion_options,
        
#     })
    
    


    
####################################33

# def filtered_table_view(request):
#     filter_activity = request.GET.get('filteractivity', '')
#     # Fetch unique options from the database
#     if(filter_activity == "Tap Tyag MM"):
#         #time_options = table_TapTyag.objects.values_list('Date', flat=True).distinct()
#         #activity_options = table_TapTyag.objects.values_list('Activity', flat=True).distinct()
#         region_options = table_TapTyag.objects.values_list('Region', flat=True).distinct()
#         #subregion_options = table_TapTyag.objects.values_list('Sub_Region', flat=True).distinct()

#         return render(request, 'test.html', {
#         #'time_options': time_options,
#         #'activity_options': activity_options,
#         'region_options': region_options,
#         #'subregion_options': subregion_options,
        
#         })
#     elif(filter_activity == "swadhyay MM"):
#         region_options = table_Swadhyay.objects.values_list('Region', flat=True).distinct()

#         return render(request, 'test.html', {
#         #'time_options': time_options,
#         #'activity_options': activity_options,
#         'region_options': region_options,
#         #'subregion_options': subregion_options,
        
#     })
    

# ######################################    




# def filtered_table(request):
    
#     filter_region = request.GET.get('filterregion', '')
#     filter_subactivity = request.GET.get('filtersubactivity', '')
#     filter_activity = request.GET.get('filteractivity', '')

#     # Filter your data based on the filter parameters (replace this with your data source)
#     data = [
#         {'time': '2023-09-18', 'region': 'jaipur', 'activity': 'gyan' , 'subactivity': ['sa1','sa3','sa5'],'subregion' : 'pratap nagar'},
#         {'time': '2023-09-19', 'region': 'delhi', 'activity': 'act2' , 'subactivity': ['sa2','sa3','sa5'],'subregion' : 'ncr'},
#         {'time': '2023-09-20', 'region': 'ajmer', 'activity': 'act2' , 'subactivity': ['sa1','sa4','sa2'],'subregion' : 'lohakhan'},
#         {'time': '2023-09-21', 'region': 'bhilwara', 'activity': 'act3' , 'subactivity': ['sa1','sa3','sa5'],'subregion' : 'pathik nagar'},
#         {'time': '2023-09-22', 'region': 'international', 'activity': 'gyan' , 'subactivity': ['sa2','sa4','sa5'],'subregion' : 'usa'},
#     ]

#     #(not filter_subactivity or item['subactivity'].lower() == filter_subactivity.lower()) and \
#     filtered_data = []

#     for item in data:
#         if (not filter_region or item['region'].lower() == filter_region.lower()) and \
#            (not filter_subactivity or filter_subactivity.lower() in item['subactivity'] ) and \
#             (not filter_activity or item['activity'].lower() == filter_activity.lower()):
#             filtered_data.append(item)

#     return render(request, 'filtered_table.html', {'filtered_data': filtered_data})
    

def home(request):
    
    path = finders.find('MM_TRIAL.xlsx')
    data = pd.read_excel(path)

    header = ['Date', 'Activity', 'Region', 'Sub_Region', 'Full_name', 'Age',
        'Gender', 'Whatsapp_India', 'Pincode', 'Village', 'SUB_ACTIVITY1',
        'SA2', 'SA3', 'SA4']

    rows = {}

    for c in header:
        rows[c] = list(data.loc[:][c])    
    
    
    return render(request,'home.html',{'rows' : rows,"lent":len(rows['Region'])})
    

from django.template.defaulttags import register

@register.filter()
def custom_range(value):
    return range(value)

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)
# {% for item in data.items %}
#   <p>{{ data|get_value:item.NAME }}</p>
# {% endfor %}

@register.filter
def index(list, ind):
    return list[ind]

# def login(request):
#     # Your view logic here  
#     return render(request, 'login.html', {"name": "Navin"})
 
# @csrf_protect
# @csrf_exempt
# def userLogin(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         m = usersList.objects.find(username=username)
#         path=finders.find('login.xlsx')
#         user_data=pd.read_excel(path)

#         temp=user_data[user_data['username']==username]

#         if not temp.empty:
#             passw=temp.iloc[0]['password']
#             location=temp.iloc[0]['location']
#             if passw==password:
#                 return JsonResponse({'location':location,'message':'loginSuccess'})
#             else:
#                 return JsonResponse({'message':'Password does not match'})
#         else:
#             return JsonResponse({'message':'No such user exists'})

def filterfunc(data,time=None,region=None,subRegion=None,activity=None,subActivity=None):
    if time:
        data=data[data['Date']==time]
    if region:
        data=data[data['Region']==region]
    if subRegion:
        data = data[data['Sub-Region'] == subRegion]
    if activity:
        data = data[data['Activity'] == activity]
    if subActivity:
        data = data[data['SUB ACTIVITY1'] == subActivity]

    return data



@csrf_protect
@csrf_exempt
def filterAPI(request):
    time=request.POST.get('time')
    region = request.POST.get('region')
    subRegion = request.POST.get('subRegion')
    activity = request.POST.get('activity')
    subActivity= request.POST.get('subActivity')

    path = finders.find('MM_TRIAL.xlsx')
    data = pd.read_excel(path)
    dic = []
    x =  requests.post('http://127.0.0.1:8000/api/filterapi/')
    data=filterfunc(data,time,region,subRegion,activity,subActivity)
    # print(data)
    data=data.to_dict(orient='records')
    return JsonResponse({'message':data},safe=False)


# api/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.serializers import *
# from .models import DataEntry
# from .serializers import DataEntrySerializer

# class DataEntryList(APIView):
#     def post(self, request):
#         # Get filter parameters from the request
#         time_start = request.data.get('time_start', None)
#         time_end = request.data.get('time_end', None)
#         regions = request.data.getlist('region', [])
#         activities = request.data.getlist('activity', [])

#         # Prepare a filter query based on the parameters
#         queryset = DataEntry.objects.all()

#         if time_start and time_end:
#             queryset = queryset.filter(time__range=[time_start, time_end])

#         if regions:
#             queryset = queryset.filter(region__in=regions)

#         if activities:
#             queryset = queryset.filter(activity__in=activities)

#         serializer = DataEntrySerializer(queryset, many=True)
#         return Response(serializer.data)


