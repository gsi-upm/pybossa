FROM jvstein/pybossa:latest

COPY gsi-template/_footer.html pybossa/themes/default/templates/_footer.html

COPY gsi-template/_navbar.html pybossa/themes/default/templates/_navbar.html

COPY settings_local.py settings_local.py