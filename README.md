#CLOUD-DEVOPS-LAB
Cloud DevOps Technical Assessment - CartFul Solutions

TASK 1 | Cloud Architecture Components Diagram
  Scenario: A mid-sized e-commerce company is planning to migrate its on-premise infrastructure to leverage cloud technologies for better scalability, reliability, and service
  availability capabilities. The company has a set of 3 microservices that are based on docker images deployed in one on-premise server, a relational database and a non
  relational database which stores configurations as JSON records. The company expects to migrate the on-premise services into the cloud using AWS Services. The company is
  also keen on ensuring high service availability and horizontal scaling for the docker based service leveraging security best practices.
  
  Given the previous scenario, you are requested to take into consideration the following
  requirements:
    • The 3 docker based microservices should scale on-demand by using your recommended AWS docker orchestration service. For illustration purposes, let the microservices
    names be:
        - user_metadata microservice, listening at port 1010.
        - flight_metadata microservice, listening at port 2020.
        - flights_availability microservice, listening at port 3030.
    • The docker based microservices should balance incoming traffic across all available services within the orchestration cloud service.
    • Only the Load Balancer should be publicly reachable from the internet.
    • The VPC should have at least 3 public and 3 private subnets.
    • The solutions should be deployed across different availability zones.
    • Docker based microservices should not be reachable from the internet but the microservices are required to have access to the internet.
    • Principle of Least Privilege should be implemented for service communication between relational database and docker based microservices.
    • Ensure high levels of security and privacy.
    • Relational Database should only allow connections from the docker based microservices and allow traffic within private network only.
    • Non-relational database service should allow connections from the Docker based microservice.
    • All docker based microservices should use a single static IP address when reaching services out of the VPC. For illustration purposes, use the static IP address
    55.55.55.55/32 when specifying the AWS resource that will allocate this static IP address in your diagram.
    • Explicitly specify the network components of the VPC that will host the docker based microservices and database. Such as route tables, gateways, Static IPs resource,
    Load Balancer open port(s), Load Balancer Type, etc.

  Design a top-level AWS cloud data architecture diagram for the e-commerce company, your design should focus on scalability, security, and availability. You can use Lucid
  Chart.
  
  Task Deliverable:
    Create a visual diagram that describes how would you deploy and allocate the previous requirements, make sure to include the following resources:
    • Network Components:
        - VPC, ACLs, Route Table, Gateway, Security Group, Availability Zone, Subnet, etc.
    • Microservice Orchestration:
        - Microservices deployed using your recommended AWS Service.
    • Relational Database:
        - Relational Database AWS Service deployed.
    • Non-relational database:
        - Non-relational Database AWS Service deployed.
    • Security and Compliance:
        - Detail the security measures (e.g., encryption types, identity and access management, network security).
    • Scalability and Reliability:
        - Describe through which AWS Service would you enable scalability for the microservices.
    
  The diagram should serve as a comprehensive guide for the e-commerce company to understand your proposed cloud-based architecture and the services involved. In a real
  world scenario, this would help the DevOps team develop the Infrastructure as Code and collaborate with you as a team.
________________________________________________________________________________________________________________________________________________________________________________

TASK 2 | NASA API Script CI/CD Automation
  Develop a single python script using NASA´s NeoWs (Near Earth Object Web Service) API to extract data about near-Earth objects (NEOs). The goal of the script is to perform a
  request to NASA’s API
  
  You can create as many functions you need in a single file, name the python script “get_data.py”. The objective of the file is to simply perform a GET request to the NASA API
  endpoint specified in the next section and store the content received as a JSON file in the path output/response.json. Once you have the script developed, build a dockerfile
  image that will run that script as entrypoint. Finally, develop a basic CI/CD pipeline using the CI/CD of your choice that builds the docker image, runs the docker image
  locally, gets the file from the /app/output/response.json and echo the files content.
  
  API Documentation: https://api.nasa.gov/
  
  Expected Steps:
    1) Build the get_data.py script:
        a) Get familiar with NeoWs API to retrieve data about NEOs. Generate your free API Key and take into consideration the Daily API Rate Limits for this test.
        b) Use the API Endpoint “Neo - Browse” and use the page 1755 as filter. Extract the results.
        c) Convert the API response as a JSON object and store it as a JSON file in the output/response.json filename path.
    2) Dockerize the script:
        a) Create a Dockerfile where the entrypoint executes the get_data.py script
        b) Manage your API Key securely.
        c) Define a shared container volume /app/output/ so you can have access to the generated output file once the container is executed.
        d) Build the docker image
        e) Run the docker image
        f) Validate the output/response.json file generated after executing the docker image
    3) CI/CD:
        a) Choose your CI/CD tool of preference, you can use CircleCI free version
        b) Develop a basic CI/CD pipeline with the following stages:
            i) Build the docker image
            ii) Run the docker image
            iii) Print/Echo the generated output file content “output/response.json”
            iv) Configure the pipeline to be triggered on every commit of the Github repository
________________________________________________________________________________________________________________________________________________________________________________

TASK 3 | NASA API Script Lambda Handler
  Given the previous get_data.py script, write the equivalent of the script as if it was a Lambda Function. Create a lambda_handler.py file and convert the script as a lambda
  function. Use as a Lambda Handler parameter, the “page” argument filter to enable parametrized page data filter (instead of a static “1755” value) to fetch data from NASA´s
  API, this way the Lambda would receive the page value as an invocation parameter. It is not required to execute or deploy the Lambda.
  
      
