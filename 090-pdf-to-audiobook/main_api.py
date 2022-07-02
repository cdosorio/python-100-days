import PyPDF2
from gtts import gTTS
from pathlib import Path
import os

# The text that you want to convert to audio
file = open('Berenice.pdf', 'rb')
filename_noext = Path(file.name).stem
filename_mp3 = f"{filename_noext}.mp3"

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(file)

totalpages = pdfReader.numPages
print(f"Total pages: {totalpages}")

from_page = pdfReader.getPage(0)
mytext = from_page.extractText()

# Convert to mp3 file
language = 'es-us'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(filename_mp3)

# Playing the converted file
os.system(filename_mp3)
