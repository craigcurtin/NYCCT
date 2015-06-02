function AreThereBikesRideSchool
{
    $url = "https://www.car2go.com/api/v2.1/vehicles?loc=New%20York%20City&oauth_consumer_key=car2gowebsite&format=json"
    $json = (Invoke-RestMethod $url)
    write-host "time of Cars2Go data:  "  $json.executionTime
    write-host $json.placemarks

    #$json | Where-Object { $_.stationName -like "*Liberty*" }
    $json | Where-Object { $_.engineType -like "*E" }
}