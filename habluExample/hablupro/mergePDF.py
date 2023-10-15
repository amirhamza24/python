from PyPDF2 import PdfMerger

allpdf = ["cv.pdf", "resume.pdf"]

ourMerger = PdfMerger()

for newPdf in allpdf:
    ourMerger.append(newPdf)

ourMerger.write("adding.pdf")
ourMerger.close()