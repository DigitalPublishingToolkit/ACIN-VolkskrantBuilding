
VK.epub: 
	pandoc \
	--from markdown \
	--to epub3 \
	--self-contained \
	--epub-chapter-level=1 \
	--toc-depth=2 \
	 --epub-metadata=docs/metadata.xml \
	-o docs/VK.epub \
	docs/VK.md
