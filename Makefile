install_prerequesites:
	pip install -r requirements.txt

compile:
	mkdocs gh-deploy
