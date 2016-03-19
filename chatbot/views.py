from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from chatbot.forms import PostForm
from chatbot.models import Answers, Contents, Questions

list=[Contents('bip','input your questions!')]
def index(request):
    return render(request,'index.html',{'list':list})

def input(request):
    if(request.method=='GET'):
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            answer_temp = Answers.objects.fill()
            return HttpResponse(question_temp)

    return HttpResponse(form)
