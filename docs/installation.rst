Installation
------------

The requirements for installing Pybossa are having docker and docker-compose installed in your computer.

The first step of the installation process is cloning the next repository:

.. code-block:: bash

	git clone http://lab.cluster.gsi.dit.upm.es/datasets/pybossa.git
	git submodule update --init --remote --recursive
	cd pybossa


In this directory, you have to create a file called .env including the following variable names and their values (without quotation marks): SECRET, SECRET_KEY, ITSDANGEROUSKEY, TASK_CSV_EXPORT_INFO_KEY, TASK_RUN_CSV_EXPORT_INFO_KEY, RESULT_CSV_EXPORT_INFO, POSTGRES_USER, POSTGRES_PASSWORD (put the values that you prefer in this variables), POSTGRES_URL and TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET, which are the credentials that you have to create for enabling Pybossa authentication with Twitter and Google.

In the settings_local.py, there are all the pybossa configuration options that you can configure for personalizing your pybossa environment.


After creating the .env file, you can run the image executing:

.. code-block:: bash

	sudo docker-compose build
	sudo docker-compose up


After executing these commands you can see the pybossa server running in http://localhost:8080/

The template that appears is the GSI-UPM template. If you want to change the template, you can edit the HTML and CSS files from the pybossadocker folder from the directory cloned before.

If you want to change your Postgres user's password, after executing docker-compose up, run in a shell of the same directory:

.. code-block:: bash

	sudo docker-compose exec postgres /bin/sh
	psql -U postgres
	ALTER USER yourpostgresuser PASSWORD 'newpassword';

Where yourpostgresuser is the value of the variable POSTGRES_USER of your .env file and newpassword the value that you want to put to your new password.
After that, update the value of POSTGRES_PASSWORD of your .env file.