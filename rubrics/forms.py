from django import forms

from .models import ReviewsStay,ReviewsEat

class ReviewsEatForm(forms.ModelForm):
    class Meta:
        model = ReviewsEat
        fields = ('name','email','text')

class ReviewsStayForm(forms.ModelForm):
    class Meta:
        model = ReviewsStay
        fields = ('name','email','text')