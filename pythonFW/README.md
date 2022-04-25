# python-api-automation

written in
### Python 3, py.test


## Installation

1. Download [Python 3.9](https://www.python.org/downloads/)
2. Install Python from the downloaded package.
3. Clone the project, navigate to project directory from your terminal, run:
```pip3 install -r requirements.txt```

## Running the tests
Simple web-service (Spring-Boot) is UP on the local machine with supported endpoints:
* http://localhost:8080/library_dev/users - GET
* http://localhost:8080/library_dev/user - POST

Note: prod environment (http://localhost:8080/library/) hasn't supported yet,
it was used mostly to show how we deal with different environments.

To start all python tests, run ```python3 -m pytest --alluredir=test_results/ tests```
By default tests are running on dev environment (ENVIRONMENT=dev).


## Report
To generate the report, run ```allure serve test_results```
In the report we can see:
* Feature by stories
* Test's description
* Type of sent request with all parameters: url, data, headers, methos name in 'Test body' section
* Attached log - detailed info about request and response

## Log file
After tests execution, all needed info (requests, resposes, parameters, test's names) are written 
into logger.log


## How to run in docker:
1. From FW folder run: docker build -t pytest_check .
2. When a new image id ready, run:
   docker run --rm --mount type=bind,src="$(pwd)",target=/tests/ pytest_check

Note: with current web-server realisation (as it is only on localhost),
it won't be visible from container. We need to deploy it.
