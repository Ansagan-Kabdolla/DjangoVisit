from django.shortcuts import render,redirect,HttpResponseRedirect
from itertools import chain
from .forms import ReviewsEatForm,ReviewsStayForm
from .models import *
from django.views.generic import ListView,DetailView
from django.views.generic.base import View
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from django.conf import settings
from django.utils import translation


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request,'index.html')

def akmola(request):
    aks = Akmola.objects.all()
    return render(request,'akmola.html',{'aks':aks})

def akmola_detail(request,slug):
    akm = Akmola.objects.get(slug=slug)
    return render(request, 'akmola_detail.html', {'akm': akm})

def events(request):
    evs = Events.objects.all()
    paginator = Paginator(evs, 8)
    page = request.GET.get('page')
    try:
        evs_page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        evs_page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        evs_page = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    return render(request,'events.html',{'events':evs_page,'n':n})

def search(request):
    query = request.GET.get('q')
    result = Eat.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(address__icontains=query)
        )
    return render(request, 'search.html', {'results': result,'query':query,'result_count':len(result)})

def search_new(request):
    q = request.GET.get('q')

    query_sets = []
    queryset_go = Go.objects.search(query=q)
    queryset_stay = Stay.objects.search(query=q)
    queryset_eat = Eat.objects.search(query=q)
    query_sets.append(queryset_go)
    query_sets.append(queryset_eat)
    query_sets.append(queryset_stay)
    final_set = list(chain(*query_sets))
    final_set.sort(key=lambda x: x.date, reverse=True)  # Выполняем сортировку

    return render(request, 'search.html', {'results': final_set,'query':q})

def news(request):
    news = News.objects.all()
    last_news = news.last()
    news = news.exclude(slug = last_news.slug)
    return render(request,'news.html',{'news':news,'last_news':last_news})

def news_detail(request,slug):
    new = News.objects.get(slug=slug)
    news = News.objects.order_by('-id')[:5]
    return render(request,'news_detail.html',{'new':new,'news':news})

def stay(request):
    dic_types = {}
    dic_cities = {}
    dic_stars = {}
    stays = Stay.objects.all()
    hotels = SidebarToStay.objects.all()
    if len(stays) == 0:
        pass
    types = stays.values('type').distinct()
    cities = stays.values('city').distinct()
    stars = stays.values('stars').distinct()
    for i in types:
        # print(i['type'])
        count = stays.filter(type=i['type']).count()
        tip = TypesStay.objects.get(id=i['type'])
        dic_types[tip] = count
    for i in cities:
        count = stays.filter(type=i['city']).count()
        city = Cities.objects.get(id=i['city'])
        dic_cities[city] = count
    for i in stars:
        count = stays.filter(stars=i['stars']).count()
        dic_stars[i['stars']] = count

    paginator = Paginator(stays, 6)
    page = request.GET.get('page')
    try:
        stays_page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        stays_page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        stays_page = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    if request.LANGUAGE_CODE == 'ru':
        stay_count_otel = stays.filter(type__name='Отель').count()
        stay_count_sanat = stays.filter(type__name='Санаторий').count()
        stay_count_gostdom = stays.filter(type__name='Гостевые дома').count()
        stay_count_zona = stays.filter(type__name='Зона отдыха').count()
    elif request.LANGUAGE_CODE == 'en':
        stay_count_otel = stays.filter(type__name='Hotel').count()
        stay_count_sanat = stays.filter(type__name='Sanatorium').count()
        stay_count_gostdom = stays.filter(type__name='Guest house').count()
        stay_count_zona = stays.filter(type__name='Recreation area').count()
    else:
        stay_count_otel = stays.filter(type__name='Қонақ үй').count()
        stay_count_sanat = stays.filter(type__name='Шипажай').count()
        stay_count_gostdom = stays.filter(type__name='Қонақ үйлер').count()
        stay_count_zona = stays.filter(type__name='Демалыс аймағы').count()
    context = {'stays':stays_page,'n':n,'types':dic_types,'cities':dic_cities,'stars':dic_stars,'stay_count_otel':stay_count_otel,
               'stay_count_sanat':stay_count_sanat,'stay_count_gostdom':stay_count_gostdom,'hotels':hotels,
               'stay_count_zona':stay_count_zona,
               }
    return render(request,'stay.html',context)

