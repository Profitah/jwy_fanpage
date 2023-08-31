from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request ,'main.html')

def community(request):
    return render (request, 'community.html')

def firstpage(request):
    return render (request, 'firstpage.html')

def gallery(request):
    return render (request, 'gallery.html')

def my_view(request):
    my_image_path = 'img/firstpagewy.jpeg'  # 이미지의 상대 경로
    my_image_url = static(my_image_path)
    
    context = {'my_image': my_image_url}
    return render(request, 'template.html', context)