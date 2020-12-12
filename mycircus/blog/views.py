from django.core.mail import mail_admins,send_mail
import datetime
from django.contrib import messages
from django.conf import settings

from django.shortcuts import get_object_or_404, render,redirect
from .models import Article
from .forms import Create_Article,ContactForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def blog_index(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'blog_index.html',{'articles': articles})

def landing_page(request):
    articles = Article.objects.all().order_by('-date')[:6]
    return render(request,'landing_page.html',{'articles': articles})


@login_required()
def blog_detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    # article = Article.objects.get(pk=pk)
    # return HttpResponse(pk)
    return render(request,'blog_detail.html',{'article':article})



def blog_create(request):
    # create_form = Create_Article()
    if request.method == 'POST':
        create_form=Create_Article(request.POST,request.FILES)
        if create_form.is_valid():
            form = create_form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('blog_index')
    else:
        create_form = Create_Article()       
    return render(request,'blog_create.html',{'create_form':create_form})


def blog_edit(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == "POST":
        form = Create_Article(request.POST,instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog_detail',pk=article.pk)
    else:
        form = Create_Article(instance=article)

    return render(request, 'blog_edit.html', {'form': form})


def blog_delete(request,pk):
    article = get_object_or_404(Article,pk=pk)
    
    article.delete()
    return redirect('blog_index')


def project(request):
    return render(request,"projects.html")

# Email views

def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():

            name = f.cleaned_data['name']
            from_email = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:<{}>".format(name, f.cleaned_data['email'])

            message = "Purpose: {}\n\nDate: {}\n\nMessage:\n\n {}".format(
                dict(f.purpose_choices).get(f.cleaned_data['purpose']),
                datetime.datetime.now(),
                f.cleaned_data['message']
            )

            # mail_admins(subject, message)
            send_mail(subject, message,settings.EMAIL_HOST_USER,['anwurissah@gmail.com'], fail_silently=False)
            messages.add_message(request, messages.INFO, 'Thanks for submitting your feedback.')

            return redirect('contact')

    else:
        f = ContactForm()

    return render(request, 'contact.html', {'form': f})