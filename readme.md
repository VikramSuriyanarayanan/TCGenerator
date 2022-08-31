<h5> What is this project about? </h5>

This project will help with updating and fetching Tranfer certificate
details from mysql db. 

<h5> Backend information: </h5>

Ensure you install the required dependencies:
<code>
pip install mysql-connector-python
</code>

Details of table are given below:
<blockquote>
<code>
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
); </code>
</blockquote>

