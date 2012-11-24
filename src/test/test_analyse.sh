echo "max. distancia,rows,cols,value,process,solver,rows,cols,value,process,solver" > maxd.csv
sqlite3 test.db "SELECT a.*, b.rows, b.cols, b.f_max, b.p_time,
b.s_time FROM (SELECT maxd, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND reduce=50 AND solver='aaterro' AND
dtype=2) a JOIN (SELECT maxd, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t2.ppm' AND reduce=50 AND solver='aaterro' AND
dtype=2) b ON a.maxd = b.maxd;" | sed 's/|/,/g' >> maxd.csv
echo "reduce,rows,cols,value,process,solver,rows,cols,value,process,solver" > reduce.csv
sqlite3 test.db "SELECT a.*, b.rows, b.cols, b.f_max, b.p_time, b.s_time FROM
(SELECT reduce, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND solver='aaterro' AND
dtype=2) a JOIN (SELECT reduce, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t2.ppm' AND maxd=800 AND solver='aaterro' AND
dtype=2) b ON a.reduce = b.reduce;" | sed 's/|/,/g' >> reduce.csv
echo "solver,rows,cols,value,process,solver,rows,cols,value,process,solver" > solver.csv
sqlite3 test.db "SELECT a.*, b.rows, b.cols, b.f_max, b.p_time, b.s_time FROM
(SELECT solver, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=50 AND
dtype=2) a JOIN (SELECT solver, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t2.ppm' AND maxd=800 AND reduce=50 AND
dtype=2) b ON a.solver = b.solver;" | sed 's/|/,/g' >> solver.csv
echo "tipo distancia,rows,cols,value,process,solver,rows,cols,value,process,solver" > dtype.csv
sqlite3 test.db "SELECT a.*, b.rows, b.cols, b.f_max, b.p_time, b.s_time FROM
(SELECT dtype, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=50 AND
solver='aaterro') a JOIN (SELECT dtype, rows, cols, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t2.ppm' AND maxd=800 AND reduce=50 AND
solver='aaterro') b ON a.dtype = b.dtype;" | sed 's/|/,/g' >> dtype.csv
