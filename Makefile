DESTDIR=/usr/bin
install:
	touch password-manager
	python3 shebang.py
	cp password-manager $(DESTDIR)/
	python3 --user install.py
clean:
	rm ~/.password/passwordmanager.db

uninstall:
	rm ~/.password/passwordmanager.db
	rm $(DESTDIR)/password-manager
