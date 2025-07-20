from django import forms
from tasks.models import Task
#Django Form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label='Assigned To')

    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        employee = kwargs.pop("employees", [])
        print(employee)
        super().__init__(*args, **kwargs)
        print(self.fields)
        self.fields['assigned_to'].choices=[(emp.id, emp.name) for emp in employee]

#Django Model Form
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tilte', 'description', 'due_date', 'assigned_to']
        #we can use exclude, when we will have many fields and we do not need some fields, then we can write those some names and others will automatically be added
        widgets ={
            'tilte' : forms.TextInput(attrs={
                'class' : "w-1/2 border-blue-500  border-2 bg-blue-100",
                'placeholder' : "Enter the title"
            }),
            'description' : forms.Textarea(attrs={
                'class' : " mt-2 border-blue-500 border-2 bg-blue-100",
                'placeholder' : "Enter the Description"
            }),
            'due_date': forms.SelectDateWidget(attrs={
                'class' : "border-2 border-red-500 bg-blue-200"
            }),
            'assigned_to': forms.CheckboxSelectMultiple
        }