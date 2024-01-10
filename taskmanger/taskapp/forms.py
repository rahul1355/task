from django import forms 
from taskapp.models import tasklist

class taskListForm(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = ['task_name','assingned_to','assigned_by','priority']
        
class editTaskForm(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = ['task_name','assingned_to','priority']