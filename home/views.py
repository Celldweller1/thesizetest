import math
from django.shortcuts import render
from django.http import *
from django.views import View
from django.core.files.storage import FileSystemStorage
import os 
from django.core.files.storage import default_storage
from pathlib import Path
from django.conf import settings
from .aicode.calculation_loop import main_measurement_loop
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DataSerializer


from .models import *

# Create your views here.


current_dir = os.getcwd()

# Define the relative path to the "aicode" directory from the current directory
front_relative_path = os.path.join(current_dir,'front')
side_relative_path = os.path.join(current_dir,'side')


def validate(email,age,userLength):
    maxAge = SystemConfiguration.objects.get(key='max age').value;
    maxLength = SystemConfiguration.objects.get(key='max length').value;
    if(age < maxAge):
        return False
    if(maxLength < maxLength):
        return False
    return True

class ScanView(View):
    def get(self,request):
        emailRegex = SystemConfiguration.objects.get(key='email regex').value;
        maxAge = SystemConfiguration.objects.get(key='max age').value;
        maxLength = SystemConfiguration.objects.get(key='max length').value;
        frontInstructions = SystemConfiguration.objects.get(key='front instructions').value;
        sideInstructions = SystemConfiguration.objects.get(key='side instructions').value;
        return render(request,"home/home.html",{
            "maxAge":maxAge,"maxLength":maxLength,"emailRegex":emailRegex,"frontInstructions":frontInstructions,"sideInstructions":sideInstructions
        })
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        print(request.FILES)
        frontVideo = request.FILES.get('frontVideo')
        sideVideo = request.FILES.get('sideVideo')
        fs = FileSystemStorage(location=front_relative_path)
        fs.save(email+"_front.mp4", frontVideo)
        fs = FileSystemStorage(location=side_relative_path)
        fs.save(email+"_side.mp4", sideVideo)
        contactNumber = request.POST['contactNumber']
        userLength = request.POST.get('userLength')
        chest,waist,hipps,inseem,arm = main_measurement_loop(int(userLength), os.path.join(front_relative_path,email+'_front.mp4'),os.path.join(side_relative_path,email+'_side.mp4'))
        chest = math.floor(chest)
        waist = math.floor(waist)
        hipps = math.floor(hipps)
        inseem = math.floor(inseem)
        arm = math.floor(arm)
        request.session['vote'] = 1
        request.session['chest'] = chest
        request.session['waist'] = waist
        request.session['hipps'] = hipps
        request.session['inseem'] = inseem
        request.session['arm'] = arm

        
        if validate(email,age,userLength):
            UserScan.objects.create(name=name,age=age,email=email,length=userLength,gender=gender,contactNumber=contactNumber,chest=chest,waist=waist,hipps=hipps,inseem=inseem,arm=arm)

        return HttpResponseRedirect(request.path)

def test(request):
    return render(request,"home/test.html")

@api_view(['POST'])
def testApi(request):
    sideImagesFolder = SystemConfiguration.objects.get(key='side folder').value;
    frontImagesFolder = SystemConfiguration.objects.get(key='front folder').value;
    name = request.POST['name']
    email = request.POST['email']
    gender = request.POST['gender']
    age = request.POST['age']
    print(request.FILES)
    frontVideo = request.FILES.get('frontVideo')
    sideVideo = request.FILES.get('sideVideo')

    # files = glob.glob(frontImagesFolder+'\\*')
    # for f in files:
    #     os.remove(f)
    # files = glob.glob(sideImagesFolder+'\\*')
    # for f in files:
    #     os.remove(f)
    fs = FileSystemStorage(location=frontImagesFolder) #defaults to   MEDIA_ROOT  
    # print(request.FILES.get('frontVideo').read())
    # if ext == '.mov':
    #     attachment.filename = os.path.splitext(filename)[0] + '.mp4'
    # else:
    #     attachment.filename = filename
    fs.save(email+"_front.mp4", frontVideo)

    fs = FileSystemStorage(location=sideImagesFolder) #defaults to   MEDIA_ROOT  
    fs.save(email+"_side.mp4", sideVideo)
    contactNumber = request.POST['contactNumber']
    userLength = request.POST.get('userLength')
    chest,waist,hipps,inseem,arm = main_measurement_loop(int(userLength), os.path.join(front_relative_path,email+'_front.mp4'),os.path.join(side_relative_path,email+'_side.mp4'))
    chest = math.floor(chest)
    waist = math.floor(waist)
    hipps = math.floor(hipps)
    inseem = math.floor(inseem)
    arm = math.floor(arm)

    if validate(email,age,userLength):
        test = UserScan.objects.create(name=name,age=age,email=email,length=userLength,gender=gender,contactNumber=contactNumber,chest=chest,waist=waist,hipps=hipps,inseem=inseem,arm=arm)
        serializer = DataSerializer(test, many=False)
        return Response(serializer.data)
    return HttpResponseBadRequest()
