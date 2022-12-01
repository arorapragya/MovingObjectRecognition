from django.shortcuts import render
from .forms import VideoForm
from .models import Video

from pathlib import Path
from .Moving_object_Detection import MOD


BASE_DIR = Path(__file__).resolve().parent.parent / 'media'

def home(request):
    if request.method=='POST':
        form= VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form= VideoForm()

    if request.method == "POST":
        video=Video.objects.last()
        
        videofile=video.videofile
        
    
        temp2=str(videofile)

        processedVideoPath=str(BASE_DIR / temp2)
        print("=============")
        print(processedVideoPath)
        
        obj1=MOD(processedVideoPath)
    # processed_video=MOD()
        video2=obj1.movingObjectDetection()
       

        print("=========",str(video2))
    else:
        video2=""    
  
    return render(request,'myapp/home.html',{'videofile':video2,'form':form})