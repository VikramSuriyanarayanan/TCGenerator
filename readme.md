<h4> What is this project about? </h4>

This project will help with updating and fetching Tranfer certificate
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


<h4> Important Links: </h4>
- [MySQL Getting started] (https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing).