def go(request):
    dic_types={}
    dic_cities={}
    to_go = Go.objects.all()
    types = to_go.values('type').distinct()
    cities = to_go.values('city').distinct()
    for i in types:
        #print(i['type'])
        count = to_go.filter(type = i['type']).count()
        tip = TypesGo.objects.get(id=i['type'])
        dic_types[tip] = count
    for i in cities:
        count = to_go.filter(type = i['city']).count()
        city = Cities.objects.get(id=i['city'])
        dic_cities[city] = count

    paginator = Paginator(to_go, 8)
    page = request.GET.get('page')
    try:
        go = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        go = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        go = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    if request.LANGUAGE_CODE == 'ru':
        count_museum = to_go.filter(type__name = 'Музей').count()
        count_monument = to_go.filter(type__name = 'Памятник').count()
        count_zapovednik = to_go.filter(type__name = 'Заповедник').count()
        count_showplace = to_go.filter(type__name = 'Достопримечательность').count()
    elif request.LANGUAGE_CODE == 'en':
        count_museum = to_go.filter(type__name='Museum').count()
        count_monument = to_go.filter(type__name='Monument').count()
        count_zapovednik = to_go.filter(type__name='Zapovednik').count()
        count_showplace = to_go.filter(type__name='Showplace').count()
    else:
        count_museum = to_go.filter(type__name='Мұражай').count()
        count_monument = to_go.filter(type__name='Ескерткіш').count()
        count_zapovednik = to_go.filter(type__name='Қорық').count()
        count_showplace = to_go.filter(type__name='Көрікті жерлер').count()
    context= {'to_go':go,'n':n,'types':dic_types,'cities':dic_cities,'count_museum':count_museum,
              'count_monument':count_monument,'count_zapovednik':count_zapovednik,'count_showplace':count_showplace}
    return render(request, 'where.html', context)

def eat(request):
    dic_types = {}
    dic_cities = {}
    eat_list = Eat.objects.all()
    types = eat_list.values('type').distinct()
    cities = eat_list.values('city').distinct()
    food = NationalFoods.objects.get(pk=1)
    for i in types:
        #print(i['type'])
        count = eat_list.filter(type = i['type']).count()
        tip = TypesEat.objects.get(id=i['type'])
        dic_types[tip] = count
    for i in cities:
        count = eat_list.filter(city = i['city']).count()
        city = Cities.objects.get(id=i['city'])
        dic_cities[city] = count
    paginator = Paginator(eat_list, 1)
    page = request.GET.get('page')
    try:
        eats = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        eats = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        eats = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1,1+n)
    if request.LANGUAGE_CODE == 'ru':
        count_restoran = eat_list.filter(type__name = 'Ресторан').count()
        count_cafe = eat_list.filter(type__name = 'Кафе').count()
        count_fast_food = eat_list.filter(type__name = 'Фаст-фуд').count()
        count_stolovaia = eat_list.filter(type__name = 'Столовая').count()
    elif request.LANGUAGE_CODE == 'kk':
        count_restoran = eat_list.filter(type__name='Дәмхана').count()
        count_cafe = eat_list.filter(type__name='Кафе').count()
        count_fast_food = eat_list.filter(type__name='Фастөфуд').count()
        count_stolovaia = eat_list.filter(type__name='Асхана').count()
    else:
        count_restoran = eat_list.filter(type__name='Restaraunt').count()
        count_cafe = eat_list.filter(type__name='Cafe').count()
        count_fast_food = eat_list.filter(type__name='Fast-food').count()
        count_stolovaia = eat_list.filter(type__name='Canteents').count()
    return render(request,'restaraunt.html',{'eats':eats,'n':n,'types':dic_types,'cities':dic_cities,'foods':food,
                                             'count_restoran':count_restoran,'count_cafe':count_cafe,
                                             'count_fast_food':count_fast_food,'count_stolovaia':count_stolovaia})


def eat_detail(request,slug):
    eat = Eat.objects.get(slug=slug)
    reviews = eat.reviews.all()
    return render(request,'eat_detail.html', {'eat':eat,'reviews':reviews})

