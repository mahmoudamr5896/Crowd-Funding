
from django.utils import timezone
from django.db import models
from users.models import User
from taggit .managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    images=models.ImageField(blank=True)
    def __str__(self):
        return self.title

class Picture(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')  

    def __str__(self):
        return self.project.title
  
      
class SimilarProject(models.Model):
    base_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='base_project')
    similar_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='similar_project')


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    

class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    

class ProjectReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()

class CommentReport(models.Model):
    REASON_CHOICES = [
        ('Inappropriate', 'Inappropriate Content'),
        ('Spam', 'Spam or Advertising'),
        ('Abusive', 'Abusive or Offensive'),
        ('Other', 'Other'),
    ]
    
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    details = models.TextField(blank=True)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Report by {self.user} on {self.created_at}"
    
class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=RATING_CHOICES)


class FeaturedProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # Add other fields as needed


    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=5, decimal_places=2)