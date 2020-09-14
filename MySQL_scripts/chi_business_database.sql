DROP DATABASE IF EXISTS chi_business;
CREATE DATABASE chi_business;

USE chi_business;
DROP TABLE IF EXISTS
	business,
	license_info,
	license_loc,
	owners;

CREATE TABLE IF NOT EXISTS business (
    lic_id 		INT NOT NULL,
    acct_no 	INT NOT NULL,
    legal_name 	VARCHAR(256) NOT NULL,
    dba 		VARCHAR(256),
    bus_act 	VARCHAR(750),
    PRIMARY KEY (lic_id)
);

CREATE TABLE IF NOT EXISTS license_info (
    lic_id 			INT NOT NULL,
    lic_descr 		VARCHAR(65) NOT NULL,
    lic_start_date 	DATE NOT NULL,
    lic_exp_date 	DATE NOT NULL,
    FOREIGN KEY (lic_id)
        REFERENCES business (lic_id)
        ON DELETE CASCADE,
    PRIMARY KEY (lic_id)
);

CREATE TABLE IF NOT EXISTS license_loc (
	lic_id 		INT NOT NULL,
    address 	VARCHAR(100) NOT NULL,
    city 		VARCHAR(35) NOT NULL,
    state 		VARCHAR(2) NOT NULL,
    zip_code 	INT,
    FOREIGN KEY (lic_id)
        REFERENCES business (lic_id)
        ON DELETE CASCADE,
    PRIMARY KEY (lic_id)
);

CREATE TABLE IF NOT EXISTS owners (
    acct_no 	INT NOT NULL,
    first_name 	VARCHAR(50),
    last_name 	VARCHAR(50),
    title 		VARCHAR(30)
);