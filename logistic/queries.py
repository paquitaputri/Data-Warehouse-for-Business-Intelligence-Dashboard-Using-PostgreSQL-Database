rollup_otif_year = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 AND (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) as otif
	from
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	GROUP BY
		ROLLUP (tahun)
	ORDER BY
		tahun;
""")
rollup_ontime_year = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 THEN 1 END) AS on_time
	from
		fakta_penjualan
	INNER JOIN 
		fakta_pengiriman ON fakta_penjualan.nomer = fakta_pengiriman.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	GROUP BY
		ROLLUP (tahun)
	ORDER BY
		tahun;
""")
rollup_infull_year = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		count(CASE WHEN (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) AS in_full
	from
		fakta_penjualan
	INNER JOIN 
		fakta_pengiriman ON fakta_penjualan.nomer = fakta_pengiriman.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	GROUP BY
		ROLLUP (tahun)
	ORDER BY
		tahun;
""")
pengiriman_rollup_year = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		count(*) as transaksi
	from
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	GROUP BY
		ROLLUP (tahun)
	ORDER BY
		tahun;
""")
rollup_infull_month = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		to_char(date_trunc('month', dim_waktu.tanggal), 'Month') AS bulan,
		count(CASE WHEN (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) AS in_full
	from
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	GROUP BY
		ROLLUP (tahun, date_trunc('month', dim_waktu.tanggal))
	ORDER BY
		tahun, date_trunc('month', dim_waktu.tanggal);
""")
pivot_infull_month = ("""
	SELECT * FROM crosstab(
				'SELECT
					to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
					to_char(date_trunc(''month'', dim_waktu.tanggal), ''Month'') AS bulan,
					count(CASE WHEN (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) AS in_full
				from
					fakta_pengiriman
				INNER JOIN 
					fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
				INNER JOIN
					dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
				GROUP BY
					ROLLUP (tahun, date_trunc(''month'', dim_waktu.tanggal))
				ORDER BY
					tahun, date_trunc(''month'', dim_waktu.tanggal);'
	) AS final_result(
	Tahun TEXT, January BIGINT, February BIGINT, March BIGINT, April BIGINT, May BIGINT, June BIGINT, July BIGINT, August BIGINT, September BIGINT, October BIGINT, November BIGINT, December BIGINT
	);

""")
rollup_ontime_month = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		to_char(date_trunc('month', dim_waktu.tanggal), 'Month') AS bulan,
		count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 THEN 1 END) AS on_time
	from
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	GROUP BY
		ROLLUP (tahun, date_trunc('month', dim_waktu.tanggal))
	ORDER BY
		tahun, date_trunc('month', dim_waktu.tanggal);

""")
rollup_region_pengiriman = ("""
    SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        nama_region as region,
        count(fakta_pengiriman) as jumlah_pengiriman
	FROM
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_kota ON fakta_pengiriman.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
rollup_region_otif_per_year = ("""
    SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        nama_region as region,
        count(CASE WHEN fakta_penjualan.tanggal_id = fakta_pengiriman.tanggal_id AND fakta_penjualan.jumlah_barang = fakta_pengiriman.barang_diterima THEN 1 END) as otif
	FROM
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_kota ON fakta_pengiriman.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
rollup_category_otif = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		dim_kategori.nama_kategori as kategori,
		count(CASE WHEN fakta_penjualan.tanggal_id = fakta_pengiriman.tanggal_id AND fakta_penjualan.jumlah_barang = fakta_pengiriman.barang_diterima THEN 1 END) as otif
	FROM
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	INNER JOIN
		dim_pesanan ON fakta_pengiriman.pesanan_id = dim_pesanan.pesanan_id
	INNER JOIN
		dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
	INNER JOIN
		dim_subkategori ON dim_produk.subkategori_id  = dim_subkategori.subkategori_id
	INNER JOIN
		dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
	GROUP BY
		ROLLUP (tahun, kategori)
	ORDER BY
		tahun, kategori;
""")
rollup_category_pengiriman = ("""
	SELECT
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
		dim_kategori.nama_kategori as kategori,
		count(*) as jumlah_pengiriman
	FROM
		fakta_pengiriman
	INNER JOIN 
		fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
	INNER JOIN
		dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
	INNER JOIN
		dim_pesanan ON fakta_pengiriman.pesanan_id = dim_pesanan.pesanan_id
	INNER JOIN
		dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
	INNER JOIN
		dim_subkategori ON dim_produk.subkategori_id  = dim_subkategori.subkategori_id
	INNER JOIN
		dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
	GROUP BY
		ROLLUP (tahun, kategori)
	ORDER BY
		tahun, kategori;
""")
pivot_ontime_month = ("""
	SELECT * FROM crosstab(
					'SELECT
						to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
						to_char(date_trunc(''month'', dim_waktu.tanggal), ''Month'') AS bulan,
						count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 THEN 1 END) AS on_time
					from
						fakta_pengiriman
					INNER JOIN 
						fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
					INNER JOIN
						dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
					GROUP BY
						ROLLUP (tahun, date_trunc(''month'', dim_waktu.tanggal))
					ORDER BY
						tahun, date_trunc(''month'', dim_waktu.tanggal);'
	) AS final_result(
		Tahun TEXT, January BIGINT, February BIGINT, March BIGINT, April BIGINT, May BIGINT, June BIGINT, July BIGINT, August BIGINT, September BIGINT, October BIGINT, November BIGINT, December BIGINT
	);
""")
pivot_otif_month = ("""
	SELECT * FROM crosstab(
				'SELECT
					to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
					to_char(date_trunc(''month'', dim_waktu.tanggal), ''Month'') AS bulan,
					count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 AND (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) as otif
				from
					fakta_pengiriman
				INNER JOIN 
					fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
				INNER JOIN
					dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
				GROUP BY
					ROLLUP (tahun, date_trunc(''month'', dim_waktu.tanggal))
				ORDER BY
					tahun, date_trunc(''month'', dim_waktu.tanggal);'
	) AS final_result(
		Tahun TEXT, January BIGINT, February BIGINT, March BIGINT, April BIGINT, May BIGINT, June BIGINT, July BIGINT, August BIGINT, September BIGINT, October BIGINT, November BIGINT, December BIGINT
	);
""")
pivot_pengiriman_month = ("""
	SELECT * FROM crosstab(
				'SELECT
					to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
					to_char(date_trunc(''month'', dim_waktu.tanggal), ''Month'') AS bulan,
					count(*) as transaksi
				from
					fakta_pengiriman
				INNER JOIN 
					fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
				INNER JOIN
					dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
				GROUP BY
					ROLLUP (tahun, date_trunc(''month'', dim_waktu.tanggal))
				ORDER BY
					tahun, date_trunc(''month'', dim_waktu.tanggal);'
	) AS final_result(
		Tahun TEXT, January BIGINT, February BIGINT, March BIGINT, April BIGINT, May BIGINT, June BIGINT, July BIGINT, August BIGINT, September BIGINT, October BIGINT, November BIGINT, December BIGINT
	);

""")
pivot_ontime_quarter = ("""

	SELECT * FROM crosstab(
				'SELECT
					to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
					to_char(date_trunc(''quarter'', dim_waktu.tanggal), ''Q'') AS quarter,
					count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 THEN 1 END) AS on_time
				from
					fakta_pengiriman
				INNER JOIN 
					fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
				INNER JOIN
					dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
				GROUP BY
					ROLLUP (tahun, quarter)
				ORDER BY
					tahun, quarter;'
	) AS final_result(
		Tahun TEXT, Quarter_1 BIGINT, Quarter_2 BIGINT, Quarter_3 BIGINT, Quarter_4 BIGINT
	);

