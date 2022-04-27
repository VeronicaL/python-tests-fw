# python-tests-fw

## Installation

1. Install Python 3.8.9.
2. Clone the project, navigate to project directory from your terminal, run:
```pip3 install -r requirements.txt```

## Preconditions
Simple [web-service](https://github.com/VeronicaL/java-web-service) (Spring-Boot) is UP on the local machine with supported endpoints:
* http://localhost:8080/library_dev/users - GET
* http://localhost:8080/library_dev/user - POST

Note: prod environment (http://localhost:8080/library/) hasn't supported yet,
it was used mostly to show how we deal with different environments.

## Running the tests
1. Clone the [web-service](https://github.com/VeronicaL/java-web-service) and start web-service
2. Clone the [python-project](https://github.com/VeronicaL/python-tests-fw)
3. Start all python tests, run ```python3 -m pytest --alluredir=test_results/ tests```
By default tests are running on dev environment (ENVIRONMENT=dev).
Note: we can set ENVIRONMENT from terminal using: ```export ENVIRONMENT=dev```


## Report
To generate the report, run ```allure serve test_results```
In the report we can see:
* Feature by stories
* Test's description
* Type of sent request with all parameters: url, data, headers, methods' name in 'Test body' section
* Attached log - detailed info about request and response

## Log file
After tests execution, all needed info (requests, responses, parameters, test's names) are written 
into logger.log


## How to run in docker:
1. From FW folder run: docker build -t pytest_check .
2. When a new image id ready, run:
   docker run --rm --mount type=bind,src="$(pwd)",target=/tests/ pytest_check

Note: with current web-server realisation (as it is only on localhost),
it won't be visible from container. We need to deploy our web-service, e.g. on Google Cloud.

## ToDo
* UI part of FW or contract testing
