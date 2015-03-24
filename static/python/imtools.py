from PIL import Image
import os

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

in_path = '../images'
out_path = in_path + '/black_n_white/'
list = get_imlist(in_path)

for infile in list:
    file, ext = os.path.splitext(infile)
    im = Image.open(infile).convert('L')
    outfile = out_path + (file + '.jpg').split('/')[-1]
    im.save(outfile)