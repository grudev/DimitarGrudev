import pdfkit

# 1. Run in terminal: sudo easy_install pip
# 2. Then do: brew install Caskroom/cask/wkhtmltopdf
# 3. Adjust file paths from the current file below
# 4. Go to the same directory where this python script exists on your mac
# 5. Run: python exportToPDF.py

# using this script https://github.com/JazzCore/python-pdfkit

options = {
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_file('/Users/grudev/data/PROJECTS/grudev.github.io/index-pdf.html', '/Users/grudev/data/PROJECTS/grudev.github.io/pdf/dimitarGrudevCV.pdf', options=options)
