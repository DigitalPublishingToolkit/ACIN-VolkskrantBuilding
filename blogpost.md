----
title: make VolkskrantBuilding.epub
---
<!--
 To do:
 * tidy scripts/epub_post.py - only fn remove
 * take photos create images
-->


The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City by Boukje Cnossen and Sebastian Olma

# make VolkskrantBuilding.epub Part I
## Introducution
In this blog post I will describe the process that led to the creation of the publication [The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City]() (TVB) by Boukje Cnossen and Sebastian Olma, as a digital book in EPUB3 format. I will be paying special attention on the use of Markdown as source files, Pandoc as markup converter software, Git as revision system, and most importantly Makefiles. I will attempt to demonstrate how all these individual resources can be combined to form one, or several, simple and yet powerful recipes which can greatly simplify and speedup the development of an EPUB, from manuscript to its final publishable form.


## Premises
From the onset we knew that TVB had to go from manustript to its two output format &ndash; EPUB and paper book &ndash; in little more than one week.
We were starting from good position. The manuscript, a .docx file, was in its final form and had been carefully edited, which meant that the all the text formatting was accomplished through styles, as described by Miriam Rash in the [Style Guide for Hybrid Publishing blog post](http://networkcultures.org/digitalpublishing/2014/10/21/style-guide-for-hybrid-publishing/). This consistency of the manuscript allows for a straightforward conversion of the manuscript into other formats, such as Markdown, necessary for the creation of the EPUB, within the [workflow](http://networkcultures.org/digitalpublishing/2014/10/07/hybrid-workflow-how-to-introduction-editing-steps/) INC is trying to implement in the production of its publications.

Despite this advantage, the short time span available for the production of TVB was still a challenge. The design studio &ndash; [UNDOG](http://www.undog.nl/) &ndash responsible for the book's design and paper edition, was working on the identity of the book, at the same time that I was developing the EPUB. This meant I had to follow the studio's lead, wait for its work to be completed, and only then apply the same identity to the EPUB edition of the TVB. The choice for such dynamic, for the production of books in multiple formats is highly questionable, for many reasons, among them its inefficiency and imposition of top-down dynamic, instead of more collaborative and egalitarian approach between all of those involved in the creation of a book, but that is in itself subject for another blog post.

> * He has treating the images, and creating the visual identity for the book
>    * I had to follow his lead, wait for his work to be done, 
>    * then: try to apply it to the EPUB
> 
> Although the text was 
> * couple of days
> * text was in its final form
> * well formatted manuscript (reference Blog post)
> * the short time span was challange
>    * designer of the book's paper edition was working at the same time as me
>    * He has treating the images, and creating the visual identity for the book
>    * I had to follow his lead, wait for his work to be done, 
>    * then: try to apply it to the EPUB
>    
> Editor did great work at correctly formatting the manuscript

## the workflow
### description
For all these reasons the production of the EPUB called for a lean, organized and fast workflow. It had to be created in a much shorter time span and direct than I had experienced so far, with the production of the  [Network Notebooks EPUBS](http://networkcultures.org/publications/#netnotebook). I decided to try out the workflow that is being developed inside the Digital Publishing Toolkit Project and is currently being applied in the creation of the [Hybrid Publishing Toolkit for the Arts](https://github.com/DigitalPublishingToolkit/Hybrid-Publishing-Toolkit-for-the-Arts) publication.

As common to my working method, I employed the following tools:
* [Markdown](http://daringfireball.net/projects/markdown/syntax) source-files: a plain-text markup language, used to do most of the preparatory work on the book's text, necessary generating an error-free EPUB;
* [Pandoc](http://johnmacfarlane.net/pandoc/): the conversion software, that translates files between different markup languages, in this case from .docx to Mardown, and then from Markdown to EPUB3);
* [Git](http://git-scm.com/): the revision system that tracks the history of changes the sources files and scripts necessary to the production of the EPUB undergo.

Yet, in addition to them I chose to also use a Makefile, as described by Michael Murtaugh in [Make Book blog post](http://networkcultures.org/digitalpublishing/2014/10/01/make-book/). The Makefile became center of operations that compiled all the source files &ndash; not only the text, but images, metadata, font files, css stylesheets &ndash and addressed them to Pandoc, in order to produce the target EPUB file. 

Here is how does the Makefile used in the production of TVB EPUB looks like:

`
VK.epub: 
	cd docs && pandoc \
	--from markdown \
	--to epub3 \
	--self-contained \
	--epub-chapter-level=2 \
	--toc-depth=2 \
	--epub-cover-image=media/cover.png \
	--epub-metadata=metadata.xml \
	--epub-stylesheet=styles.epub.css \
	--epub-embed-font=fonts/VAGRoundedStd-Black.otf \
	--epub-embed-font=fonts/VAGRoundedStd-Bold.otf \
	--epub-embed-font=fonts/VAGRoundedStd-Light.otf \
	--epub-embed-font=fonts/VAGRoundedStd-Thin.otf \
	--default-image-extension png \
	-o VK.epub \
	VK.md
`

> X You can see that it ask pandoc not only to convert the markdown file VK.md into an EPUB3 format under the filename VK.epub, but that it indicates that supplies the EPUB withspecific cover image, metadata, s   

In order to convert that markdown file into a full-fledged EPUB I only had to run: `make VK.epub`

>    * in addition to: markdown, pandoc, git
>    * use of make files (described in MM blog post)


### positive aspects   
This approach became quite useful and sped-up the process of development of the EPUB. 
It allowed me to work only with the source files, run the make command, and review the resulting EPUB. 

This new approach was very different and much simpler than my usual working method. In my previous approach I'd created a rough EPUB with pandoc, unzip it and then start to work with its constituint files &ndash; entering the metadata, resources such the stylesheet or fonts to package document (.opf file), garnishing the content documents (.xhtml files), etc. The newx step would normally be to zip all the files back into an EPUB and look at the result. I'd take notes of what needed to be change, went back to to EPUB constituint files and repeate the whole process a few times until I was statiesfied with the outcome.

Although it worked, this approach was somehow unfocused. The amount of files I needed to work with was very large &ndash; in an EPUB content is split into multiple xhtml files, each corresponding to a chapter or section of the book &ndash; and the language I need to work with &ndash; HTML &ndash; although very powerfull and compreensible, because hard to read and edit when we are talking about chapter after chapter of text.

Using the makefile approach I started to work *only* with markdown source file, which contrarily to HTML are very easy to read and edit, and in this case was limited to one single file. And even in cases where I need to include more expressive elements into the text, such as the the red quotations blocks that permeate this publication, I kept working on the markdown source files, overcoming Markdown limitations by introducing snippets of HTML to accomplish these more elaborate job. ![A red quotation from The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City]()

The distance between making a change and viewing that change became much shorter, creating an almost emmediate feedback loop between source files and compiled EPUB.  

And as I was using git to track all the changes in both source files and the compiled and the EPUB I was spared from having to creating many versions of the same files. Instead I would over-write all the files. If I need to revert my changes to a previous version, or *revision* in programmers parlance, I just need to ask Git to do it. 


> *  Not much change: I kept using the same  tools

> * Simple 
> * Allows
>    * write elaborate conversions (css file, fonts, cover, metadata is speficied)
>    * a simple comand make VK.epub the epub is produce
>    * the same file and logic can be used to create convesions to other formats such as html, odf
>    * streams: inclusion of html 
### exceptions
#### subs
Now the downside of this approach is that it leaves one at the mercy of the conversion software used.
Although Pandoc is and incredibly powerfull piece of software is not perfect, as I am afraid no piece of software is. 
The way Pandoc does conversions is sometimes, specially in very small details, not the best.

An example of this is the way Pandoc handles footnote references in conversions to the EPUB3.
In order to achieve a superscript footnote, Pandoc wraps the reference number in HTML superscript tags (`<sup>`), as in
`squatters movement.<a href="#fn2" class="footnoteRef" id="fnref2" epub:type="noteref"><sup>2</sup></a>`. 
This behavious is understandble, as it is a simple way to archieve number marks that can be easily understood as footnotes.
Yet it goes against the [accessibility guidelines](http://www.idpf.org/accessibility/guidelines/content/xhtml/notes.php) from the International Digital Publishing Forum, which state "Do not use the sup element to superscript note references, as it is redundant presentational tagging. The CSS vertical-align property can be set to superscript the a elements." Furthermore, they compromise the resposiveness of footnote references in the iPad's iBooks reader.

However there is a solution for every problem, or more than one.
The most obvious fix is to remove all the sup tags from the EPUB once this was create, this was what I did by through a [pyhton script](https://github.com/DigitalPublishingToolkit/VolkskrantBuilding/blob/master/scripts/epub_post.py). 
The other solutions are directly related to the fact that Pandoc is Free/Open-Source Software, licensed under the [GNU General Public License version 2](http://www.gnu.org/licenses/gpl-2.0.html). The license clearly states that "You may modify your copy or copies of the Program or any portion of it". Which means that if you have the ability to do so you can change the way the program behaves, and can consequently alter the way footnote references are encoded in conversions to EPUB3.
Another, more accessible approach is to go the central repository where the development takes place, and address this problem by [opening an issue](https://github.com/jgm/pandoc/issues?q=is%3Aissue+is%3Aopen).     


> * pandoc good
> * but might do things, sometimes in ways one doesn't want
>     * otf fonts
> 	* converts the footnotes wrapped in HTML `<sup>` 

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

