import PyPDF2
import pyttsx3

file = open('Berenice.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(file)

totalpages = pdfReader.numPages
print(f"Total pages: {totalpages}")

from_page = pdfReader.getPage(2)
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
