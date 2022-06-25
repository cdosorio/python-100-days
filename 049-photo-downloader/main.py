# -*- coding: utf-8 -*-
from lxml import html
from os import mkdir
from os.path import basename, exists
from sys import argv
from requests import get
# SETUP PACKS FOLDER HERE
packsFolder = './img/'
def run():
    if len(argv) < 3:
        print('[ERROR] Folder name not given!')
        print('[ERROR] wines.cl url not given!')
        exit()
      
    if not 'https://www.wines.cl/temas/' in argv[2]:
        exit('[ERROR] Given URL do not match to Wines.cl!')
      
    packOutFolder = f"{packsFolder}{argv[1]}"
  
    # ADD / AT END OF PATH
    if packOutFolder[-1] != '/':
        packOutFolder += '/'
      
    # CREATE FOLDER
    if not exists(packOutFolder):
        print(f"[INFO] Creating: '{packOutFolder}'...", end='')
        mkdir(packOutFolder)
        print('[DONE]')
    # REQUEST HTML
    r = get(argv[2])
    if r.status_code == 200:
        dom = html.fromstring(r.text)
        imgList = dom.cssselect('#messageList')[0] \
            .cssselect('li')[0] \
            .cssselect('blockquote.messageText')[0] \
            .cssselect('img.bbCodeImage')
        imgLinks = [img.get('data-src') for img in imgList]
      
        # DOWNLOAD PHOTOS
        if len(imgLinks) > 0:
            print(f"[INFO] {len(imgLinks)} photos found!")
          
            for imgLink in imgLinks:
                imgName = f"{packOutFolder}{basename(imgLink)}"
              
                print(f"[INFO] Downloading: {imgLink}...", end='')
              
                # AVOID IF ALREADY EXISTS
                if exists(imgName):
                    print('[AVOID: ALREADY EXISTS!]')
                    continue
              
                with get(imgLink, stream=True) as imgR:
                    if imgR.status_code == 200:
                        with open(imgName, 'wb') as imgFile:
                            for chunk in imgR.iter_content(chunk_size=8192):
                                imgFile.write(chunk)
                        print('[COMPLETE]')
                    else:
                        print(f"[ERROR: HTTP CODE {imgR.status_code}]")
        else:
            print('[INFO] No photos found in first thread!')
              
    else:
        exit("\n[ERROR] HTTP_CODE: " + r.status_code)
      
# CLI PARAMETERS
# 1: FOLDER NAME INSIDE packsFolder
# 2: WINES LINK
if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        print('\n\n...Aborted!')