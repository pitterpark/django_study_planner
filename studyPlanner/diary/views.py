from tabnanny import check
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect

from django.shortcuts import render,redirect
from django.contrib import auth

# Create your views here.
def diary(request):
    # todothing
    todo_lists = Todothing.objects.all()
    todo_form = TodothingForm()
    #서버의 write 클래스 정보를 모두 가져온다.

    return render(request, 'diary_main.html', {
        'todo_lists' : todo_lists,
        'todo_form' : todo_form,
    })

def addTodo(request):
    if request.method == 'POST':
        todo_form = TodothingForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('diary:diary')
    else:
        todo_form = TodothingForm()
    return render(request, "diary:diary_main", {'todo_form' : todo_form})


def checkedTodo(request):
    checked = request.POST.getlist('checked') # html에서 체크한 목록의 id값 리스트로 받아오기
    # 체크한 id값에 해당하는 checkbox = True로 수정하기
    for id in checked:
        id = int(id) # 리스트 내의 요소를 문자열에서 정수로 바꾸기
        todo_list = get_object_or_404(Todothing, pk=id)
        # 체크된 것을 True로 바꿔주기
        todo_list.checkbox = True
        todo_list.save() # 모델의 필드 저장
    return redirect('diary:diary')


        



    

        
    
    return render(request, 'diary_main.html')

def logout(request):
    auth.logout(request)
    return redirect('diary:diary')
