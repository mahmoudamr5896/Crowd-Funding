# forms.py
from django import forms
from .models import CommentReport, Picture, Project, Comment, Donation, ProjectReport, Report, Rating


class ImageForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image']      

class ProjectForm(forms.ModelForm):
    ImageFormSet = forms.inlineformset_factory(Project, Picture, form=ImageForm, extra=3)
    tags = forms.CharField(label='Tags', required=False, help_text='Enter tags separated by commas')
    
    class Meta:
        model = Project
        fields = ['title', 'details', 'tags', 'category', 'total_target', 'start_time', 'end_time','images']



     

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
 

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']
        
class ProjectReportForm(forms.ModelForm):
    class Meta:
        model = ProjectReport
        fields = ['reason']

class CommentReportForm(forms.ModelForm):
    class Meta:
        model = CommentReport
        fields = ['reason', 'details']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        widgets = {
            'value': forms.Select(choices=Rating.RATING_CHOICES)
        }