def go_detail(request,slug):
    to_go = Go.objects.all()
    go = to_go.get(slug=slug)
    if request.LANGUAGE_CODE == 'ru':
        count_museum = to_go.filter(type__name = 'Музей').count()
        count_monument = to_go.filter(type__name = 'Памятник').count()
        count_zapovednik = to_go.filter(type__name = 'Заповедник').count()
        count_showplace = to_go.filter(type__name = 'Достопримечательность').count()
    elif request.LANGUAGE_CODE == 'en':
        count_museum = to_go.filter(type__name='Museum').count()
        count_monument = to_go.filter(type__name='Monument').count()
        count_zapovednik = to_go.filter(type__name='Zapovednik').count()
        count_showplace = to_go.filter(type__name='Showplace').count()
    else:
        count_museum = to_go.filter(type__name='Мұражай').count()
        count_monument = to_go.filter(type__name='Ескерткіш').count()
        count_zapovednik = to_go.filter(type__name='Қорық').count()
        count_showplace = to_go.filter(type__name='Көрікті жерлер').count()
    return render(request,'go_detail.html', {'go':go,'count_museum':count_museum,
              'count_monument':count_monument,'count_zapovednik':count_zapovednik,'count_showplace':count_showplace}
    )

def stay_detail(request,slug):
    stay = Stay.objects.get(slug=slug)
    reviews = stay.reviews.all()
    return render(request,'stay_detail.html', {'stay':stay,'reviews':reviews})


class AddReviewEat(View):
    def post(self,request,pk):
        eat = Eat.objects.get(pk=pk)
        reviews = eat.reviews.all()
        form = ReviewsEatForm(request.POST)
        e = False
        if form.is_valid():
            form = form.save(commit=False)
            form.rubric_id = pk
            form.save()
        else:
            e = True
            #return render(request,'eat_detail.html',{'form':form,'eat':eat,'reviews':reviews})
        if 'next' in request.GET:
            return redirect(request.GET['next'])
        return render(request,'eat_detail.html', {'eat':eat,'reviews':reviews,'e':e})

class AddReviewStay(View):
    def post(self,request,pk):
        stay = Stay.objects.get(pk=pk)
        reviews = stay.reviews.all()
        form = ReviewsStayForm(request.POST)
        e = False
        if form.is_valid():
            form = form.save(commit=False)
            form.rubric_id = pk
            form.save()
        else:
            e = True
            #return render(request,'eat_detail.html',{'form':form,'eat':eat,'reviews':reviews})
        if 'next' in request.GET:
            return redirect(request.GET['next'])
        return render(request,'stay_detail.html', {'stay':stay,'reviews':reviews,'e':e})

