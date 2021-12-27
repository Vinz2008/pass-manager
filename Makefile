DESTDIR=/usr/bin
install:
	touch password-manager
	python3 shebang.py
	cp password-manager $(DESTDIR)/
clean:
	rm ~/.password/passwordmanager.db
