----
title: make VolkskrantBuilding.epub
---
<!--
 To do:
 * take photos create images
-->


The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City by Boukje Cnossen and Sebastian Olma

# make VolkskrantBuilding.epub Part I
## Introduction
In this blog post I will describe the process that led to the creation of the publication [The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City]() (TVB) by Boukje Cnossen and Sebastian Olma, as a digital book in EPUB3 format. I will be paying special attention on the use of Markdown as source files, Pandoc as markup converter software, Git as revision system, and most importantly Makefiles. I will attempt to demonstrate how all these individual resources can be combined to form one, or several, simple and yet powerful recipes which can greatly simplify and speedup the development of an EPUB, from manuscript to its final publishable form.

## Premises
From the onset we knew that TVB had to go from manustript to its two output format &ndash; EPUB and paper book &ndash; in little more than one week.
We were starting from good position. The manuscript, a .docx file, was in its final form and had been carefully edited, which meant that the all the text formatting was accomplished through styles, as described by Miriam Rash in the [Style Guide for Hybrid Publishing blog post](http://networkcultures.org/digitalpublishing/2014/10/21/style-guide-for-hybrid-publishing/). This consistency of the manuscript allows for a straightforward conversion of the manuscript into other formats, such as Markdown, necessary for the creation of the EPUB, within the [workflow](http://networkcultures.org/digitalpublishing/2014/10/07/hybrid-workflow-how-to-introduction-editing-steps/) INC is trying to implement in the production of its publications.

Despite this advantage, the short time span available for the production of TVB was still a challenge. The design studio &ndash; [UNDOG](http://www.undog.nl/) &ndash responsible for the book's design and paper edition, was working on the identity of the book, at the same time that I was developing the EPUB. This meant I had to follow the studio's lead, wait for its work to be completed, and only then apply the same identity to the EPUB edition of the TVB. The choice for such dynamic, for the production of books in multiple formats is highly questionable, for many reasons, among them its inefficiency and imposition of top-down dynamic, instead of more collaborative and egalitarian approach between all of those involved in the creation of a book, but that is in itself subject for another blog post.

## the workflow
For all these reasons the production of the EPUB called for a lean, organized and fast workflow. It had to be created in a much shorter time span and direct than I had experienced so far, with the production of the  [Network Notebooks EPUBS](http://networkcultures.org/publications/#netnotebook). I decided to try out the workflow that is being developed inside the Digital Publishing Toolkit Project and is currently being applied in the creation of the [Hybrid Publishing Toolkit for the Arts](https://github.com/DigitalPublishingToolkit/Hybrid-Publishing-Toolkit-for-the-Arts) publication.

My usual method for creating EPUBs involves the following tools:
* [Markdown](http://daringfireball.net/projects/markdown/syntax) source-files: a plain-text markup language, used to do most of the work on the book's text; It can perhaps be best described as a preparatory document to the generation of the EPUB, as all the essential content and structure of the EPUB is already present, under a much simpler form, in the Markdonwn.
* [Pandoc](http://johnmacfarlane.net/pandoc/): the conversion software, that translates between different markup languages. In this case I converted firs the manuscript from .docx to Mardown, and then the source Markdown file to an EPUB3 ebook;
* [Git](http://git-scm.com/): the revision system that tracks the history of changes, the sources files undergo during the production of the EPUB.

Yet, in addition to them I chose to also use a Makefile, much in a similar way as described by Michael Murtaugh in [Make Book blog post](http://networkcultures.org/digitalpublishing/2014/10/01/make-book/). The Makefile became center of operations that compiled all the source files &ndash; not only the text, but images, metadata, font files, css stylesheets &ndash and addressed them to Pandoc, in order to produce the target EPUB file. 

Here is how does the Makefile used in the production of TVB EPUB looks like:

`
VolkskrantBuilding.epub: 
	cd docs && pandoc \
	--from markdown \
	--to epub3 \
	--self-contained \
	--epub-chapter-level=1 \
	--toc-depth=2 \
	--epub-cover-image=media/cover.png \
	--epub-metadata=metadata.xml \
	--epub-stylesheet=styles.epub.css \
	--epub-embed-font=VAGRoundedStd-Black.otf \
	--epub-embed-font=VAGRoundedStd-Bold.otf \
	--epub-embed-font=VAGRoundedStd-Light.otf \
	--epub-embed-font=VAGRoundedStd-Thin.otf \
	--default-image-extension png \
	-o VolkskrantBuilding.epub \
	VK.md
`

With this recipe and all its ingredients in place I, I only had to run: `make VolkskrantBuilding.epub` and a a full-fledged EPUB was produced. 

### positive aspects   
This approach, centered on a Makefile, became quite useful and sped-up the development of the EPUB.
Its major strength relies in its ability to reduce my work focus to the source files, and the makefile. 
The source files &ndash; the Markdown text files, images, metadata, CSS styles &ndash; are the ingredients I need in order to cook this EPUB dish and the recipe is the makefile.  
If I want a specific result, a spefic dish, to be produced I will need to change either my ingredients or my recipe  &ndash; the 2 focal points of this approach. 
The cooking itself, or in other words the production of the EPUB, is realized in a matter of seconds though the execution of the makefile and its instructions via `make VolkskrantBuilding.epub`. 
I then view the result and evaluate the result.
If I happen to dislike the dish I just created, I can very simply adjust the ingredients or the recipe, in an attempt that the following EPUB dish, will be closer to my expectation.
I iterate through this circle of fine-tuning ingredients and recipe, cooking, and tasting, until I arrive to a EPUB dish which I consider satisfactory. 

The described approach contrasts with my usual method for producing EPUB.
In latter case I create a rough EPUB with pandoc, unzip it and then start to work with its constituent files &ndash; editing the metadata in content.opf, the stylesheet, or the content .xhtml files. 
Once all editing is done I zip all the files back into an EPUB and look at the result. 
I evaluate the result, see what needs to be change, and  back to the unzipped EPUB constituent files, repeating the whole process a few more times until I am happy with the outcome.
If I carry on with a culinary analogy I'd say that this approach would be like cooking with an already cooked dish. 
The EPUB dish is in front of me, and what I do is to separate its different parts, such as the salad, the sauce, the main ingredient, change them individually, and then put them back together in a slightly different dish. Different iteration of this process are also necessary to arrive to a pleasing result. 

Although it works, this approach is somehow unfocused. I need to work with many HTML files, and although HTML is a powerful and yet simple markup language, it is unpleasant to either read or edit. It instinctively feels like a recipe for disaster when one edits large sections of text wrapped by countless HTML tags. 

With the makefile approach I am spared from working with HTML. Instead I deal mostly with Markdown source files, which contrarily to HTML are easy to read and edit.
Even in cases where I need to include more expressive sections to the text, which follow outside the capabilities of Markdown, such as the the red quotations blocks that permeate TVB EPUB, I kept working on the Markdown and introduced snippets of HTML to accomplish these more elaborate job. ![A red quotation from The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City]()

Thanks to both the easiness in which content can be changed, and promptly compiled in to an EPUB, the feedback loop between change and its effect on the EPUB became much shorter.
In conjunction with Git, which tracks all the changes in both source files and the compiled EPUB, I was spared from having to creating many versions of the same files and could instead over-write all the files, knowing that at any time, I could revert my changes to a previous version ( or *revision* in Git parlance).


### exceptions
The downside of this approach is that it leaves one at the mercy of the conversion software used.
Although Pandoc is an incredibly powerful piece of software, it is not perfect, as I am afraid no piece of software is. 
Pandoc conversions, are sometimes, specially in very small details, not exactly what one might wish.
An example of this is the way Pandoc handles footnote references in conversions to the EPUB3.
In outcomes of such conversion, superscript footnotes' reference numbers are wrapped by HTML superscript elements `<sup>`, as in
`squatters movement.<a href="#fn2" class="footnoteRef" id="fnref2" epub:type="noteref"><sup>2</sup></a>`. 
This behavious is understandble, as it is a simple way to present the reader symbols that can easily be understood as footnotes.
Yet it goes against the [accessibility guidelines](http://www.idpf.org/accessibility/guidelines/content/xhtml/notes.php) from the International Digital Publishing Forum, which state "Do not use the sup element to superscript note references, as it is redundant presentational tagging. The CSS vertical-align property can be set to superscript the a elements." Furthermore, they compromise the resposiveness of footnote references in the iPad's iBooks reader. 
It is understandable that such an issue arises. EPUB3 specs are still in development and Pandoc is an open-source project of small dimensions, which probably has more pressing issues than to make the footnotes in EPUB3 conversions, respond well in the iPad reader. 

Yet, one can do something about this issue. The most obvious fix is to remove all the sup tags from the EPUB once is created. 
The other solutions are directly related to the fact that Pandoc is Free/Open-Source Software, licensed under the [GNU General Public License version 2](http://www.gnu.org/licenses/gpl-2.0.html). The license clearly states that "You may modify your copy or copies of the Program or any portion of it", which means that if one has the permission to alter the way footnote references are encoded in conversions to EPUB3, and other default behavior of Pandoc.
It is also possible to visit the [central repository](https://github.com/jgm/pandoc) where the development of Pandoc takes place, and address this problem by [opening an issue](https://github.com/jgm/pandoc/issues?q=is%3Aissue+is%3Aopen), where it will be read and possibly considered by Pandoc's developers.     


### evaluation
In a nutshell Makefiles are useful and yet simple ways to optimize the development of an EPUB into recipes that can simplify the development of an EPUB and
make the most out of the combination of small, simple and yet powerful pieces of software. 
However this approach isn't perfect. It isn't a one-size-fits-all recipe that can be applied to the production each and every kind of EPUBs, as it produces nearly invisible artifacts that in some contexts can become disruptive. 
Consequently the intervention of other approaches are essential to the creation of digital books. 
I see this heterogeneity of approaches as essential, to promote experimentation and innovation in the creation of digital books. 












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