def filtering(request):
    dic_types = {}
    dic_cities = {}
    MinPrice=None
    MaxPrice=None
    eat_list = Eat.objects.all()
    types = eat_list.values('type').distinct()
    cities = eat_list.values('city').distinct()
    food = NationalFoods.objects.get(pk=1)
    for i in types:
        # print(i['type'])
        count = eat_list.filter(type=i['type']).count()
        tip = TypesEat.objects.get(id=i['type'])
        dic_types[tip] = count
    for i in cities:
        count = eat_list.filter(city=i['city']).count()
        city = Cities.objects.get(id=i['city'])
        dic_cities[city] = count

    queryset = Eat.objects.all()
    if "city" in request.GET:
        queryset = queryset.filter(
                Q(city__name__in = request.GET.getlist("city"))
            )
    if "type" in request.GET:
        queryset = queryset.filter(
                Q(type__name__in = request.GET.getlist("type"))
        )
    if request.GET.get("MinPrice"):
        MinPrice = request.GET.get("MinPrice")
        queryset = queryset.filter(
            Q(price__gte=request.GET.get("MinPrice"))
        )
    if request.GET.get("MaxPrice"):
        MaxPrice = request.GET.get("MaxPrice")
        queryset = queryset.filter(
            Q(price__lte=request.GET.get("MaxPrice"))
        )
    city_list = ''.join([f"city={x}&" for x in request.GET.getlist("city")])
    type_list = ''.join([f"type={x}&" for x in request.GET.getlist("type")])
    q = queryset
    paginator = Paginator(q, 6)
    page = request.GET.get('page')
    try:
        eats = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        eats = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        eats = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    if request.LANGUAGE_CODE == 'ru':
        count_restoran = eat_list.filter(type__name='Ресторан').count()
        count_cafe = eat_list.filter(type__name='Кафе').count()
        count_fast_food = eat_list.filter(type__name='Фаст-фуд').count()
        count_stolovaia = eat_list.filter(type__name='Столовая').count()
    elif request.LANGUAGE_CODE == 'kk':
        count_restoran = eat_list.filter(type__name='Дәмхана').count()
        count_cafe = eat_list.filter(type__name='Кафе').count()
        count_fast_food = eat_list.filter(type__name='Фаст-фуд').count()
        count_stolovaia = eat_list.filter(type__name='Асхана').count()
    else:
        count_restoran = eat_list.filter(type__name='Restaraunt').count()
        count_cafe = eat_list.filter(type__name='Cafe').count()
        count_fast_food = eat_list.filter(type__name='Fast-food').count()
        count_stolovaia = eat_list.filter(type__name='Canteents').count()

    return render(request, 'restaraunt.html', {'eats':eats,'n':n,'city_list':city_list,'type_list':type_list,'foods':food,
                                               'MinPrice':MinPrice,'MaxPrice':MaxPrice,
                                               'types':dic_types,'cities':dic_cities,
                                             'count_restoran':count_restoran,'count_cafe':count_cafe,
                                             'count_fast_food':count_fast_food,'count_stolovaia':count_stolovaia})


def filter_ajax(request):
    queryset = Eat.objects.all()
    if "city" in request.GET:
        queryset = queryset.filter(
            Q(city__in = request.GET.getlist("city"))
        )
    if "type" in request.GET:
        queryset = queryset.filter(
            Q(type__in = request.GET.getlist("type"))
        )
    queryset = queryset.distinct().values('title','type','city')

    json_queryset = list(queryset)
    return JsonResponse({'eats':json_queryset},safe=False)

def filtering_stay(request):
    dic_types = {}
    dic_cities = {}
    dic_stars = {}
    MinPrice = None
    MaxPrice = None
    stays = Stay.objects.all()
    hotels = StaticPages.objects.filter(type='where_to_stay')
    if len(stays) == 0:
        pass
    types = stays.values('type').distinct()
    cities = stays.values('city').distinct()
    stars = stays.values('stars').distinct()
    for i in types:
        # print(i['type'])
        count = stays.filter(type=i['type']).count()
        tip = TypesStay.objects.get(id=i['type'])
        dic_types[tip] = count
    for i in cities:
        count = stays.filter(type=i['city']).count()
        city = Cities.objects.get(id=i['city'])
        dic_cities[city] = count
    for i in stars:
        count = stays.filter(stars=i['stars']).count()
        dic_stars[i['stars']] = count
    queryset = Stay.objects.all()
    if "city" in request.GET:
        queryset = queryset.filter(
                Q(city__name__in = request.GET.getlist("city"))
            )
    if "type" in request.GET:
        queryset = queryset.filter(
                Q(type__name__in = request.GET.getlist("type"))
        )
    if "stars" in request.GET:
        queryset = queryset.filter(
            Q(stars__in=request.GET.getlist("stars"))
        )
    if request.GET.get("MinPrice"):
        MinPrice = request.GET.get("MinPrice")
        queryset = queryset.filter(
            Q(price__gte=request.GET.get("MinPrice"))
        )
    if request.GET.get("MaxPrice"):
        MaxPrice = request.GET.get("MaxPrice")
        queryset = queryset.filter(
            Q(price__lte=request.GET.get("MaxPrice"))
        )
    city_list = ''.join([f"city={x}&" for x in request.GET.getlist("city")])
    type_list = ''.join([f"type={x}&" for x in request.GET.getlist("type")])
    stars_list = ''.join([f"stars={x}&" for x in request.GET.getlist("stars")])
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    try:
        stays_page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        stays_page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        stays_page = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    if request.LANGUAGE_CODE == 'ru':
        stay_count_otel = stays.filter(type__name='Отель').count()
        stay_count_sanat = stays.filter(type__name='Санаторий').count()
        stay_count_gostdom = stays.filter(type__name='Гостевые дома').count()
        stay_count_zona = stays.filter(type__name='Зона отдыха').count()
    elif request.LANGUAGE_CODE == 'en':
        stay_count_otel = stays.filter(type__name='Hotel').count()
        stay_count_sanat = stays.filter(type__name='Sanatorium').count()
        stay_count_gostdom = stays.filter(type__name='Guest house').count()
        stay_count_zona = stays.filter(type__name='Recreation area').count()
    else:
        stay_count_otel = stays.filter(type__name='Қонақ үй').count()
        stay_count_sanat = stays.filter(type__name='Шипажай').count()
        stay_count_gostdom = stays.filter(type__name='Қонақ үйлер').count()
        stay_count_zona = stays.filter(type__name='Демалыс аймағы').count()
    context = {'stays': stays_page, 'n': n, 'types': dic_types,'city_list':city_list,'type_list':type_list,'stars_list':stars_list,
               'cities': dic_cities, 'stars': dic_stars,'MinPrice':MinPrice,'MaxPrice':MaxPrice,
               'stay_count_otel': stay_count_otel,
               'stay_count_sanat': stay_count_sanat, 'stay_count_gostdom': stay_count_gostdom,'hotels':hotels,
               'stay_count_zona': stay_count_zona,
               }
    return render(request, 'stay.html', context)
    #return render(request, 'restaraunt.html', {'eats':eats,'n':n,'city_list':city_list,'type_list':type_list,
    #                                           'MinPrice':MinPrice,'MaxPrice':MaxPrice,
    #                                           'types':dic_types,'cities':dic_cities,
    #                                         'count_restoran':count_restoran,'count_cafe':count_cafe,
    #                                         'count_fast_food':count_fast_food,'count_stolovaia':count_stolovaia})

