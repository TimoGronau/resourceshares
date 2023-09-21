from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count, Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Resources, Category, ResourcesTag, Review, Rating
from apps.user.models import User
from .form import PostResourceForm
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


class ResourceDetailView(LoginRequiredMixin,View):
    max_viewed_resources = 5
    template_name = 'resources/resource_detail.html'

    def get(self, request, id):
        viewed_resources = request.session.get("viewed_resources", [])
        res = Resources.objects.get(pk=id)
        viewed_resource = [id, res.title]

        if viewed_resource in viewed_resources:
            viewed_resources.remove(viewed_resource)
        viewed_resources.insert(0, viewed_resource)
        
        viewed_resources = viewed_resources[:self.max_viewed_resources]
        request.session["viewed_resources"] = viewed_resources

        resource_tags = ResourcesTag.objects.filter(resources_id=res)
        reviews = Review.objects.filter(resources_id=res).count()
        average_rating = Rating.objects.filter(resources_id=res).aggregate(avg_rating=Avg("rate"))["avg_rating"]

        context = {
            'res': res,
            'resource_tags': resource_tags,
            'reviews': reviews,
            'average_rating': average_rating,
        }

        return render(request, self.template_name, context)

class ResourcePostView(LoginRequiredMixin, View):
    template_name = "resources/resource_post.html"

    def get(self, request):
        form = PostResourceForm()
        return render(
            request,
            self.template_name,
            {"form": form},
        )

    def post(self, request):
        form = PostResourceForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_resource = Resources.objects.create(**data)
            new_resource.user_id = User.objects.get(pk=1)
            new_resource.save()
            return redirect("http://127.0.0.1:8000/")

        return render(
            request,
            self.template_name,
            {"form": form},
        )


class HomePage(TemplateView):
    template_name = 'home_page.html'