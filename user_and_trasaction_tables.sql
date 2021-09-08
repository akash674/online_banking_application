USE online_banking;
CREATE TABLE user(
account_no bigint primary key AUTO_INCREMENT,
first_name varchar(30) NOT NULL,
last_name varchar(20),
dob date NOT NULL,
gender varchar(10),
aadhar bigint,
pan char(10),
net_banking_id bigint,
net_banking_password varchar(20),
account_balance double,
ifsc_code char(11),
address varchar(100),
pincode int
)

ALTER TABLE user AUTO_INCREMENT=1000;

select * from user;

CREATE TABLE Transaction(
transaction_id int PRIMARY KEY auto_increment,
tran_date date,
withdrawals_ammount float,
deposit_ammount float,
transfer_fund float,
from_account int,
to_account int,
comment varchar(100)
)
ALTER TABLE Transaction AUTO_INCREMENT=5000;
select * from  Transaction;

delete from Transaction where transaction_id=1000;
drop Transaction;

