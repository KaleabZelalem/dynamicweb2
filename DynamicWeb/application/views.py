from django.shortcuts import render, HttpResponse
from .models import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage
from .models import AboutContent
# Create your views here.
def home(request):
    movies = Movie.objects.all()
    data = {'movies': movies}
    return render(request, 'home.html', data)

def about(request):
    # Check if content already exists in the database
    if AboutContent.objects.exists():
        about_content = AboutContent.objects.first()
    else:
        # If not, create new content
        about_content = AboutContent(
            description='Welcome',
            about_paragraph="""
                Welcome to our Website, your ultimate destination for curated movie lists that cater to every film enthusiast's taste. 
                At this Website, we take pride in delivering a personalized and engaging cinematic experience by offering carefully curated 
                lists of top movies, categorized based on genres and release dates. Our team of passionate movie aficionados is dedicated 
                to bringing you the best of the film world, ensuring that you always stay in the loop with the latest releases and timeless 
                classics. Whether you're a fan of heartwarming dramas, pulse-pounding thrillers, or side-splitting comedies, we have 
                meticulously crafted lists to suit every mood and preference.
                Whether you're a seasoned movie buff or just starting your cinematic journey, [Your Website Name] is your go-to resource 
                for discovering, appreciating, and enjoying the best of cinema. Thank you for being part of our community, and we look 
                forward to being your trusted companion on your cinematic exploration.
            """,
            mission='Our mission is to provide a comprehensive and engaging movie discovery experience.',
        )
        about_content.save()

    context = {
        'website_name': 'My Movies',
        'description': about_content.description,
        'mission': about_content.mission,
        'about_paragraph': about_content.about_paragraph,
    }

    return render(request, 'about.html', context)



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the message to the database
            ContactMessage.objects.create(name=name, email=email, message=message)

            send_mail(
                f'Message from {name}',
                message,
                email,
                ['zz.kaleab@gmail.com'],  # your email address
            )
            return redirect('success')  # Redirect to a success page or home
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


    
    

def movies(request):
    return render(request, 'movies.html')
