import string
from django.shortcuts import render, redirect

from image_saver.settings import BASE_DIR, IMAGES_URL, PROJECT_ROOT
from .forms import *
import cv2 as cv2
import os
import pandas as pd


# Create your views here.


def upload_image(request):

    if request.method == 'POST':
        form = ImageModelForm(request.POST, request.FILES)

        if form.is_valid():
            model = form.save()
            # url = os.path.join(IMAGES_URL,"rice.jpeg")
            image_url = str(model.image)
            print(image_url)
            img = cv2.imread(image_url)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                if (w < 20 or h < 20): continue
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                df = cv2.putText(img, "W: {}, H: {}".format(w, h), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(df)

            cv2.imshow("Rice Detection", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return redirect('upload_image')
            # return Response('upload_image')
    else:
        form = ImageModelForm()
    return render(request, 'image_form.html', {'form': form})
