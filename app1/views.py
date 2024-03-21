from django.shortcuts import render,redirect,HttpResponse
from .models import Post,Reviews,Links
from .forms import AddReview,UploadPost,Linkform
from django.views import generic 

# Create your views here.
def home(request):
    form=AddReview
    if request.method == 'POST':
        form=AddReview(request.POST)
        if form.is_valid():
            form.save()
            return redirect('susuc')
    return render (request,"home.html",{'form':form})

def audio(request):
    return render (request,"audio.html")

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'blog.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'


def chat(request):
    form=AddReview
    if request.method == 'POST':
        form=AddReview(request.POST)
        if form.is_valid():
            form.save()
            return redirect('susuc')
    return render(request,"chat.html",{'form':form})

def reviewed(request):
    data=Reviews.objects.all().order_by('-upload')
    return render(request,'review.html',{'data':data})

def susc(request):
    return render(request,'susuc.html')

def complication(request):
    return render (request,"complication.html")

def diafact(request):
    return render (request,"diafact.html")

def diet(request):
    return render (request,"diet.html")

def elderdia(request):
    return render (request,"elderdia.html")

def faq(request):
    return render (request,"faq.html")

def fitness(request):
    return render(request,"fitness.html")

def footcare(request):
    return render (request,"footcare.html")

def juvenlie(request):
    return render (request,"juvenlie.html")

def latestdia(request):
    data=Links.objects.all().order_by('-created')
    return render (request,"latestdia.html",{'data':data})

def linkup(request):
    form=Linkform
    if request.method == 'POST':
        form=Linkform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1 style="text-align: center;">Uploaded</h1>')
    return render (request,'linkup.html',{'form':form})

def video(request):
    return render (request,"video.html")

def women(request):
    return render (request,"women.html")
