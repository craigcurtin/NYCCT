Write-Output "Downloading File..."

$storageDir = $pwd
$webclient = New-Object System.Net.WebClient
$url = "https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi"
$file = "python-2.7.10.msi"
$webclient.DownloadFile($url,$file)

Write-Output "File Downloaded"