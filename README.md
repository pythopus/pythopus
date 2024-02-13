![image](https://github.com/pytopus/pytopus/assets/2507085/b72b3617-2922-4620-a41b-02a31d6a5cb0)

# pytopus
Pytopus, your ultimate python octopus pet companion!

## What is it?

This project is about connecting APIs together.

## Why am I building this

For years, I've been looking for a tool which can help me interconnect output of APIs to input of others. Unfortunately, I've always been left sad with the tools and solutions I found. Either they were too complicated to use because of overwealming useless features, or they are too simple and missing part of the need. Anyhow, that's why I decided to start building my own API Octopus in Python. The name comes from the cross of the words Python and Octopus as it acts like a gigantic Octopus connecting APIs together using Python language.

## How to build
```bash
docker ...
```
blah blah blah ...

## How to run
```bash
docker ...
```
blah blah blah ...

## Architecture

### High level View
The design of Pytopus platform follows an industry-grade architecture that includes a modern frontend, an API built with Flask (Python), caching, a backend queue system, a modern data store, and search engine capabilities.

-==[ INSERT HERE ARCHITECTURE DIAGRAM ]==-

### Vision
This architecture ensures a scalable, resilient, and high-performing application, leveraging modern technologies for each component of the system. Docker and Kubernetes provide the flexibility to scale parts of the system independently, based on demand, while Redis and RabbitMQ ensure the application remains responsive and efficient.

With the inclusion of both MongoDB and PostgreSQL in the architecture, we're looking at a versatile setup that leverages the strengths of both a NoSQL and a relational database. This setup can cater to various data storage needs, such as unstructured or semi-structured data in MongoDB for flexibility and scalability, and structured data in PostgreSQL for transactions and complex queries. 

This architecture combines the strengths of relational and NoSQL databases to support a wide range of data types and access patterns, offering flexibility, scalability, and robustness necessary for a modern web application.

### Overview
- User Interaction: Users interact with the application through the ReactJS frontend, which communicates with the Flask backend for data operations.

- API Layer: Flask serves as the conduit between the frontend and the databases (MongoDB and PostgreSQL), deciding which database to query based on the data structure and requirements. It leverages Redis for caching to improve performance.

- Data Storage:
  - Structured Data: PostgreSQL stores structured data that benefits from relational database features like transactions and complex queries.
  - Unstructured/Semi-Structured Data: MongoDB stores data that doesn't fit neatly into tables, such as JSON documents, for flexibility and scalability.

- Search and Analysis: Elasticsearch indexes data from MongoDB and/or PostgreSQL to provide fast search capabilities across the application's data.

- Asynchronous Processing: RabbitMQ queues tasks for background processing, allowing the Flask application to remain responsive to user requests.

- Scalability and Resilience: Docker and Kubernetes ensure that each component can be independently scaled and managed, providing a robust infrastructure.

- Monitoring and Operational Insight: Prometheus and Grafana offer real-time monitoring, while Graylog provides centralized logging for debugging and monitoring application health.


### Choosen Components 
Let's outline each component and its role in our architecture:

- Frontend: ReactJS

    Provides the user interface, utilizing ReactJS for its efficient and interactive UI capabilities. It communicates with the Flask API to send and receive data.

- API: Flask (Python)
    
    Serves as the backend application server, handling requests from the React frontend. Flask interacts with both MongoDB and PostgreSQL databases, Redis cache, Elasticsearch for search, and RabbitMQ for queue management.

- Caching System: Redis
    Enhances performance by caching frequently accessed data, reducing database load and speeding up response times.

- Backend Queue System: RabbitMQ
    Manages background tasks and asynchronous processing, improving application responsiveness and scalability.

- Modern Data Store: PostgreSQL & MongoDB
    - PostgreSQL: Acts as the primary relational database for structured data, supporting transactions and complex queries with ACID compliance.
    - MongoDB: Provides a flexible, schema-less data store for unstructured or semi-structured data, offering scalability and rapid development.

- Search Engine Capabilities: Elasticsearch
    Offers powerful full-text search capabilities over large volumes of data, enhancing the user search experience.

- Containerization and Orchestration: Docker & Kubernetes
    Docker containers encapsulate each component, with Kubernetes managing deployment, scaling, and management in production environments.

- Monitoring and Logging:
    - Prometheus & Grafana for monitoring and visualization: Track application performance and metrics.
    - Graylog for centralized logging: Aggregate logs for operational insights and troubleshooting.

## History

