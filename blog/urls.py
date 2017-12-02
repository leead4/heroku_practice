"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url


# Remember to include your view below
# example: from website.views.view_category import *
from blogpost.views.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about$', about, name='about'),
    url(r'^archive$', archive, name='archive'),
    url(r'^search_keyword/$', search_keywords, name='search_keywords'),
    url(r'^popular$', popular, name='popular'),
    url(r'^tags$', get_tags, name='get_tags'),
    url(r'^topics$', topic, name='topic')


]



