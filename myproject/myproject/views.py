from django.http import HttpResponse
from django.shortcuts import render

def HelloWorld (request):
    return HttpResponse("hi I Am Zakir Hossain")

def abcd(request):
    return HttpResponse("Hellow how are your?")

def abcd(request, name):
    # str = "Hellow how are {}". format(name)
    str = f"Hello how are {name}"
    return HttpResponse(str)

def abcd(request, name1, name2):

    sum = int(name1) + int(name2)
    print(type(sum))
    return HttpResponse(sum)

def contact(request):
    context={
        "Students":[{

            "class1": [
                {
                    "name": "Harun",
                    "roll": 1,
                },
                {
                    "name": "Jamal",
                    "roll": 2,
                },
            ],

            "class2": [
                {
                    "name": "Mohin",
                    "roll": 1,
                },
                {
                    "name": "Fahim",
                    "roll": 2,
                },
            ]
        }]
    }
    return render(request,'contact.html', context)

def blog(request):
    return render(request,'blog.html')

def home(request):
    context={
        "Students":[{

            "class1": [
                {
                    "name": "Harun",
                    "roll": 1,
                },
                {
                    "name": "Jamal",
                    "roll": 2,
                },
                {
                    "name": "Zakir",
                    "roll": 3,
                },
                {
                    "name": "Rohim",
                    "roll": 4,
                },
                {
                    "name": "Shetu",
                    "roll": 5,
                },
                {
                    "name": "Rahman",
                    "roll": 6,
                },
            ],

            "class2": [
                {
                    "name": "Mohin",
                    "roll": 1,
                },
                {
                    "name": "Fahim",
                    "roll": 2,
                },
                {
                    "name": "Jamal",
                    "roll": 3,
                },
                {
                    "name": "Joynal",
                    "roll": 4,
                },
                {
                    "name": "Salam",
                    "roll": 5,
                },
                {
                    "name": "Zabber",
                    "roll": 6,
                },

                {
                    "name": "Kalam",
                    "roll": 7,
                },
                {
                    "name": "Khokon",
                    "roll": 8,
                },
                {
                    "name": "Tumpa",
                    "roll": 9,
                },
                {
                    "name": "Kudus",
                    "roll": 10,
                },
            ]
        }]
    }
    return render(request,'index.html',context)
