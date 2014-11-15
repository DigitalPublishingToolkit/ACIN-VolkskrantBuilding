----
title: make VolkskrantBuilding.epub
---

The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City by Boukje Cnossen and Sebastian Olma

# make VolkskrantBuilding.epub Part I
## Introducution
In this blog post I will describe the process of production of the EPUB for The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City by Boukje Cnossen and Sebastian Olma. 

(I will pay special attention on the use of a markdown source files, makefiles and version control, as these elements allow for a very fast and lean workflow for the production of an EPUB).

## Premises
From the onset we knew that the ebook had to be development in as little as for days.
Although the text was 
* couple of days
* text was in its final form
* well formatted manuscript (reference Blog post)
* the short time span was challange
   * designer of the book's paper edition was working at the same time as me
   * He has treating the images, and creating the visual identity for the book
   * I had to follow his lead, wait for his work to be done, 
   * then: try to apply it to the EPUB
   
Editor did great work at correctly formatting the manuscript


## the workflow
### description
* I decided to try workflow: DPT
   * in addition to: markdown, pandoc, git
   * use of make files (described in MM blog post)

### positive aspects   
* Simple 
* Allows
   * write elaborate conversions (css file, fonts, cover, metadata is speficied)
   * a simple comand make VK.epub the epub is produce
   * the same file and logic can be used to create convesions to other formats such as html, odf

* streams: inclusion of html 
### exceptions
#### subs
Now the downside of this approach is that it leaves one at the mercy of the conversion software.
* pandoc good
* but might do things, sometimes in ways one doesn't want
    * otf fonts
	* converts the footnotes wrapped in HTML `<sup>` 

These expceptions can force you out of the workflow
* I had to unzip the EPUB and make change manual changes  
* Or for the `<sup>` write a script to remove sup tags from footnotes

### evaluation
* powerfull, simple, fast way to create EPUBs

* Not make, but the combination of these small, simple and yet powerfull pieces of software that allow the process of EPUB creation quite a straight-forwad business







----


# make VolkskrantBuilding.epub: Part II 
`designin books  ≈ developing code`

This second post will take the workflow employed in the production of "The Volkskrant Building" Epub, as describe in **POST** and use it as an example of how the creation process of a bookcan gain from engaging with practices that have their origin in software development.



* with EPUB the approach to entire creation of a book is closer to practices of software development
* instead of working with a many file formats that change at every step of the book publishingladder,  the work **can be** concentrated on as little as one source file

* (source files dont need to be markdown. Other markup language: Mediawiki, syntax that easy to read and write and provides elements essential to writing, such as footnotes, referencing, hierarchic headings, basic styling, inclusion of image, allow inclusing HTML &ndash to garnish the text with more elaborate elements)

# How ?#

`conventional: .doc(author) --> .doc(editor) w/ changes --> indesign(designer) --> pdf(for print)`

`new:
                 editor
				   |
 md(author) -->  .md  <-- desiger/develop
                   | 
                   /\
               EPUB  ICML 
			           \
                       indesign  (scribus)


* ICML --> inDesign: Silvio Post


## Advatage
* contrary to what MR describes, corrections dont need to be implemented in each one of the book outputs (time-consuming,  prove to error)
    * changes are done on the source file(s)
    * the source file(s) is track by a revision system

## Chalanges
* Does this mean that authors, editors, and designers will have become programmers?
  * No, at least not partly 
  * they wont be need to write pices of software, they will be instead borowing methodologies from software development practices.

* will it happen? I dont know the answer, however change and leans working methods is something from which the book publishing could hardly benefit 

