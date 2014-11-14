----
title: make VolkskrantBuilding.epub
---

The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City by Boukje Cnossen and Sebastian Olma

# make VolkskrantBuilding.epub: Part I
## Introducution
In this blog post I will describe the process of production of the EPUB for The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City by Boukje Cnossen and Sebastian Olma. 

I will pay special attention on the use of a markdown source files, makefiles and version control, as these elements allow for a very fast and lean workflow for the production of an EPUB.

## the workflow
* how the EPUB was developed using: markdown, makefile, pandoc, git can be use 
* use of makefile: described in MM blog post
### description
### positive aspects
* streams: inclusion of html 
### exceptions
### evaluation


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

