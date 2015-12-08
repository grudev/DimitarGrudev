import pdfkit

# using this script https://github.com/JazzCore/python-pdfkit

options = {
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_file('/Volumes/data/PROJECTS/dimitargrudev.github.io/index.html', '/Volumes/data/PROJECTS/dimitargrudev.github.io/pdf/dimitarGrudevCV.pdf', options=options)
