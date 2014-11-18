#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys, zipfile, os, shutil, glob, textwrap
from os.path import join
from xml.etree import ElementTree as ET
import html5lib
import argparse
#####
# EDITING AFTER ITS CREATION, TO:
###

## STEP 1: unzip epub
filename = sys.argv[1]
pos_filename = sys.argv[1]#(filename.replace(".epub",""))+"_post.epub"

# unzip ePub
fh = open(str(filename), 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "temp"
    z.extract(name, outpath)
fh.close()

## STEP 2:  Do Changes

### Changes defs
def fn_rm_sup(tree, element):
    for fn in tree.findall(element):
#        print ET.tostring(fn)
        for child in list(fn):
            if child.tag == 'sup':                
                number = child.text
#                print child
#                child.clear() # STILL LEAVING </sup>
                fn.remove(child)
                fn.text=number

def figure(tree, element): # insert <div> inside <figure> tp wrap <img>
    print '     adding <div class="fig"> to <figure>'
    for tag in tree.findall(element):
        figure = tag.find('./figure')
        img = tag.find('./img')  # find child elements' atrib
        img_src = img.get('src')
        figcaption = tag.find('./figcaption') #to img alt & figcaption text
        if figcaption is not None:
            figcaption_txt = figcaption.text
        else:
            figcaption_txt = ""
        tag.clear() # clear child elements
        new_fig = ''' <figure>
  <div class="fig">	      
  <img class="fig" src="{src}"
  alt="{caption}" />
  </div>
  <figcaption>{caption}</figcaption>
</figure>
'''.format(src=(img_src.encode('utf-8')), caption=(figcaption_txt.encode('utf-8'))) # new children
        new_fig = new_fig.replace('&', '&amp;')
        new_fig_tag = ET.fromstring(new_fig)
        tag.extend(new_fig_tag) # insert into figure



def figure(tree, element): # insert class fig inside to figure, img, figcaption, so they stay together
# use css avoi-page-break

    print '     adding <div class="fig"> to <figure>'
    for tag in tree.findall(element):
        figure = tag.find('./figure')
        img = tag.find('./img')  # find child elements' atrib
        img_src = img.get('src')
        figcaption = tag.find('./figcaption') #to img alt & figcaption text
        if figcaption is not None:
            figcaption_txt = figcaption.text
        else:
            figcaption_txt = ""
        tag.clear() # clear child elements
        new_fig = ''' <figure>
  <div class="fig">	      
  <img class="fig" src="{src}"
  alt="{caption}" />
  </div>
  <figcaption>{caption}</figcaption>
</figure>
'''.format(src=(img_src.encode('utf-8')), caption=(figcaption_txt.encode('utf-8'))) # new children
        new_fig = new_fig.replace('&', '&amp;')
        new_fig_tag = ET.fromstring(new_fig)



temp_ls=os.listdir("temp/")


for f in temp_ls: # 2.1: loop content files
    if f[:2]=='ch' and f[-6:]==".xhtml": # all ch*.xhtml
        filename = "temp/"+f
        print 'Processing:', filename
        # 2.2 Parse each file
        xhtml = open("temp/"+f, "r") # open and parse
        xhtml_parsed = html5lib.parse(xhtml, namespaceHTMLElements=False)

#        figure(xhtml_parsed, './/figure') 
        fn_rm_sup(xhtml_parsed, './/a[@class="footnoteRef"]')

        html = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n' + ET.tostring(xhtml_parsed, method="xml", encoding="utf-8")
        edited = open(filename, 'w') #write
        edited.write(html)


# Step 3: zip epub
epub = zipfile.ZipFile(pos_filename, "w")
#epub.writestr("mimetype", "application/epub+zip")
temp_dir = "temp"

def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            matches.append(os.path.join(root, filename))
    return matches

dirlist=fileList(temp_dir)

for name in dirlist:
    path = name[5:] # removes temp/
    epub.write(name, path, zipfile.ZIP_DEFLATED)
epub.close()


# Step 4: clean up: rm temp zipname
shutil.rmtree(temp_dir)

print
print "** toolkit_post.epub was generated without errors **"

