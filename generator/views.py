# Import necessary modules
from django.shortcuts import render
import random

# Add your views here

# Define the home view function
def home(request):
    # `request` is an instance of the `HttpRequest` class
    # You can access various properties and methods of the `request` object
    # to handle the incoming request and generate an appropriate response.


    # Create a dictionary called 'context' with some data
    context = {
        'weak_range': range(6, 16),  # A range of numbers from 6 to 15
        'strong_range': range(16, 129),  # A range of numbers from 16 to 128
        'unbelievable_range': [256, 512, 1024, 2048],  # A list of specific numbers
    }

    # Render the 'generator/home.html' template with the 'context' data
    return render(request, 'generator/home.html', context)

# Define the password view function
def password(request):
    # Define lists of characters: lowercase letters, uppercase letters, numbers, and symbols
    lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
    upper_case_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    # Get the desired password length from the request (default is 16)
    length = int(request.GET.get('length', 16))

    # Initialize the available characters with lowercase letters
    available_chars = lower_case_letters

    # If the user wants uppercase letters, add them to the available characters
    if request.GET.get('uppercase'):
        available_chars += upper_case_letters

    # If the user wants numbers, add them to the available characters
    if request.GET.get('numbers'):
        available_chars += numbers

    # If the user wants symbols, add them to the available characters
    if request.GET.get('symbols'):
        available_chars += symbols

    # Generate a random password by choosing characters from the available set
    password = ''
    for _ in range(length):
        password += random.choice(available_chars)

    # Render the 'generator/password.html' template with the generated password
    return render(request, 'generator/password.html', {'password': password})
