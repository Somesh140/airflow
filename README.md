# airflow

Steps
* Install docker desktop make sure that virtualisation in your system is enabled also WSL should be enabled
* download this repo
* create a folder inside airflow-main as dockerfiles
* keep the Dockerfile inside the dockerfiles folder
* In the terminal run the command (make sure that you are inside the airflow directory)
```
 docker-compose up --build
 ```
 * check in the docker desktop the container is running also a dags directory will be created in the current directory
 
 * In the browser check ```localhost:8080```
 * Split the terminal 
 * In the new terminal run command ``` pip install apache-airflow```
 * Inside dags directory create a file first_dag.py
 * To stop the docker run the command ```docker-compose down```
 