from itertools import chain




class SearchView(View):


    def get(self, request, *args, **kwargs):
        context = {}

        q = request.GET.get('q')
        if q:
            query_sets = []  # Общий QuerySet

            # Ищем по всем моделям
            query_sets.append(Eat.objects.search(query=q))
            query_sets.append(Stay.objects.search(query=q))
            query_sets.append(Go.objects.search(query=q))
            query_sets.append(News.objects.search(query=q))
            query_sets.append(Tours.objects.search(query=q))
            query_sets.append(Tourists.objects.search(query=q))
            query_sets.append(Akmola.objects.search(query=q))
            # и объединяем выдачу
            final_set = list(chain(*query_sets))
            final_set.sort(key=lambda x: x.date, reverse=True)  # Выполняем сортировку

            context['last_question'] = '?q=%s' % q

            current_page = Paginator(final_set, 6)

            page = request.GET.get('page')
            try:
                context['object_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['object_list'] = current_page.page(1)
            except EmptyPage:
                context['object_list'] = current_page.page(current_page.num_pages)
            context['query'] = q
            context['result_count'] = len(final_set)
            n = current_page.num_pages
            n = range(1, 1 + n)
            context['n']=n
        return render(request=request, template_name='search.html', context=context)

def select_lang(request, code):

    go_next = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(go_next)
    if code and translation.check_for_language(code):
        if hasattr(request, 'session'):
            request.session['django_language'] = code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, code)
        translation.activate(code)
    return response

def tours(request):
    tours = Tours.objects.all()
    a = len(tours)
    short_tours = tours[:3]
    return render(request,'tours.html',{'tours':tours,'short_tours':short_tours,'len':a})

def tours_detail(request,slug):
    tours = Tours.objects.all()
    tour = tours.get(slug=slug)
    return render(request,'tours_detail.html',{'tours':tours,'tour':tour})

def tourists(request):
    tourists = Tourists.objects.all()
    return render(request,'tourists.html',{'tourists':tourists})

def tourists_detail(request,slug):
    tourists = Tourists.objects.all()
    tourist = tourists.get(slug=slug)
    return render(request,'tourists_detail.html',{'tourists':tourists,'tourist':tourist})

def comanda(request):
    comanda = StaticPages.objects.get(slug='komanda-visit-aqmola')
    return render(request,'comanda.html',{'comanda':comanda})

