# Data Engineering of Customer Data to produce Scalability

### Prerequisites

#### Python 3.6.* or later.
> 
> See installation instructions at: https://www.python.org/downloads/
> 
> Check you have python3 installed:
> ```bash
> python3 --version
> ```

#### Preferably an IDE such as Sublime Editor
>
>[https://www.sublimetext.com/download](https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe)


### Dependencies and data

#### Creating a virtual environment
>
> Ensure your pip (package manager) is up to date:
> ```bash
> pip3 install --upgrade pip
> ```
> 
> To check your pip version run:
> ```bash
> pip3 --version
> ```
> 
> Install virtualenv:
> ```bash
> pip3 install virtualenv
> ```
> 
> Create the virtual environment in the root of the cloned project:
> ```bash
> virtualenv -p python3 .venv
> ```

#### Activating the newly created virtual environment
> 
> You always want your virtual environment to be active when working on this project.
> 
> ```bash
> source ./.venv/bin/activate 
> ```

#### Installing Python requirements
>
> This will install some of the packages you might find useful:  
> ```bash
> pip3 install -r ./requirements.txt
> 
> ```

#### Running tests to ensure everything is working correctly
> 
> ```bash
> pytest ./tests
> ```

#### Generating the data
>
> A data generator is included as part of the project in `./input_data_generator/main_data_generator.py`
> This allows you to generate a configurable number of months of data.
> Although the technical test specification mentions 6 months of data, it's best to generate
> less than that initially to help improve the debugging process.

> To run the data generator use:
> ```bash
> python ./input_data_generator/main_data_generator.py
> ```

> This should produce customers, products and transaction data under `./input_data/starter`


#### Getting started
The scalability of the generated data are being produced in the *solution* folder due course of following steps:

1)solution_start.py :A resultant dataset has been produced which maps the generated data whie creating a json like [{customer_id:C5},{loyalty_score:7},{product_id:P09},{product_category:House}]

2)data_invoke_to_database.py :Creating a mongo-database from the above mentioned json.

3)app.py :A RestAPI uisng Flask Framework is generated for bridging server-side and client-side reponses.Customer_id is being taken as an request and correponding server-side reponse will be the details belongs to the given customer-id.
