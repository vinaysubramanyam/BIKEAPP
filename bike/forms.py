from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from bike.models import Page, Category

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()
	


# class SignUpForm(forms.ModelForm):

# 	class Meta:
# 		model = SignUp
# 		fields = ['full_name', 'email', 'password'] 

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
	
# 		if not "com" in email:
# 			raise forms.ValidationError("please use a valid email address")
# 		return email

# 	def clean_full_name(self):
# 		full_name = self.cleaned_data.get('full_name')
# 		return full_name

# 	password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
	
# 	helper = FormHelper()
# 	helper.form_method = 'POST'
# 	helper.add_input(Submit('login', 'login', css_class='btn-primary'))

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        # fields = ('title', 'url', 'views')
        def clean(self):
        	cleaned_data = self.cleaned_data
        	url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        	if url and not url.startswith('http://'):
        		url = 'http://' + url
            	cleaned_data['url'] = url

        	return cleaned_data
