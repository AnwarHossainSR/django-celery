from django.shortcuts import render
from core.celery import add
from celery.result import AsyncResult


# Enqueue Task using delay()
# def home(request):
#     print("Results: ")
#     result1 = add.delay(10, 20)
#     print("Result 1: ", result1)
#     result2 = sub.delay(80, 10)
#     print("Result 2: ", result2)
#     return render(request, "myapp/home.html")

# # Enqueue Task using apply_async()
# def home(request):
#     print("Results: ")
#     result1 = add.apply_async(args=[10, 20])
#     print("Result 1: ", result1)
#     result2 = sub.apply_async(args=[80, 10])
#     print("Result 2: ", result2)
#     return render(request, "myapp/home.html")


# Display addition value after task execution
def home(request):
    result = add.delay(100, 30)
    return render(request, "myapp/home.html", {'result': result})


def about(request):
    return render(request, 'myapp/about.html')


def contact(request):
    return render(request, 'myapp/contact.html')


def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    # print("Ready: ", result.ready())
    # print("Successful: ", result.successful())
    # print("Failed: ", result.failed())
    # print("Get: ", result.get())
    return render(request, 'myapp/result.html', {'result':result})