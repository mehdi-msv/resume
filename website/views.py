from django.shortcuts import render
def index(request):
    context = {'NAME':'Mehdi',
               'LAST_NAME':'Mousavi',
               'Profile':'Backend Developer',
               'Email':'mehdi.mousavi.rad1@gmail.com',
               'Phone':'(+98) 916-854-3458'} 
    return render(request,'index.html', context)