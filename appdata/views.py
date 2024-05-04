from django.shortcuts import render,redirect
from django.contrib import messages  
from .models import *
from .forms import *
import datetime
import time 
from playsound import playsound
from django.db.models import Q
import qrcode
import cv2
def DepartmentAdd(request):  
    if request.method=='POST':        
        frm = DepartmentForm(request.POST)  
        if frm.is_valid():            
            frm.save()
            fname=request.POST['qr']
            loc=request.POST['loc']
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            loc = loc.split(',')
            data="https://maps.google.com/maps?q="+str(loc[0]).strip()+"%2C"+str(loc[1]).strip()+"&z=17&hl=en"
            qr.add_data(data)
            qr.make(fit=True)

            # Create an image from the QR code
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image
            img.save("media/"+fname)
            messages.success(request,'Department Save Successfully')
            return redirect('/DepartmentAdd')
        else:
            messages.success(request,'Please Fill All the Field')
    return render(request,'department_add.html')
def DepartmentView(request):
    frm=Department.objects.all()
    context={'data':frm}
    return render(request,'department_view.html',context)
def DepartmentList(request):
    frm=Department.objects.all()
    context={'data':frm}
    return render(request,'department_list.html',context)
def DepartmentDelete(request,id):
    frm=Department.objects.get(id=id)
    frm.delete()
    import os.path
    from os import path
    fpath="media/"+frm.dname+'.png'
    if path.exists(fpath):
        print('File found')
        os.remove(fpath)  
    print(frm.dname)
    return redirect('/DepartmentList')
def Login(request):
    if request.method=='POST':
        uname=request.POST['uname']       
        pass1=request.POST['pass1']
        if uname=="admin" and pass1=="admin":
            return redirect('/DepartmentList')
        else:
            messages.success(request,'Login Failed')
        
    return render(request,'login.html')
def Welcome(request):
    

    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open a video capture object
    cap = cv2.VideoCapture(0)
    m=0
    # Loop through each frame of the video
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw bounding boxes around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            m=1+1
            print(m)
        
        # Display the frame with marked faces
        cv2.imshow('Video', frame)
        if m==10:
            break
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
    playsound("voice.mp3")
    return redirect('/DepartmentView')

