install:
	cp password-manager.py password-manager
	shebang="#!/usr/bin/python"
	finalcontent=echo "$(shebang)" | cat - password-manager
	echo $(finalcontent) > test
