import requests
import json

def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def replace_template_with_data(template, data):
    for key, value in data.items():
        template = template.replace(f"{{{{GetUser.{key}}}}}", str(value))
    return template

def execute_api_call(call_config, prev_responses):
    method = call_config.get("method")
    url = call_config.get("url")
    headers = call_config.get("headers", {})
    payload = call_config.get("payload", {})
    query_params = call_config.get("query_params", {})
    
    # Template replacement
    if prev_responses:
        query_params = {k: replace_template_with_data(v, prev_responses) for k, v in query_params.items()}

    response = requests.request(method, url, headers=headers, json=payload, params=query_params)
    return response.json()

def main(config_path):
    config = load_config(config_path)
    api_chain = config.get("api_chain", [])
    responses = {}

    for api_call in api_chain:
        response = execute_api_call(api_call, responses.get(api_call['name']))
        responses[api_call['name']] = response
        print(f"Response from {api_call['name']}: {response}")

if __name__ == "__main__":
    main("config.json")
