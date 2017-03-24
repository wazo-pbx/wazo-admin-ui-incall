install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/incall.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-incall
	rm /etc/wazo-admin-ui/conf.d/incall.yml
	systemctl restart wazo-admin-ui
