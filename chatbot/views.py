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
            list.append('you',content)
            question_temp = Questions.objects.filter(question_text=content)
            answer_temp = Answers.objects.filter(pk=question_temp[0].answers_id)

            return HttpResponse(list)

    return HttpResponse(form)
