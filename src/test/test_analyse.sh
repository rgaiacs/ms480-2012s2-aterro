echo '800-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=100 AND solver='aterro';"
echo '900-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=900 AND reduce=100 AND solver='aterro';"
echo '1000-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=1000 AND reduce=100 AND solver='aterro';"
echo 'r800-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=100 AND solver='raterro';"
echo 'r900-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=900 AND reduce=100 AND solver='raterro';"
echo 'r1000-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=1000 AND reduce=100 AND solver='raterro';"
echo 'r800-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=100 AND solver='aaterro';"
echo 'r900-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=900 AND reduce=100 AND solver='aaterro';"
echo 'r1000-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=1000 AND reduce=100 AND solver='aaterro';"
echo 'r800-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=100 AND solver='aaterro';"
echo 'r800-50'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=800 AND reduce=50 AND solver='aaterro';"
echo 'r900-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=900 AND reduce=100 AND solver='aaterro';"
echo 'r900-50'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=900 AND reduce=50 AND solver='aaterro';"
echo 'r1000-100'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=1000 AND reduce=100 AND solver='aaterro';"
echo 'r1000-50'
sqlite3 test.db "SELECT dtype, cols, rows, f_max, p_time, s_time FROM benchmark
WHERE problem='test/t1.ppm' AND maxd=1000 AND reduce=50 AND solver='aaterro';"
