
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
	VK.md  &&\
	python ../scripts/epub_post.py VK.epub


