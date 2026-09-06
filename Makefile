check-spdx:
	./add_spdx.py

apply-spdx:
	./add_spdx.py --apply

install-git-hooks:     ## Install git-hooks
        git config --local core.hooksPath $(HOOKS_DIR)
	ln -s ../../add_spdx.py .git/hooks/pre-commit

uninstall-git-hooks:     ## Uninstall git-hooks
	rm .git/hooks/pre-commit
