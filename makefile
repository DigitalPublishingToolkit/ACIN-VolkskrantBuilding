
VK.epub: 
	cd docs && pandoc \
	--from markdown \
	--to epub3 \
	--self-contained \
	--epub-chapter-level=1 \
	--toc-depth=2 \
	--epub-cover-image=media/cover.png \
	--epub-metadata=metadata.xml \
	--epub-embed-font=fonts/VAGRoundedStd-Black.otf \
	--epub-embed-font=fonts/VAGRoundedStd-Bold.otf \
	--epub-embed-font=fonts/VAGRoundedStd-Light.otf \
	--epub-embed-font=fonts/VAGRoundedStd-Thin.otf \
	--epub-stylesheet=styles.epub.css \
	--default-image-extension png \
	-o VK.epub \
	VK.md  &&\
	cp VK.epub VK_post.epub &&\
	python ../scripts/epub_post.py VK_post.epub


