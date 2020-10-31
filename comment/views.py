from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.core import serializers
from .forms import CommentForm, CommentPopupForm, SubCommentForm
from .models import Comment, CommentLike, SubComment
from account.models import Account

# Create your views here.
@login_required
def index(request):
    form = CommentForm()
    formpopup = CommentPopupForm()
    formsubcomment = SubCommentForm()
    comments = Comment.objects.annotate(count=Count('likes')).order_by('-count')
    context ={
        'form' : form,
        'formpopup' : formpopup,
        'comments':comments,
        'formsubcomment' : formsubcomment,
        'user' : request.user,
    }
    return render(request, 'comment/index.html', context)


@login_required
def profile(request):
    comments = Comment.objects.filter(user_id=request.user).all()
    context={
        'comments':comments,
        'user':request.user
    }
    return render(request, 'comment/profile.html', context)

@login_required
def subcommentlist(request, id):
    if request.method == "GET":
        comments = Comment.objects.filter(id=id).first().subcomments.all()
        #qs_json = serializers.serialize('json', comments )
        data = json.dumps( [{'subcomment': comment.subcomment,'UserFL': comment.User.first_name+" "+comment.User.last_name,
                            'UserNick':comment.User.username,'subcomment_id':comment.id, 'date': str(comment.date),
                            'picture': str(comment.picture)} for comment in comments])
        return JsonResponse(data, safe=False)
        #return JsonResponse({'comments':qs_json}, safe=False,content_type='application/json')

@login_required
def get_likes_count(request, id):
    if request.method == "GET":
        likes = Comment.objects.filter(id=1).first().likes.all()
        like ={'like':likes.count()}
        return JsonResponse(like)

@login_required
def subcommentadd(request):
    if request.method == "POST":
        subcomment = SubComment(User=request.user, subcomment=request.POST['subcomment'])
        if(request.FILES):
            subcomment.picture = request.FILES['picturesubcomment']
        subcomment.save()
        comment = Comment.objects.filter(id=request.POST['id']).first()
        comment.subcomments.add(subcomment)
        comment.save()
        message = 'Başarılı!'
        status = 200
        return HttpResponse(json.dumps({'message': message, status:status}))


@login_required
def commentadd(request):
    if request.method == "POST":
        #body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)
        try:
            newcomment = Comment(user_id=request.user,comment = request.POST['comment'])
            if(request.FILES):
                newcomment.picture =request.FILES['picture']
            newcomment.save()
            message = 'Kayıt Başarılı'
            status = 200
        except:
            message = 'Hata'
            status = 400
        return HttpResponse(json.dumps({'message': message, status:status}))

@login_required
def commentlike(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        comment = Comment.objects.filter(id=int(body['id'])).first()
        if not comment.likes.filter(id=request.user.id).first():
            like = CommentLike(user=request.user, comment=comment)
            like.save()
            comment.likes.add(request.user)
            comment.save()
            status=200
        else:
            user=comment.likes.filter(id=request.user.id).first()
            comment.likes.remove(user)
            like = CommentLike.objects.filter(user=request.user.id,comment=comment.id).first()
            like.delete()
            status=201
        return HttpResponse(json.dumps({'message': 'success','status':status}))

@login_required
def recomment(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        recommnet = Comment.objects.filter(id=body['id']).first()
        newcomment = Comment(user_id=request.user, comment=body['comment'],parent=recommnet)
        newcomment.save()
        return HttpResponse(json.dumps({'message':'success'}))
