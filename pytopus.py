import requests
import json
from datetime import datetime

def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def replace_template_with_data(template, data):
    # Improved templating to handle more complex nested structures
    for key, value in data.items():
        template = template.replace(f"{{{{steps[{key}].output.{value}}}}}", str(data[key]))
    return template

def execute_api_call(call_config, prev_responses):
    method = call_config.get("method")
    url = call_config.get("url")
    headers = call_config.get("headers", {})
    # Initialize payload and query_params as None
    payload = None
    query_params = None
    
    if method.upper() == "POST":
        payload = call_config.get("body", {})
        if isinstance(payload, dict):
            payload = {k: replace_template_with_data(v, prev_responses) if isinstance(v, str) else v for k, v in payload.items()}
    elif method.upper() == "GET":
        query_params = call_config.get("queryParams", {})
        if isinstance(query_params, dict):
            query_params = {k: replace_template_with_data(v, prev_responses) if isinstance(v, str) else v for k, v in query_params.items()}

    response = requests.request(method, url, headers=headers, json=payload, params=query_params)
    return response.json()

def map_output(output_mapping, response):
    mapped_output = {}
    for key, path in output_mapping.items():
        keys = path.split('.')
        temp_response = response
        for k in keys:
            temp_response = temp_response.get(k, {})
        mapped_output[key] = temp_response
    return mapped_output

def main(config_path):
    config = load_config(config_path)
    api_chain = config.get("steps", [])
    prev_responses = {}

    for step in api_chain:
        response = execute_api_call(step, prev_responses)
        if "outputMapping" in step:
            prev_responses[step['step']] = map_output(step["outputMapping"], response)
        print(f"Response from step {step['step']}: {response}")

if __name__ == "__main__":
    main("config.json")