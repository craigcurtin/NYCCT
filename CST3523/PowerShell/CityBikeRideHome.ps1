function AreThereBikesRideSchool
{
    $url = 'http://www.citibikenyc.com/stations/json'
    $json = (Invoke-RestMethod $url)
    write-host "time of CitiBike data:  "  $json.executionTime
    $json.stationBeanList | Where-Object { $_.stationName -like "*Liberty*" }
}



function AreThereBikesRideHome
{
    $url = 'http://www.citibikenyc.com/stations/json'
    $json = (Invoke-RestMethod $url)
    $json.executionTime
    $json.stationBeanList | Where-Object { $_.stationName -like "*Broadway*" }
}