#!/usr/bin/env python3
import urllib

monthEndDate = [("01","31"), ("02","28"), ("03","31"), ("04","30"), ("05","31"), ("06", "30"), ("07", "31"), ("08","31"), ("09","30"),("10","31"),("11","30"),("12","31")]


for year in range(2005,2016):
	yearStr = str(year)
	for date in monthEndDate:
		url = "http://property.spatialest.com/nc/durham/phpcode/createExcel.php?cond="+yearStr+"-"+date[0]+"-01_"+yearStr+"-"+date[0]+"-"+date[1]+"_saledate:111_luc:"
		recordname = yearStr+"-"+date[0]+".xls"
		print(url)
		urllib.urlretrieve(url, recordname)





# url = "http://property.spatialest.com/nc/durham/phpcode/createExcel.php?cond=2005-03-01_2005-03-28_saledate:"
# recordname = "2005-3.xls"
# urllib.urlretrieve (url, recordname)