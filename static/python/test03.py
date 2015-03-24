from PIL import Image
import glob, os

# size = 128, 128

for infile in glob.glob('*.jpg'):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile).convert('L')
    # im.thumbnail(size, Image.ANTIALIAS)
    outfile = file + '_bw.jpg'
    im.save(outfile)