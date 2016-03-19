from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from chatbot.forms import PostForm
from chatbot.models import Answers, Contents, Questions

def index(request):
    list = Contents.objects.all()
    return render(request,'index.html',{'list':list})

def input(request):
    if(request.method=='GET'):
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Contents(name='you',text=content).save()
            question_temp = Questions.objects.filter(question_text=content)
            if Questions.DoesNotExist:
                Contents(name='bip',text="i don't know").save()
            else:
                answer_temp = Answers.objects.filter(pk=question_temp[0].answers_id)
                Contents(name='bip',text=answer_temp[0].answers_text).save()
            list = Contents.objects.all()
            return render(request,'index.html',{'list':list})

    return HttpResponse(form)
