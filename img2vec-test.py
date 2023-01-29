from img2vec_pytorch import Img2Vec
from PIL import Image

# Initialize Img2Vec with GPU
img2vec = Img2Vec(cuda=False)

# Read in an image (rgb format)
img = Image.open('https://images.craigslist.org/00t0t_dUxbE6HM8er_0CI0t2_300x300.jpg')
# Get a vector from img2vec, returned as a torch FloatTensor
vec = img2vec.get_vec(img, tensor=True)