""")
pivot_infull_quarter = ("""
	SELECT * FROM crosstab(
					'SELECT
						to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
						to_char(date_trunc(''quarter'', dim_waktu.tanggal), ''Q'') AS quarter,
						count(CASE WHEN (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) AS in_full
					from
						fakta_pengiriman
					INNER JOIN 
						fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
					INNER JOIN
						dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
					GROUP BY
						ROLLUP (tahun, quarter)
					ORDER BY
						tahun, quarter;'
	) AS final_result(
		Tahun TEXT, Quarter_1 BIGINT, Quarter_2 BIGINT, Quarter_3 BIGINT, Quarter_4 BIGINT
	);

""")
pivot_otif_quarter = ("""
	SELECT * FROM crosstab(
					'SELECT
						to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
						to_char(date_trunc(''quarter'', dim_waktu.tanggal), ''Q'') AS quarter,
						count(CASE WHEN (fakta_penjualan.tanggal_id - fakta_pengiriman.tanggal_id ) >= 0 AND (fakta_penjualan.jumlah_barang - fakta_pengiriman.barang_diterima ) = 0 THEN 1 END) as otif
					from
						fakta_pengiriman
					INNER JOIN 
						fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
					INNER JOIN
						dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
					GROUP BY
						ROLLUP (tahun, quarter)
					ORDER BY
						tahun, quarter;'
	) AS final_result(
		Tahun TEXT, Quarter_1 BIGINT, Quarter_2 BIGINT, Quarter_3 BIGINT, Quarter_4 BIGINT
);
""")
pivot_pengiriman_quarter = ("""
	SELECT * FROM crosstab(
					'SELECT
						to_char(date_trunc(''year'', dim_waktu.tanggal), ''YYYY'') as tahun,
						to_char(date_trunc(''quarter'', dim_waktu.tanggal), ''Q'') AS quarter,
						count(*) as transaksi
					from
						fakta_pengiriman
					INNER JOIN 
						fakta_penjualan ON fakta_pengiriman.nomer = fakta_penjualan.nomer
					INNER JOIN
						dim_waktu on fakta_pengiriman.tanggal_id = dim_waktu.tanggal_id
					GROUP BY
						ROLLUP (tahun, quarter)
					ORDER BY
						tahun, quarter;'
	) AS final_result(
		Tahun TEXT, Quarter_1 BIGINT, Quarter_2 BIGINT, Quarter_3 BIGINT, Quarter_4 BIGINT
	);
""")