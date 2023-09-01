from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image_filter_choices = [
        ('argentina', 'Argentina'),
        ('bolivia', 'Bolivia'),
        ('canary_islands', 'Canary Islands'),
        ('chile', 'Chile'),
        ('colombia', 'Colombia'),
        ('costa_rica', 'Costa Rica'),
        ('cuba', 'Cuba'),
        ('dominican_republic', 'Dominican Republic'),
        ('ecuador', 'Ecuador'),
        ('el_salvador', 'El Salvador'),
        ('equatorial_guinea', 'Equatorial Guinea'),
        ('guatemala', 'Guatemala'),
        ('honduras', 'Honduras'),
        ('mexico', 'Mexico'),
        ('nicaragua', 'Nicaragua'),
        ('panama', 'Panama'),
        ('paraguay', 'Paraguay'),
        ('peru', 'Peru'),
        ('spain', 'Spain'),
        ('uruguay', 'Uruguay'),
        ('venezuela', 'Venezuela'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_jwxvtb', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
