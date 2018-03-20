FROM jvstein/pybossa:latest

COPY gsi-template/_footer.html pybossa/themes/default/templates/_footer.html
COPY gsi-template/_navbar.html pybossa/themes/default/templates/_navbar.html
COPY gsi-template/base.html pybossa/themes/default/templates/base.html
COPY gsi-template/nuevo.html pybossa/themes/default/templates/nuevo.html

COPY gsi-template/_helpers.html pybossa/themes/default/templates/account/_helpers.html

COPY gsi-template/pybossa-gsi.min.css pybossa/themes/default/static/css/gen/pybossa-gsi.min.css
COPY gsi-template/projects.html pybossa/themes/default/templates/account/projects.html



COPY gsi-template/logo.png pybossa/themes/default/static/img/

COPY settings_local.py settings_local.py
