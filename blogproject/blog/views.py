from django.shortcuts import render,redirect
from .models import Post,category,comment,User
from accounts.models import profile_pic

# Create your views here.
def blog(request):
    posts=Post.objects.filter(is_published=True)
    context={
    'posts':posts,
    }

    return render(request,'blog/blog.html',context)

def post(request,title):

    pos=Post.objects.get(title=title)
    try:
         comts=comment.objects.filter(post=pos).filter(is_resolved=True)
         
    except :
        context={
            'pos':pos,
            }
    else:
        context={
            'pos':pos,
            'comts':comts,

            }
        print(comts)



    return render(request,'blog/post.html',context)

def write_post(request):
    cat=category.objects.all()
    cats={
    'cat':cat
    }
    if request.method=='POST':
        pos_title=request.POST['post_title']
        tag=request.POST['tag']
        catii=request.POST['cati']
        ca=category.objects.get(id=catii)
        post_disp=request.POST['post_disp']
        u_id=request.POST['id']
        u=User.objects.get(id=u_id)
        thumbnaill_img = request.FILES.get('thumbnail_img')
        posttt=Post(categoryy=ca,title=pos_title,tags=tag,user=u,discreption=post_disp,thumbnail=thumbnaill_img,is_published=True)
        posttt.save()
        print(thumbnaill_img)
        return redirect('write_post')

    return render(request,'blog/write_post.html',cats)

def postcomment(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        commentt=request.POST['comment']
        t_id=request.POST['id']
        p=Post.objects.get(id=t_id)
        c=comment(namee=name ,email=email,comment=commentt,post=p,is_resolved=True)
        c.save()
        return redirect('post',title=p.title)
