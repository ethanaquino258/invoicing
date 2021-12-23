from django import forms

class BilledItemForm(forms.Form):
  description = forms.CharField(label='Description', max_length=255)

class InvoiceForm(forms.Form):
  title = forms.CharField(label='Title', max_length=255)
  date = forms.DateField(label='Date')
  due_date = forms.DateField(label='Due Date')
  billedItem = BilledItemForm

