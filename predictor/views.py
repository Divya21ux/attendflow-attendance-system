from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserSignIn, Student


# Homepage / front page
def front(request):
    return render(request, 'predictor/front.html')


# Signin page
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "✅ Signed in successfully!")
            UserSignIn.objects.create(username=username, success=True)
            return redirect("predict_attendance")
        else:
            messages.error(request, "❌ Invalid username or password")
            UserSignIn.objects.create(username=username, success=False)

    return render(request, "predictor/signin.html")


# Attendance prediction page
def predict_attendance(request):
    prediction = None
    percentage = None

    if request.method == "POST":
        roll_no = int(request.POST.get("roll"))
        total_classes = int(request.POST.get("total_classes"))
        attended_classes = int(request.POST.get("attended_classes"))

        percentage = (attended_classes / total_classes) * 100 if total_classes else 0

        if percentage < 75:
            prediction = "Low Attendance Risk"
        else:
            prediction = "Safe"

    return render(request, "predictor/index.html", {
        "prediction": prediction,
        "percentage": percentage
    })

#Dashboard page
def dashboard(request):
    return render(request, 'predictor/dashboard.html')