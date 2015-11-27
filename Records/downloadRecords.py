import urllib
url = "http://property.spatialest.com/nc/durham/phpcode/createExcel.php?cond=2005-03-01_2005-03-28_saledate:"
recordname = "2005-3.xls"
urllib.urlretrieve (url, recordname)