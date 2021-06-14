# DevOps Core Practical Project
## Football Project Generator
# 
#
* [Introduction](#Introduction) 
  * [Objetives & Project Proposal](#)
  * [Requirements](#)
* [Sofware Architecture](#architecture)
  * [Project Management](#trello)
  * [Risk Assessment](#risk)
  * [Database Structure](#entity-relationship-diagram)
  * [Continuous Integration Pipeline](#CI)
* [Software Infrastructure](#softwareinfrastructure)
  * [Jenkins](#jenkins)
  * [Services](#SERVICES)
  * [Swarm](#Swarmconfig)
  * [Front-End](#FrontEnd)
* [Testing](#Testing)
  * [Unit Testing](#Unitteting)
  * [Test Coverage](#testcoverage)
* [Future Improvements & Constraints](#FutureImprovementsandproblems)
* [Author](#Author)

## Introduction 
#

### Objetives & Project Proposal

This was an indidual project which involved me creating a service-orientated architecture application which had to be made up of four services. Service one is the core service, meaning it is the front-end that the user will see which should render the Jinja2 templates that interacts with my application, as well as communicating with other services.

The idea I went with was to create a player score generator that predicts if a player would score against a given team that was defined in the 'server_2' routes file. The user will first connect server 1 which will display the webpage, however before displaying the page, a GET request is made to service 2 & 3. Service will 2 will then return a random player, and service 3 a random team. Then a POST request is made to service 4 sending the random 'player' and'team' information obtained from the previous GET requests. Service 4 consists of nested IF staements that assigns a player to a team and returns an outcome, whether the player will score or not.

### Requirements

In order to achieve the brief and achieve the SFIA requirements, the following requirements must be achieved:

* Kanban board
* Relational database 
* Clear documentation 
* An application fully integrated using the feature branch model into a Version Control System (VCS). The VCS will be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine. 
* When any change is made to the code it is pushed to the VCS, webhooks must be set up for the CI server to recreate and redeploy the application
* Containerisation: Docker
* Ansible playbook must be made that will provide the environment for the application to run.
* A reverse proxy must be set up to make the applciation accessible to the user(NGINX).

## Software Architecture
#
### Project Management
For the project management i used a Kanban board on Trello. I found that Trello is very easy to use and is free.
I found it very easy to organise the tasks i need to get done. Below is an image of my Trello board aswell as a link to my Trello board
### Risk Assessment
A picture of a detailed risk assesment can be found below.


### Database Structure
I have included a picture of a ERD diagram showing the structure of the database.


### Continuous Integration Pipeline

## Software Infrastructure
#
### Jenkins 
Jenkins is a free and open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration and deployment. 

For this project, the stages of the Jenkins pipeline is as follows: 
* Testing - Which produces coverage reports on the console
* Build and push images - Docker-compose is used to build the images and push them to Docker-Hub
* Ansible configuration - Allows us to configure several servers at once, including:
* * Installing necessary dependencies,Initializing the swarm and connecting to worker nodes and Configuring the NGINX server for load-balancing
* Deploy stack - Configures the web-applcation on the manager and worker nodes

Further details on these stages used in the Jenkins pipeline can be found in the jenkinsfile. 

### Services

The project must include a minimum of 4 services as part of the MVP. The picture below shows how my services interact with each other, as you can see

### Swarm
The swarm manager, both workers and NGINX all run on seperate VM's on Google Cloud Platform. The way in which the swarm works:
- It starts with the manager, it pulls down the services and runs copies of them across to the workers
- This exists so that indivudual containers arent overloaded by heavy traffic and so that if either server or any container stops working the app will continue to run.
- Nginx then acts as a reverse proxy
- It also directs which tasks will be used for each user balancing the load and making sure the containers are distributed appropriately.

The image below shows a basic set up of the swarm. Once Ansible installs docker on both swarm-manager and swarm-worker nodes. It then intialises the swarm on the manager node and joins the worker nodes.

### Front-end

## Testing 
#
### Unit Testing
For my project I implemented unit testing in the application. I tested all services. Unit testing allows us to test whether each function reuturns an expected response. The pictures below shows pytest running on each server.
### Testing Coverage
My testing coverage did not meet the pass requirements as i only achieved a 72%. I was pretty overwhelmed with my workload and had lots of issues with GCP, so I had to move on and priorotize my time with the automation and jenkins.
## Future Improvements & Constraints
#

Despite my test coverage I think my application was a success. In future I believe I can definietly improve on my testing and add more testing to make it even more robust.

One big problem I ran into was being limited to 4 instances in one location.This caused me major issues as I had to constantly switch between instances by stopping and starting them. This was very frustrating and held me back.



## Author
#
- Arman Khan
## Acknowledgements
#
- Harry Volker

- Ben Hesketh

- Raji Kolluru










