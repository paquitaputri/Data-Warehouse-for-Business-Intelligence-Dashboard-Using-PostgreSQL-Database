#queries.py
transaksi_year = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        count(fakta_penjualan.nomer) as transaksi
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    GROUP BY
        ROLLUP (tahun)
    ORDER BY
        tahun;
""")
rollup_year_revenue = ("""
SELECT
    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
    sum(fakta_penjualan.harga) as revenue

FROM
    dim_waktu
INNER JOIN 
    fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
GROUP BY
    ROLLUP (tahun)
ORDER BY
    tahun;
""")

rollup_year_profit = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        sum(fakta_penjualan.profit) as profit

    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    GROUP BY
        ROLLUP (tahun)
    ORDER BY
        tahun;
""")


rollup_month_revenue = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('month', dim_waktu.tanggal), 'Month') AS bulan,
        sum(fakta_penjualan.harga) as revenue

    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    GROUP BY
        ROLLUP (tahun, date_trunc('month', dim_waktu.tanggal))
    ORDER BY
        tahun, date_trunc('month', dim_waktu.tanggal) ;
""")

rollup_month_profit = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('month', dim_waktu.tanggal), 'Month') AS bulan,
        sum(fakta_penjualan.profit) as profit

    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    GROUP BY
        ROLLUP (tahun, date_trunc('month', dim_waktu.tanggal))
    ORDER BY
        tahun, date_trunc('month', dim_waktu.tanggal) ;
""")

rollup_quarterly_revenue = ("""

    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        sum(fakta_penjualan.harga) as revenue

    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    GROUP BY
        ROLLUP (tahun, quarter)
    ORDER BY
        tahun, quarter;

""")

rollup_quarterly_profit = ("""

    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        sum(fakta_penjualan.profit) as profit

    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    GROUP BY
        ROLLUP (tahun, quarter)
    ORDER BY
        tahun, quarter;

""")

rollup_category_year_revenue = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        dim_kategori.nama_kategori as kategori,
        sum(fakta_penjualan.harga) as revenue
    FROM
        fakta_penjualan
    INNER JOIN 
        dim_waktu ON fakta_penjualan.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_pesanan ON fakta_penjualan.pesanan_id = dim_pesanan.pesanan_id
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

rollup_category_year_profit = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        dim_kategori.nama_kategori as kategori,
        sum(fakta_penjualan.profit) as profit
    FROM
        fakta_penjualan
    INNER JOIN 
        dim_waktu ON fakta_penjualan.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_pesanan ON fakta_penjualan.pesanan_id = dim_pesanan.pesanan_id
    INNER JOIN
        dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
    INNER JOIN
        dim_subkategori ON dim_produk.subkategori_id  = dim_subkategori.subkategori_id
    INNER JOIN
        dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
    GROUP BY
        ROLLUP (tahun,kategori)
    ORDER BY
        tahun, kategori;
""")

rollup_category_month_revenue = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('month', dim_waktu.tanggal), 'Month') AS bulan,
        dim_kategori.nama_kategori as kategori,
        sum(fakta_penjualan.harga) as revenue
    FROM
        fakta_penjualan
    INNER JOIN 
        dim_waktu ON fakta_penjualan.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_pesanan ON fakta_penjualan.pesanan_id = dim_pesanan.pesanan_id
    INNER JOIN
        dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
    INNER JOIN
        dim_subkategori ON dim_produk.subkategori_id  = dim_subkategori.subkategori_id
    INNER JOIN
        dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
    GROUP BY
        ROLLUP (tahun, date_trunc('month', dim_waktu.tanggal),kategori)
    ORDER BY
        tahun, date_trunc('month', dim_waktu.tanggal),kategori;
""")

rollup_category_month_profit = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('month', dim_waktu.tanggal), 'Month') AS bulan,
        dim_kategori.nama_kategori as kategori,
        sum(fakta_penjualan.profit) as profit
    FROM
        fakta_penjualan
    INNER JOIN 
        dim_waktu ON fakta_penjualan.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_pesanan ON fakta_penjualan.pesanan_id = dim_pesanan.pesanan_id
    INNER JOIN
        dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
    INNER JOIN
        dim_subkategori ON dim_produk.subkategori_id = dim_subkategori.subkategori_id
    INNER JOIN
        dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
    GROUP BY
        ROLLUP (tahun, date_trunc('month', dim_waktu.tanggal),kategori)
    ORDER BY
        tahun, date_trunc('month', dim_waktu.tanggal),kategori;
