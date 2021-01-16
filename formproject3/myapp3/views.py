from django.shortcuts import render
from myapp3.forms import signup
# Create your views here.
def view1(request):
    f=signup()
    if request.method=="POST":
        f=signup(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            roll=f.cleaned_data['roll']
            email=f.cleaned_data['email']
            phone=f.cleaned_data['phone']
            comments=f.cleaned_data['comments']
            areuengineeringstudent=f.cleaned_data['areuengineeringstudent']
            password=f.cleaned_data['password']
            repassword=f.cleaned_data['repassword']
            d={'name1':name,'roll1':roll,'email1':email,'phone1':phone,'comments1':comments,'areuengineeringstudent1':areuengineeringstudent,'password1':password,'repassword1':repassword}
            return render(request,'myapp3/output.html',d)
    d={'form':f} 
    return render(request,'myapp3/input.html',d)       