from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# 使用图像分割技术对同区域两个时期的卫星图像变化情况完成分析
def detect_change(request):
    if request.method == 'POST':
        image1 = request.FILES.get('pre_image')
        image2 = request.FILES.get('post_image')
        pre_image = open(image1.name, mode='wb')
        post_image = open(image2.name, mode='wb')
        for chunk in image1.chunks():
            pre_image.write(chunk)
        for chunk in image2.chunks():
            post_image.write(chunk)
        '''change detection'''
        # 图像送进模型推理，返回单通道灰度图

        pre_image.close()
        post_image.close()


@csrf_exempt
# 使用图像分割技术对卫星图像中指定对象完成分割
def extract_object(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        object_image = open(image.name, mode='wb')
        for chunk in image.chunks():
            object_image.write(chunk)
        '''object extraction'''
        # 图像送进模型推理，然后对指定对象部分进行语义分割级渲染

        object_image.close()


@csrf_exempt
# 使用目标检测技术对卫星图像中指定对象完成检测
def detect_object(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        object_image = open(image.name, mode='wb')
        for chunk in image.chunks():
            object_image.write(chunk)
        '''object detection'''
        # 图像送进模型推理，然后返回指定对象的坐标，对该部分进行对应颜色渲染

        object_image.close()


@csrf_exempt
# 使用图像分割技术对卫星图像每个像素完成分类
def classify_pixel(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        whole_image = open(image.name, mode='wb')
        for chunk in image.chunks():
            whole_image.write(chunk)
        '''classify the image'''
        # 图像送进模型推理，然后逐像素分类进行渲染

        whole_image.close()
