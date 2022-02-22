from glob import glob
from pdf2image import convert_from_path

pdffiles = glob("*.pdf")

for j, pdffile in enumerate(pdffiles):

	images = convert_from_path(pdffile, 250)

	for i, image in enumerate(images):
		image.save(f'save_{j}_{i}.png')      
