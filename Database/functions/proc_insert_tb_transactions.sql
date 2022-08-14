CREATE OR REPLACE PROCEDURE staging.proc_insert_tb_transactions()
 LANGUAGE plpgsql
AS $procedure$
	begin
		truncate table etl_api.tb_transactions;
		insert into etl_api.tb_transactions
		select 
			*
		from staging.stg_transactions;

	END;
$procedure$
;
