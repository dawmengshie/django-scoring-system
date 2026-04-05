from django import forms
from .models import Team, ScoreEntry, TeamColor


class ScoreEntryForm(forms.ModelForm):
    class Meta:
        model = ScoreEntry
        fields = ['team', 'points', 'description']
        widgets = {
            'team': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'points': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'min': '0'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.all()
        self.fields['team'].empty_label = "Select a team"
        self.fields['points'].label = "Points"


class TeamColorForm(forms.ModelForm):
    class Meta:
        model = TeamColor
        fields = ['name', 'color_code']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., Red, Blue, Green'
            }),
            'color_code': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '#FF0000',
                'type': 'color'
            }),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            # Check for case-insensitive duplicate
            if TeamColor.objects.filter(name__iexact=name).exclude(id=self.instance.id if self.instance else None).exists():
                raise forms.ValidationError('A team color with this name already exists.')
        return name


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Team name'
            }),
            'color': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].queryset = TeamColor.objects.all()
        self.fields['color'].empty_label = "Select a color"