def hotels(request,slug):
    hotel = StaticPages.objects.get(slug=slug)
    return render(request,'comanda.html',{'comanda':hotel})

def gallery(request):
    gallery =  Gallery.objects.all()
    return render(request,'gallery.html',{'photos':gallery})

def type_stay(request,slug):
    stay_list = Stay.objects.all()
    stays = stay_list.filter(type__slug=slug)
    types = TypesStay.objects.get(slug=slug)
    hotels = SidebarToStay.objects.all()
    paginator = Paginator(stays, 6)
    page = request.GET.get('page')
    try:
        stays = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        stays = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        stays = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    if request.LANGUAGE_CODE == 'ru':
        stay_count_otel = stay_list.filter(type__name='Отель').count()
        stay_count_sanat = stay_list.filter(type__name='Санаторий').count()
        stay_count_gostdom = stay_list.filter(type__name='Гостевые дома').count()
        stay_count_zona = stay_list.filter(type__name='Зона отдыха').count()
    elif request.LANGUAGE_CODE == 'en':
        stay_count_otel = stay_list.filter(type__name='Hotel').count()
        stay_count_sanat = stay_list.filter(type__name='Sanatorium').count()
        stay_count_gostdom = stay_list.filter(type__name='Guest house').count()
        stay_count_zona = stay_list.filter(type__name='Recreation area').count()
    else:
        stay_count_otel = stay_list.filter(type__name='Қонақ үй').count()
        stay_count_sanat = stay_list.filter(type__name='Шипажай').count()
        stay_count_gostdom = stay_list.filter(type__name='Қонақ үйлер').count()
        stay_count_zona = stay_list.filter(type__name='Демалыс аймағы').count()
    context = {'stays':stays,'n':n,'stay_count_otel':stay_count_otel,'type':types,'hotels':hotels,
               'stay_count_sanat':stay_count_sanat,'stay_count_gostdom':stay_count_gostdom,'hotels':hotels,
               'stay_count_zona':stay_count_zona,
               }
    return render(request, 'type_stay.html', context)

def type_eat(request,slug):
    eat_list = Eat.objects.all()
    eats = eat_list.filter(type__slug=slug)
    types = TypesEat.objects.get(slug=slug)
    food = NationalFoods.objects.get(pk=1)
    #food = StaticPages.objects.filter(type='where_to_eat')
    paginator = Paginator(eats, 6)
    page = request.GET.get('page')
    try:
        eats = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        eats = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        eats = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    n = range(1, 1 + n)
    if request.LANGUAGE_CODE == 'ru':
        count_restoran = eat_list.filter(type__name='Ресторан').count()
        count_cafe = eat_list.filter(type__name='Кафе').count()
        count_fast_food = eat_list.filter(type__name='Фаст-фуд').count()
        count_stolovaia = eat_list.filter(type__name='Столовая').count()
    elif request.LANGUAGE_CODE == 'kk':
        count_restoran = eat_list.filter(type__name='Дәмхана').count()
        count_cafe = eat_list.filter(type__name='Кафе').count()
        count_fast_food = eat_list.filter(type__name='Фастөфуд').count()
        count_stolovaia = eat_list.filter(type__name='Асхана').count()
    else:
        count_restoran = eat_list.filter(type__name='Restaraunt').count()
        count_cafe = eat_list.filter(type__name='Cafe').count()
        count_fast_food = eat_list.filter(type__name='Fast-food').count()
        count_stolovaia = eat_list.filter(type__name='Canteents').count()

    return render(request,'type_eat.html',{'eats':eats,'type':types,'n':n,'foods':food,
                                             'count_restoran':count_restoran,'count_cafe':count_cafe,
                                             'count_fast_food':count_fast_food,'count_stolovaia':count_stolovaia})

def top_stay(request,slug):
    top = SidebarToStay.objects.get(slug=slug)
    city = top.city
    stays = Stay.objects.filter(isTop=True, city=city)
    return render(request, 'top_stay_detail.html', {'top': top, 'stays': stays})

def national_foods(request):
    foods = NationalFoods.objects.all()
    return render(request,'national_foods.html',{'foods':foods})
