from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class TeamColor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color_code = models.CharField(max_length=7, help_text="Hex color code (e.g., #FF0000)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def clean(self):
        # Validate hex color code
        if not self.color_code.startswith('#'):
            raise ValidationError('Color code must start with #')
        if len(self.color_code) != 7:
            raise ValidationError('Color code must be 7 characters long (including #)')
        try:
            int(self.color_code[1:], 16)
        except ValueError:
            raise ValidationError('Color code must be a valid hex color')


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.ForeignKey(TeamColor, on_delete=models.PROTECT, related_name='teams', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.color.name})"
    
    def get_total_score(self):
        return self.score_entries.aggregate(
            total=models.Sum('points')
        )['total'] or 0


class ScoreEntry(models.Model):
    SCORE_TYPES = [
        ('merit', 'Merit'),
        ('demerit', 'Demerit'),
    ]
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='score_entries')
    score_type = models.CharField(max_length=10, choices=SCORE_TYPES)
    points = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.team.name} - {self.get_score_type_display()}: {self.points} pts"
