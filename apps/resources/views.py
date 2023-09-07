from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count, Avg

from .models import Resources, Category, ResourcesTag, Review, Rating
from apps.user.models import User
from .utils import generate_cat_count_list

def home_page(request):
    cnt = Resources.objects.all().count()
    act_use = User.objects.filter(is_active=True).count()
    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))

    context = {
        'cnt': cnt,
        'act_use': act_use,
        'res_per_cat': res_per_cat,
    }
    
    return render(request,"resources/home.html", context)


def resource_detail(request, id):
    res = Resources.objects.get(pk=id)
    resource_tags = ResourcesTag.objects.filter(resources_id=res)
    reviews = Review.objects.filter(resources_id=res).count()
    average_rating = Rating.objects.filter(resources_id=res).aggregate(avg_rating=Avg("rate"))["avg_rating"]
    context = {
        'res': res, 
        'resource_tags': resource_tags,
        'reviews': reviews,
        'average_rating': average_rating,
    }
    
    return render(request, 'resources/resource_detail.html',context)
    

class HomePage(TemplateView):
    template_name = 'home_page.html'