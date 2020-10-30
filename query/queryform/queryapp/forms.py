from django import forms

class QueryForm(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    mail_id = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    query = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter ur query'}))

    def clean_query(self):
        input_query=self.cleaned_data['query']
        f = open("queryapp/words.txt",'r') 
        blacklist=f.read().splitlines()

        for disposable_feedback in blacklist:
            if disposable_feedback in input_query:
                raise forms.ValidationError("Your query message contains insensitive/abusive words. please check" )
        return input_query