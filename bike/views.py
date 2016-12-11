from django.shortcuts import render
from django.conf import settings
# from .forms import SignUpForm, ContactForm
from bike.forms import ContactForm, CategoryForm
from django.core.mail import send_mail
# from .models import SignUp
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from bike.models import Page



def home(request):
	# title = 'Sign Up'

	# form = SignUpForm(request.POST or None)
	

	# context = {
	# 	"title": title,
	# 	"form": form,
	# }

	#add a form
	# if request.method == "post":
	# 	print (request.POST)
	

	# if form.is_valid():
	# 	# form.save()
	# 	instance =form.save(commit=False)

	# 	full_name = form.cleaned_data.get("full_name")
	# 	if not full_name:
	# 		full_name = "New full_name"
	# 	instance.full_name=full_name

	# 	instance.save()
	# 	# print(instance)
	# 	# print(instance.timestamp)
	# 	context = {
	# 		"title": "Thank You"
	# 	}

	# 	return render(request,"private.html",context)

	# if request.user.is_authenticated() and request.user.is_staff:
	# 	# print(SignUp.objects.all())
	# 	# i = 1
	# 	# for instance in SignUp.objects.all():
	# 	# 	print(i)
	# 	# 	print(instance.full_name)
	# 	# 	i+=1
	# 	queryset=SignUp.objects.all().order_by('-timestamp')
	# 	context = {
	# 		"queryset": queryset
	# 	}

	
	return render(request,"home.html")


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'vinaygallaxhar@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
	}
	return render(request, "forms.html", context)


def Category(request, category_name_slug):

	context_dict={}
	try:
		category=Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		pages = Page.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		
		context_dict['category'] = category
	except:

        
		pass

    # Go render the response and return it to the client.
	return render(request, 'category.html', context_dict)




def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'news.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'add_category.html', {'form': form})



