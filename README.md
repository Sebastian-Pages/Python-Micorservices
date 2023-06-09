# Micro Services

This repository contains a collection of microservices built using a globe architecture. Each microservice serves a specific purpose and can be independently deployed and scaled. This projects was made following a tutorial at https://www.freecodecamp.org/news/python-microservices-course/

## Description

The Micro Services project is designed to demonstrate a microservices architecture. It consists of multiple services that work together to provide a complete solution. The services communicate with each other using RabbitMQ as the message broker and rely on a MySQL database for data storage.

## Technologies Used

The project utilizes the following technologies:

- Django: A Python web framework used for building one of the microservices.
- Flask: A lightweight Python web framework used for building another microservice.
- RabbitMQ: A message broker that enables communication between the microservices.
- MySQL: A relational database management system used for data storage.
- Docker: A containerization platform used to package and run the microservices.

## Prerequisites

Make sure you have the following dependencies installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## How to Run the Project

To run the Micro Services project locally using Docker, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/micro_services.git`
2. Navigate to the project directory: `cd micro_services/admin` and `cd micro_services/main`
3. Set the AMQP_URL value in the dfocker-compose file of each microservice
4. Build the Docker containers for the microservices: `docker-compose build`
5. Start the microservices: `docker-compose up`
6. Access the application using the provided URLs or endpoints.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue on the project repository.

## License

The Micro Services project is available under the [MIT License](LICENSE).