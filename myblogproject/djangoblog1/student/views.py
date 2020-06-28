from django.http import HttpResponse
from django.shortcuts import render

def HelloWorld (request):
    return HttpResponse("hi I Am Zakir Hossain")

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

student = {
    1: {
        "name":"Zakir",
        "age":18,
        "gender": "male",
        "roll": 1,
    },
    2: {
        "name": "Rohim",
        "age": 17,
        "gender": "male",
        "roll": 2,
    },
    3: {
        "name": "Ron",
        "age": 16,
        "gender": "male",
        "roll": 3,
    },
    4: {
        "name": "Kamal",
        "age": 19,
        "gender": "male",
        "roll": 4,
    },
}

students = [

    {
        "name":"Zakir",
        "age":18,
        "gender": "male",
        "roll": 1,
    },
    {
        "name": "Rohim",
        "age": 17,
        "gender": "male",
        "roll": 2,
    },
    {
        "name": "Ron",
        "age": 16,
        "gender": "male",
        "roll": 3,
    },
    {
        "name": "Kamal",
        "age": 19,
        "gender": "male",
        "roll": 4,
    },
]

def student_list(request):
    return render(request, 'student/list.html', {'student_list': students})

def student_detail(request, roll):
    std = student[roll]
    context = {
        'student':std
    }
    return render(request, 'student/detail.html', context)
