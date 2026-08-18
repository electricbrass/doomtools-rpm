SOURCES := $(shell rpm --eval '%_sourcedir')

srpm:
	tar \
		-czf $(SOURCES)/doomtools-rpm-sources.tar.gz \
		doomtools.desktop \
		net.mtrop.doom.tools.metainfo.xml \
		template.sh \
		completion
	rpmbuild -bs doomtools.spec --define "_srcrpmdir $(outdir)"
