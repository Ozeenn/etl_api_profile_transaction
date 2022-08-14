CREATE OR REPLACE PROCEDURE staging.proc_insert_tb_profile_infos()
 LANGUAGE plpgsql
AS $procedure$
	BEGIN
		insert into etl_api.tb_profile_infos
		select 
			md5(num_card || num_account) as id,
			nom_profile,
			nom_username,
			des_sex,
			dat_birth,
			des_blood_group,
			des_ssn,
			des_mail,
			des_residence,
			des_adress,
			num_latitude_atual,
			num_longitude_atual,
			des_job,
			nom_company,
			num_card,
			des_card,
			num_account,
			dat_processamento
		from staging.stg_profile_infos;

	END;
$procedure$
;
