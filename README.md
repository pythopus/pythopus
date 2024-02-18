![Pythopus](https://github.com/pythopus/pythopus/assets/2507085/8b20e957-9637-43a4-a45d-c3475c9a2215)

# Pythopus

Unleashing the Power of API Integration with the Flexibility of Python!

## What is it?

Pythopus is a sophisticated API Orchestrator designed to streamline the integration and management of multiple API services. By enabling the creation of configurable chains, it seamlessly orchestrates the flow of data between APIs, facilitating the efficient handling of inputs and outputs in a cascading manner. This approach not only simplifies complex API interactions but also enhances the automation and scalability of interconnected systems, making it an invaluable tool for developers looking to optimize their digital infrastructure.

## Why am I building this

For years, I've been on the quest for a tool capable of seamlessly interconnecting the output of one API to the input of another. Unfortunately, my search often ended in disappointment. The tools and solutions I encountered were either overwhelmingly complex, cluttered with superfluous features, or disappointingly simplistic, lacking essential functionalities. Driven by these frustrations, I embarked on a journey to create my own solution. Thus, Pythopus was born—a name that marries 'Python' with 'Octopus', symbolizing its ability to adeptly link APIs together through the power of the Python language, much like an octopus connects its tentacles.


## Features

- **Configurable API Chains**: Define and execute sequences of API calls, managing the flow of data from one service to another.
- **Dynamic Data Mapping**: Automate the mapping of output from one API as input to another, reducing manual coding and potential errors.
- **Extensible Connector Library**: Leverage a growing library of API connectors or easily add your own to integrate with various services.
- **User-Friendly Interface**: A straightforward configuration format that abstracts away the complexity of API integration.
- **Python-Powered**: Built with Python, ensuring ease of use for developers familiar with the language and promoting community contributions.

## Further Enhancements
- **Dynamic Date Handling**: Integrate functionality to automatically update the last_modified date whenever the configuration is changed.
- **Configuration Management**: Implement a system to manage multiple configurations, potentially storing them in a database like MongoDB or PostgreSQL with appropriate timestamps and retrieval mechanisms.
- **Advanced Templating**: Extend the templating system to handle more complex data extraction and manipulation from API responses, possibly using a more sophisticated templating engine or custom parsing logic.

## Getting Started

### Prerequisites

- Python 3.6 or later
- `requests` library

### Installation

1. Clone the Pythopus repository:
   ```bash
   git clone https://github.com/pythpus/pythopus.git
   ```
2. Navigate to the Pythopus directory:
    ```bash
    cd pythopus
    ```
3.Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a api config file `jsonplaceholder.config.json` file in /src/api_configs directory. Refer to the Configuration Guide for details.

2. Example [api_name].config.json:

    ```json
    {
        "api_name": "Example API",
        "base_url": "https://jsonplaceholder.typicode.com",
        "authentication": {
            "type": "OAuth 2.0",
            "token_url": "https://jsonplaceholder.typicode.com/oauth/token",
            "client_id": "your_client_id",
            "client_secret": "your_client_secret"
        },
        "endpoints": [
            {
                "name": "Get Users",
                "method": "GET",
                "url": "/users",
                "description": "Get the list of users",
                "response_body": {
                    "data":[...],
                    "pageInfo":{}
                }
            },
            {
                "name": "Create User",
                "method": "POST",
                "url": "/users",
                "description": "Create a new user",
                "request_body": {
                    "username": "string",
                    "password": "string",
                    "email": "string"
                }
            },
            {
                "name": "Get User Details",
                "method": "GET",
                "url": "/users/{user_id}",
                "description": "Get details of a specific user",
                "url_parameters": {
                    "user_id": "string"
                },
                "response_body": {
                    "data": [...],
                    "pageInfo": {}
                }
            },
            {
                "name": "Update User",
                "method": "PUT",
                "url": "/users/{user_id}",
                "description": "Update details of a user",
                "url_parameters": {
                    "user_id": "string"
                },
                "request_body": {
                    "username": "string",
                    "email": "string"
                }
            }
        ]
    }
    ```
3. Visual representation of the configuration:

   ![image](https://github.com/pythopus/pythopus/assets/2507085/2a85d013-4928-40e0-8fee-749ce2ced125)

## Running Pythopus

Execute Pythopus by running:

```bash
python pythopus.py
```

## Configuration Guide

Detailed information on configuring your API chains, including examples and parameter explanations, can be found [here](future-link).

## Architecture

### High level View
The design of Pythopus platform follows an industry-grade architecture that includes a modern frontend, an API built with Flask (Python), caching, a backend queue system, a modern data store, and search engine capabilities.

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

## Contributing
We welcome contributions from the community! If you'd like to contribute, please follow our Contributing Guidelines.

## License
Pythopus is licensed under the GNU Affero General Public License Version 3. See the LICENSE file for more details.

## Acknowledgments and Credits
Thanks to all the contributors who have helped shape Pythopus.
Inspired by the flexibility and capability of both the Python programming language and the adaptability of octopuses.
For more information, visit our GitHub repository or contact the project maintainers.

[@floriangrousset](https://github.com/floriangrousset) ~ Project lead
<br/>[@antonyjaen](https://github.com/antonyjaen) ~ Project co-lead
