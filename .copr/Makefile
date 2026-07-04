srpm:
	tar \
		-czf $(outdir)/doomtools-rpm-sources.tar.gz \
		doomtools.desktop \
		template.sh \
		completion
	rpmbuild -bs "domtools.spec --define "_srcrpmdir $(outdir)"
