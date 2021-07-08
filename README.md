# QS-university-ranking-scraper

# Requirements:
- Install imports
- Excel or similar tool installed
- Modify paths of the script 

# CSV Delimiter issues:
- When opening CSV in Excel, Ctrl+A to grab all cells then click on data -> convert to table and select comma as delimiter then apply changes to correctly implement delimiter and clearly setup columns in your file for better organisation. 

# Future plans: 
- Fix CSV issue, automatically separate data into columns
- Add each university's topuniversity.com website to the list of collected data

# How to use on different year rankings:
- QS global university ranking page is loaded through Ajax. So to extract the url for other years. 
- Inspect element -> Network -> XHR -> Refresh page -> Select the 3rd name: 'random integer' +.txt? -> Select Header and copy the url.

# Credits:
- Zyingzhou
