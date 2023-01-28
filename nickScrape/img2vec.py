# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:07:45 2023

@author: Nick Cheng
@uses: https://github.com/christiansafka/img2vec
"""

from img2vec_pytorch import Img2Vec
from PIL import Image
import requests
from io import BytesIO

img2vec = Img2Vec()

def imgDist(url1, url2):
    # Read in an image (rgb format)
    # Get a vector from img2vec, returned as a torch FloatTensor
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    img1 = Image.open(BytesIO(r1.content)).convert('RGB')
    img2 = Image.open(BytesIO(r2.content)).convert('RGB')
    vec1 = img2vec.get_vec(img1, tensor=True)
    vec2 = img2vec.get_vec(img2, tensor=True)
    
    return ((vec1-vec2)**2).sum().numpy()

#print(imgDist("https://www.applesfromny.com/wp-content/uploads/2020/05/20Ounce_NYAS-Apples2.png",
#              "https://images.craigslist.org/00L0L_vlGovQnxpQz_0wg0qa_300x300.jpg"))