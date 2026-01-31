check-spdx:
	./add_spdx.py

apply-spdx:
	./add_spdx.py --apply

install-git-hooks:     ## Install git-hooks
	ln -s ../../add_spdx.py .git/hooks/pre-commit

uninstall-git-hooks:     ## Uninstall git-hooks
	rm .git/hooks/pre-commit
