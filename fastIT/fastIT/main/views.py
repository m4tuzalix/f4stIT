from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Job, main_cities
from django.core.paginator import Paginator


def main(request):
    return render(request, "main_page.html")

def about(request):
    return render(request, "project.html")

def Pagination(request, model, number):
    paginator = Paginator(model, number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    index = paginator.page_range.index(page_obj.number)
    max_index = len(paginator.page_range)
    start_index = index - 9 if index >= 9 else 0
    end_index = index + 9 if index <= max_index - 9 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return page_obj, page_range

class Search(View):
    template_name="search.html"
    paginate_by = 30

    def get(self, request):
        search_phrase = request.GET["search"]
        cities = ""
        results = None
        if "city" in request.GET:
            cities = request.GET["city"].split(",")
            results = Job.objects.filter(position__icontains=search_phrase, city__in=cities)
            if "Inne" in cities:
                others = Job.objects.exclude(position__icontains=search_phrase, city__in=main_cities)
                results = results | others
            cities = request.GET["city"]
        else:
            results = Job.objects.filter(position__icontains=search_phrase)
        paginator_objects, paginator_range = Pagination(request, results.order_by("city"), self.paginate_by)
        context = {
            "objects":paginator_objects,
            "range":paginator_range,
            "search_value": search_phrase,
            "city_value": cities
        }
        return render(request, self.template_name, context)




