from django.contrib import admin
from django import forms

from django.utils.safestring import mark_safe


from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class GoInline(admin.TabularInline):
    model = GoPhotos
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.images.url} width="120" height="120" ')
    get_image.short_description = "Photo"


class StayInline(admin.TabularInline):
    model = StayPhoto
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.images.url} width="120" height="120" ')
    get_image.short_description = "Photo"

class EatInline(admin.TabularInline):
    model = EatPhotos
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.images.url} width="120" height="120" ')
    get_image.short_description = "Photo"

class StayReviewsInline(admin.TabularInline):
    model = ReviewsStay
    extra = 1

class EatReviewsInline(admin.TabularInline):
    model = ReviewsEat
    extra = 1

class StaticPagesAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = StaticPages
        fields = '__all__'

class ToursAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Tours
        fields = '__all__'

class TouristsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Tourists
        fields = '__all__'

class EventsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Events
        fields = '__all__'

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class AkmolaAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Akmola
        fields = '__all__'

admin.site.register(EatPhotos)
admin.site.register(GoPhotos)
admin.site.register(StayPhoto)
admin.site.register(Cities)
admin.site.register(Gallery)
admin.site.register(TypesGo)
admin.site.register(NationalFoods)

@admin.register(SidebarToStay)
class SidebarToStay(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(TypesStay)
class TypesStay(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
@admin.register(TypesEat)
class TypesStay(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



@admin.register(Akmola)
class AkmolaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = AkmolaAdminForm

@admin.register(Eat)
class EatAdmin(admin.ModelAdmin):
    list_display = ('title','city','type','price','phone','get_image')
    list_filter = ('city','type','price')
    prepopulated_fields = {'slug':('title',)}
    inlines = [EatInline,EatReviewsInline]

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.thumbnail.url} width="60" height="60" ')
    get_image.short_description = "Photo"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    form = NewsAdminForm
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title','date','address')
    prepopulated_fields = {'slug': ('title',)}
    form = EventsAdminForm

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    form = ToursAdminForm
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Tourists)
class TouristsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    form = TouristsAdminForm
    prepopulated_fields = {'slug': ('title',)}

@admin.register(StaticPages)
class StaticPagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    form = StaticPagesAdminForm
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Go)
class GoAdmin(admin.ModelAdmin):
    list_display = ('title','city','type','phone','get_image')
    list_filter = ('city','type')
    inlines = [GoInline]
    prepopulated_fields = {'slug':('title',)}
    
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.thumbnail.url} width="60" height="60" ')
    get_image.short_description = "Photo"

@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ('title','city','type','price','phone','get_image','isTop')
    list_editable = ('isTop',)
    list_filter = ('city','type','price','stars')
    prepopulated_fields = {'slug':('title',)}
    inlines = [StayInline,StayReviewsInline]
    
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.thumbnail.url} width="60" height="60" ')
    get_image.short_description = "Photo"

@admin.register(ReviewsEat)
class ReviewsEatAdmin(admin.ModelAdmin):
    list_display = ('name','email','rubric')
    readonly_fields = ('name','email','rubric','date')

@admin.register(ReviewsStay)
class ReviewsStayAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rubric')
    readonly_fields = ('name', 'email', 'rubric', 'date')
