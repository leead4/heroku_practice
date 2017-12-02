from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
import operator
from django.shortcuts import render
from django import forms
from django.db.models import Q
from blogpost.models.models import *

# Create your views here.
def index(request):
    template_name = 'index.html'
    all_blogs = Post.objects.all()
    return render(request, template_name, {'blogs': all_blogs})

def about(request):
	template_name = 'about.html' 
	return render(request, template_name, {})

def archive(request):
	template_name = 'archive.html' 
	blogs = Post.objects.order_by('date')[:5]
	return render(request, template_name, {'blogs': blogs})


def search_keywords(request):

    form_data = request.GET
    iterable_form_data = form_data.dict()
    
    search_box = iterable_form_data['Search']
    print("search_box", search_box)
    

    posts_head = Post.objects.filter(content__text__contains=search_box)
    
    print_me = list(posts_head)
    print("hello", print_me)


    for head in print_me:
        print("head", type(head))

    print("post", posts_head)

    template_name = 'search_keywords.html'

    return render(request, template_name, {'blogs': posts_head})

def popular(request):
    blogs = Post.objects.order_by('post_like')
    template_name = 'popular.html'
    return render(request, template_name, {'blogs': blogs})    


def get_tags(request):
    blogs = Post.objects.filter(tags__topic = "Illustration" )
    template_name = 'tags.html'
    # print(blogs)
    return render(request, template_name, {'blogs': blogs})

def topic(request):
    topic ="Illustration"
    blogs = Post.objects.order_by('date')[:5]
    template_name = 'topic.html'
    print(blogs)
    return render(request, template_name, {'blogs': blogs, 'topic': topic})

# def like_this_post(request):


# def share_this_post(request):


# def get_posts_by_topic(request):


# def get_posts_by_year(request):


# def get_posts_by_most_shared(request):


# def get_post_by_most_liked(request):


