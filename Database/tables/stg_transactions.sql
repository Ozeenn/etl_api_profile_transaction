-- staging.stg_transactions definition

-- Drop table

-- DROP TABLE staging.stg_transactions;

CREATE TABLE staging.stg_transactions (
	etl_id varchar(100) NOT NULL,
	cod_mcc varchar(4) NULL,
	vlr_transaction numeric NULL,
	dat_transaction timestamp NULL,
	nom_city varchar(100) NULL,
	nom_country varchar(100) NULL,
	CONSTRAINT stg_transactions_pkey null
);