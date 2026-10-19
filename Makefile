.PHONY: test catalog check social

test:
	python3 -m unittest discover -s tests -v

catalog:
	python3 scripts/build_catalog.py

check:
	python3 scripts/build_catalog.py --check

# Requer Chromium (CHROME) e ImageMagick (convert). O headless corta a altura útil da
# janela, então renderiza maior e recorta para 1280x640.
CHROME ?= chromium
social:
	$(CHROME) --headless --no-sandbox --disable-gpu --hide-scrollbars \
		--window-size=1280,900 --screenshot=assets/social-preview.png \
		file://$(CURDIR)/assets/social-preview.html
	convert assets/social-preview.png -crop 1280x640+0+0 +repage assets/social-preview.png
