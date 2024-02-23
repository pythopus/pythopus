![Pythopus](https://github.com/pythopus/pythopus/assets/2507085/8b20e957-9637-43a4-a45d-c3475c9a2215)

# Pythopus
Unleashing the Power of API Integration with the Flexibility of Python!

## What is it?
Pythopus is a sophisticated API Orchestrator designed to streamline the integration and management of multiple API services. By enabling the creation of configurable chains, it seamlessly orchestrates the flow of data between APIs, facilitating the efficient handling of inputs and outputs in a cascading manner. This approach not only simplifies complex API interactions but also enhances the automation and scalability of interconnected systems, making it an invaluable tool for developers looking to optimize their digital infrastructure.

## Why am I building this
For years, I've been looking for a tool that can effortlessly bridge the outputs of multiple APIs with the inputs of others, forming a continuous, interconnected sequence of calls starting from a single one first API call. Unfortunately, my search often ended in disappointment. The tools and solutions I encountered were either overwhelmingly complex, cluttered with superfluous features, or disappointingly simplistic, lacking essential functionalities. Driven by these frustrations, I embarked on a journey to create my own solution. Thus, Pythopus was born—a name that marries 'Python' with 'Octopus', symbolizing its ability to adeptly link APIs together through the power of the Python language, much like an octopus connects its tentacles.

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
1. Create a api config file, example `jsonplaceholder.config.json` file in the same directory than the application. 

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

  ![image](https://github.com/pythopus/pythopus/assets/60453790/9257efc2-e766-46ff-b361-62160825fc1a)


## Running Pythopus
Execute Pythopus by running:

```bash
python pythopus.py
```
## Configuration Guide
TODO: add details on configuring API chains, including examples and parameter explanations.

## Architecture
TODO: provide architecture diagram and details.

## Built With
- Flask - The web framework used
- Docker - Containerization

## Contributing
We welcome contributions from the community! If you'd like to contribute, please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the GNU AFFERO General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Credits
[@floriangrousset](https://github.com/floriangrousset) ~ Project lead
<br/>[@antonyjaen](https://github.com/antonyjaen) ~ Project co-lead
