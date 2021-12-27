DESTDIR=/usr/bin
install:
	touch password-manager
	python3 shebang.py
	sudo cp password-manager $(DESTDIR)/
	python3 install.py
clean:
	rm ~/.password/passwordmanager.db

uninstall:
	rm ~/.password/passwordmanager.db
	sudo rm $(DESTDIR)/password-manager
