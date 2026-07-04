srpm:
	tar \
		-czf $(outdir)/doomtools-rpm-sources.tar.gz \
		doomtools.desktop \
		template.sh \
		completion
	rpmbuild -bs doomtools.spec --define "_srcrpmdir $(outdir)"
