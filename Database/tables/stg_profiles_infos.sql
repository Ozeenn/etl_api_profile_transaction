-- staging.stg_profile_infos definition

-- Drop table

-- DROP TABLE staging.stg_profile_infos;

CREATE TABLE staging.stg_profile_infos (
	des_job varchar(100) NULL,
	nom_company varchar(100) NULL,
	des_ssn varchar(50) NULL,
	des_residence varchar(200) NULL,
	num_latitude_atual numeric NULL,
	num_longitude_atual numeric NULL,
	des_blood_group varchar(5) NULL,
	nom_username varchar(100) NULL,
	nom_profile varchar(100) NULL,
	des_sex varchar(1) NULL,
	des_adress varchar(250) NULL,
	des_mail varchar(100) NULL,
	dat_birth date NULL,
	num_card varchar(20) NULL,
	des_card varchar(20) NULL,
	num_account varchar(6) NULL,
	dat_processamento timestamp NULL
);