from PIL import Image
import glob, os

infile = 'adamo_ruggiero.jpg'
file, ext = os.path.splitext(infile)
im = Image.open(infile).convert('L')
outfile = file + '_bw.jpg'
im.save(outfile)

# size = 128, 128
# for infile in glob.glob('*.jpg'):
# 	file, ext = os.path.splitext(infile)
# 	im = Image.open(infile)
# 	im.thumbnail(size, Image.ANTIALIAS)
# 	outfile = file + '_thumbnail.jpg'
# 	im.save(outfile)