""")

rollup_category_quarterly_revenue = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        dim_kategori.nama_kategori as kategori,
        sum(fakta_penjualan.harga) as revenue
    FROM
        fakta_penjualan
    INNER JOIN 
        dim_waktu ON fakta_penjualan.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_pesanan ON fakta_penjualan.pesanan_id = dim_pesanan.pesanan_id
    INNER JOIN
        dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
    INNER JOIN
        dim_subkategori ON dim_produk.subkategori_id  = dim_subkategori.subkategori_id
    INNER JOIN
        dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
    GROUP BY
        ROLLUP (tahun, quarter, kategori)
    ORDER BY
        tahun, quarter, kategori;
""")

rollup_category_quarterly_profit = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        dim_kategori.nama_kategori as kategori,
        sum(fakta_penjualan.profit) as profit
    FROM
        fakta_penjualan
    INNER JOIN 
        dim_waktu ON fakta_penjualan.tanggal_id = dim_waktu.tanggal_id
    INNER JOIN
        dim_pesanan ON fakta_penjualan.pesanan_id = dim_pesanan.pesanan_id
    INNER JOIN
        dim_produk ON dim_pesanan.produk_id = dim_produk.produk_id 
    INNER JOIN
        dim_subkategori ON dim_produk.subkategori_id  = dim_subkategori.subkategori_id
    INNER JOIN
        dim_kategori ON dim_subkategori.kategori_id = dim_kategori.kategori_id
    GROUP BY
        ROLLUP (tahun, quarter, kategori)
    ORDER BY
        tahun, quarter, kategori;
""")
region_revenue = ("""
    SELECT
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    GROUP BY
        ROLLUP (region)
    ORDER BY
        region;
""")
region_revenue_year = ("""
    SELECT
	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
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
region_profit = ("""
    SELECT
        nama_region as region,
        sum(fakta_penjualan.profit) as profit
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    GROUP BY
        ROLLUP (region)
    ORDER BY
        region;
""")
region_profit_year = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        nama_region as region,
        sum(fakta_penjualan.profit) as profit
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
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
region_revenue_2015 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2015'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_revenue_2016 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2016'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_revenue_2017 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2017'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_revenue_2018 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2018'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_profit_2015 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.profit) as profit
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2015'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_profit_2016 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.profit) as profit
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2016'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_profit_2017 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.profit) as profit
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2017'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_profit_2018 = ("""
    SELECT
	    to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
	nama_region as region,
	    sum(fakta_penjualan.profit) as profit
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
	WHERE
		to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2018'
    GROUP BY
        ROLLUP (tahun, region)
    ORDER BY
        tahun, region;
""")
region_revenue_2015_quarter1 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '1' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2015'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2015_quarter2 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '2' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2015'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2015_quarter3 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '3' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2015'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2015_quarter4 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '4' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2015'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2016_quarter1 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_tanggal_pesanan.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '1' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2016'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2016_quarter2 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '2' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2016'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2016_quarter3 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '3' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2016'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2016_quarter4 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '4' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2016'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2017_quarter1 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '1' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2017'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2017_quarter2 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '2' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2017'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2017_quarter3 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_tanggal_pesanan
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '3' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2017'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2017_quarter4 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_tanggal_pesanan
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '4' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2017'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2018_quarter1 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '1' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2018'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2018_quarter2 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '2' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2018'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2018_quarter3 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '3' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2018'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")
region_revenue_2018_quarter4 = ("""
    SELECT
        to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') as tahun,
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') AS quarter,
        nama_region as region,
        sum(fakta_penjualan.harga) as revenue
    FROM
        dim_waktu
    INNER JOIN 
        fakta_penjualan ON dim_waktu.tanggal_id = fakta_penjualan.tanggal_id
    INNER JOIN
        dim_kota ON fakta_penjualan.kota_id = dim_kota.kota_id
    INNER JOIN
        dim_provinsi ON dim_kota.provinsi_id = dim_provinsi.provinsi_id
    INNER JOIN
        dim_negara ON dim_provinsi.negara_id = dim_negara.negara_id
    INNER JOIN
        dim_region ON dim_negara.region_id = dim_region.region_id
    WHERE
        to_char(date_trunc('quarter', dim_waktu.tanggal), 'Q') = '4' AND 	to_char(date_trunc('year', dim_waktu.tanggal), 'YYYY') = '2018'
    GROUP BY
        ROLLUP (tahun, quarter, region)
    ORDER BY
        tahun, quarter, region;
""")