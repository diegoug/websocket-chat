# Pycharm professional edition

## Configure Pycharm to work with Docker

Open [microservice-name] folder in to your Pycharm professional edition

![Menu open folder](img/pycharm_open_folder.png)

![Open folder](img/pycharm_select_folder.png)

### Configure Pycharm professional edition

#### Configure Python interpreter

Open File > Settings, then on the settigs of pycharm select Project:[microservice-name] then select python interpreter, now add a new pthon interpreter, select the option On Docker Compose.

![Settings](img/pycharm_open_settings.png)

![Python interpreter](img/pycharm_docker_compose_interpreter.png)

On the target Docker Compose select the folder on configuration files, add a new docker compose configuration file, find [docker-compose.yml](../docker/development/docker-compose.yml) file on hermes project.

![docker compose configuration file](img/pycharm_docker_compose_configuration_file.png)

Add a enviroment variable LOCAL_VAR=/var to the target, then go Next.

![docker compose configuration](img/pycharm_docker_compose_configuration.png)

Now in the last step you can preview the created interpreter and then select Create

![docker compose directory and languale](img/pycharm_docker_compose_directory_and_languale.png)

Now with this you can preview the correctly created python interpreter using docker compose, and now you can see the python libraries installed in this docker compose python interpreter

![docker compose select interpreter](img/pycharm_docker_compose_select_interpreter.png)

#### Configure Pycharm professional editio enviroment

In the upper right corner is the menu to configure the development environment which we are going to create using the previously configured interpreter.

select edit configurations, the Run/Debug Configurations window will open, in the plus symbol, you can add a new flask server, give it a name, preferably [microservice-name], in Target type select Scrit path, in additional options add the following configuration : --host=0.0.0.0 --port=3500, in python interpreter selects the interpreter that we created in the previous step, and to finish it is necessary to create some before launch actions

![create debug configuration](img/pycharm_create_debug_configuration.png)

![flask debug configuration](img/pycharm_flask_debug_configuration.png)

It is important to create a before launch action to create an environment variable file based on the environment variable file for development.

![flask debug configuration external tool](img/pycharm_flask_debug_configuration_external_tool.png)

Once the before launch task is created, we return to the Run/Debug Configurations view and select ok

### Run debug mode

Now in the upper right corner will appear the created [microservice-name] environment and the debug and run options, if you select the bug you will be able to debug the application with break points, and if you select the play button you will be able to run the application, the difference is time boot and resources since debugging mode uses more of these to function.

### Running

![Running](img/pycharm_flask_debug_start.png)

Back to [README](../../README.md)