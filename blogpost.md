
# Cooking the VolkskrantBuilding.epub
![The Volkskrant Building EPUB trailer]()

Last week [The Institute of Network Cultures](http://networkcultures.org/) and [Amsterdam Creative Industries Network](amsterdamcreativeindustries.com/)  launched the publication [The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City](http://networkcultures.org/blog/publication/the-volkskrant-building-manufacturing-difference-in-amsterdams-creative-city-boukje-cnossen-and-sebastian-olma/) (TVB) by Boukje Cnossen and Sebastian Olma. 
I use this post to share the process that led to the production of its EPUB edition.


From the onset it was clear that TVB had to go from manuscript to its two output format &ndash; EPUB and paper book &ndash; in little more than one week.
We were starting from good position: the manuscript, a .docx file, was in its final form and had been carefully edited, with all of its text formatting accomplished through styles, as described by Miriam Rash in the [Style Guide for Hybrid Publishing blog-post](http://networkcultures.org/digitalpublishing/2014/10/21/style-guide-for-hybrid-publishing/). This consistency of the manuscript allows for the necessary format conversions to be performed with ease and little obstructions. Despite this advantage, the short time span available for the production of TVB was still a challenge. While [UNDOG](http://www.undog.nl/) design studio worked on the identity of the book, I developed the EPUB. This meant I had to follow the studio's lead, wait for its work to be completed, and only then could I apply the same identity to the EPUB edition. The adoption of such dynamic, for the production of books in multiple formats, is highly questionable, given its inefficiency and imposition of top-down dynamic instead of s more collaborative approach between all of those involved in the production of a book, but that is in itself subject for another blog post.

The production of the EPUB called for a lean, organized and fast workflow. The ebook had to be created in a much shorter time period than I had had for the production of the [Network Notebooks EPUBS](http://networkcultures.org/publications/#netnotebook). 

In my usual method for creating EPUBs I use: 

* [Markdown](http://daringfireball.net/projects/markdown/syntax) source-files: a plain-text markup language, used to do most of the work on the book's text; It can perhaps be best described as a preparatory document to the generation of the EPUB, where all the content, text-formatting, and structure of the EPUB is already present, under a much simpler form.

* [Pandoc](http://johnmacfarlane.net/pandoc/): the conversion software, that translates between different markup languages. In this case I used Pandoc to first converted the manuscript from .docx to Markdown, made the necessary changes to the Markdown source file and then converted it to an EPUB3 ebook;

* [Git](http://git-scm.com/): the versioning system which tracks the history of changes the sources files undergo during the production of the EPUB.

In addition to these tools I chose to use a Makefile, in a similar way as described by Michael Murtaugh in the [Make Book blog post](http://networkcultures.org/digitalpublishing/2014/10/01/make-book/). The Makefile became center of operations that compiled all the source files, not only the text, but images, metadata, font files, CSS stylesheet and addressed them to Pandoc, to be converted into a target EPUB file as intended. 

<pre>
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
</pre>

The Makefile used in the production of TVB EPUB.



This approach centered on a Makefile allowed me to narrow my focus to the source files and the Makefile. As a result it sped-up and simplified the process of developing the EPUB.
The source files &ndash; the Markdown text files, images, metadata, CSS styles &ndash; are the ingredients necessary to cook this EPUB dish and the recipe is the Makefile.  
If I want a specific result to be produced I need to change either my ingredients or my recipe.
The cooking itself, or in other words the production of the EPUB, is realized in a matter of seconds though the execution of the makefile and its instructions via `make VolkskrantBuilding.epub`. 
Once the `make` command is executed I'll evaluate the result.
If I happen to dislike the dish I just created, I can very simply adjust the ingredients or the recipe.
I iterate through this circle, fine-tuning ingredients and recipe, cooking, and tasting, until I arrive to a satisfactory EPUB. 

The described approach contrasts with my default method for producing EPUBs.
Usually I create a rough EPUB with Pandoc, unzip it and start working its constituent files &ndash; editing the metadata inside content.opf, the stylesheet, or the content .xhtml files. 
When all editing is done I zip the files back into an EPUB and look at the result. I repeat the whole process few more times until I am happy with the outcome.
If I carry on with the culinary analogies I'd say that this approach would be like cooking an already cooked dish. 
The EPUB dish is in front of me, and what I do is separate its different parts, change them individually, and then put them back together in a slightly different dish. Although it works, this approach is somehow unfocused, which brings to work with several HTML files. Although HTML is a powerful, yet simple markup language, it is unpleasant to either read or edit. It instinctively feels like a recipe for disaster when one has to edit large sections of text wrapped by countless HTML tags. 


With the Makefile approach I am spared from working with HTML. Instead I deal with Markdown source files, which contrarily to HTML are easy to read and edit and can be quickly compiled into an EPUB. The feedback loop between a change and its effect on the EPUB became much shorter and more direct.
And even in cases of more expressive sections, which fall outside the scope of Markdown, such as the red quotations blocks that permeate TVB, Markdown allows the inclusion of HTML, which can easily do the job. 

![A red quotation from The Volkskrant Building: Manufacturing Difference in Amsterdam’s Creative City]()



The big downside of this approach is that it leaves one at the mercy of the conversion software used.
Although Pandoc is an incredibly powerful piece of software, it is not perfect, as I am afraid no piece of software is. 
Pandoc conversions, are sometimes, specially in very small details, not exactly what one wishes.
An example of this is the way Pandoc handles footnote references in conversions towards EPUB3.
The conversion presents superscript footnote reference numbers wrapped by HTML superscript elements `<sup>`, as in: `squatters movement.<a href="#fn2" class="footnoteRef" id="fnref2" epub:type="noteref"><sup>2</sup></a>`. 
This behavior is understandable, as `<sup>` tags are a simple means to format text as superscript.
Yet it goes against the [accessibility guidelines](http://www.idpf.org/accessibility/guidelines/content/xhtml/notes.php) from the International Digital Publishing Forum, which state "Do not use the sup element to superscript note references, as it is redundant presentational tagging. The CSS vertical-align property can be set to superscript the a elements." Furthermore, they compromise the responsiveness of footnote references in the iPad's iBooks reader. 
All in all, it is understandable that such issue arises. EPUB3 specs are still in development and Pandoc is an open-source project of small dimensions, which probably has more pressing issues than to make footnotes respond well on the iPad. 
Yet, one can do something about it. The most obvious fix is to remove all the sup tags from the EPUB once is created (via a script). 
The other solutions are directly related to the fact that Pandoc is Free/Open-Source software, licensed under the [GNU General Public License version 2](http://www.gnu.org/licenses/gpl-2.0.html). The license clearly states that "You may modify your copy or copies of the Program or any portion of it", which means anyone has the permission to modify Pandoc source-code, and alter the way footnote references are encoded in conversions towards EPUB3. Other possibility is to visit the [central repository](https://github.com/jgm/pandoc) where the development of Pandoc takes place, and address this problem by [opening an issue](https://github.com/jgm/pandoc/issues?q=is%3Aissue+is%3Aopen), which will be read considered by Pandoc's developers.     


In a nutshell Makefiles are useful and simple ways to optimize the development of an EPUB into recipes that can simplify the development of an EPUB and
make the most out of the combination of small, simple and yet powerful pieces of software. 
However this approach isn't perfect. It isn't a one-size-fits-all recipe that can be applied to the production each and every kind of EPUBs, as it produces default behaviors and nearly invisible artifacts that in some contexts can become disruptive. 
Consequently the employment of other approaches and experimentation remains essential to the innovation and diversification of digital books. 
