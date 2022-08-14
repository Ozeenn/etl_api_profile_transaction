-- etl_api.tb_transactions definition

-- Drop table

-- DROP TABLE etl_api.tb_transactions;

CREATE TABLE etl_api.tb_transactions (
	etl_id varchar(100) NULL,
	cod_mcc varchar(4) NULL,
	vlr_transaction numeric NULL,
	dat_transaction timestamp NULL,
	nom_city varchar(100) NULL,
	nom_country varchar(100) NULL
);