DESTDIR=/usr/bin
install:
	touch password-manager
	python3 shebang.py
	mkdir $(DESTDIR)/password-manager/
	cp password-manager $(DESTDIR)/password-manager/
clean:
	rm ~/.password/passwordmanager.db
