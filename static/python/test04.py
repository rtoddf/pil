from PIL import Image
import glob, os

infile = 'adamo_ruggiero.png'
file, ext = os.path.splitext(infile)
outfile = file + '.jpg'
if infile != outfile:
	try:
		Image.open(infile).save(outfile)
	except IOError:
		print('cannot convert', infile)