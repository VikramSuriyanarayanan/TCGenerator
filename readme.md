<h4> What is this project about? </h4>

This project will help with updating and fetching Transfer certificate
details from mysql db. 

<h4> Backend information: </h4>
<body>
Ensure you install the required dependencies:

```
pip install mysql-connector-python
pip install pandas
```

Details of my-sql table is given below:

```
CREATE TABLE transfer_certificate
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the student
  name            VARCHAR(150) NOT NULL,                # Name of the student
  father_name     VARCHAR(150) NULL,                    # Name of the father
  mother_name     VARCHAR(150) NULL,                    # Name of the mother
  nationality     VARCHAR(150) NULL,                    # Nationality
  conduct         VARCHAR(150) NOT NULL,                # Conduct - Good, Bad
  remark          VARCHAR(1500) NULL,                   # Other comments if any
  PRIMARY KEY     (id)                                  # Make the id the primary key
); 
```
</body>
<h4> How to run it in local? </h4>

- Install the needed dependencies as mentioned above.
- Download the input file to same location where `main.py` is downloaded
- Run the following command `python main.py`
- Table output should look something like ![this]( https://github.com/VikramSuriyanarayanan/TCGenerator/blob/d68a3355036b9d54340da34081463b2c5d6e925e/table_output.png)
- Python output should look something like ![this](https://github.com/VikramSuriyanarayanan/TCGenerator/blob/d68a3355036b9d54340da34081463b2c5d6e925e/python_output.png)


<h4> Important Links: </h4>

- For getting started with mysql : [MySQL Getting started](https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing)
- Ensure you have pip installed in windows/mac [Pip installer](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
- Download pycharm community edition if needed [Pycharm Installer for Windows](https://www.jetbrains.com/pycharm/download/#section=windows)
