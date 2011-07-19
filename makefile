# Copyright (c) 2011 Martin Ueding <dev@martin-ueding.de>

listui.py: list.ui
	pyuic4 $^ -o $@
