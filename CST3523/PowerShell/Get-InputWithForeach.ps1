

Set-StrictMode -Version 3
## Process each element in the pipeline, using a
## foreach statement to visit each element in $input
function Get-InputWithForeach($identifier) {
    Write-Host "Beginning InputWithForeach (ID: $identifier)"
    foreach($element in $input) {
        Write-Host "Processing element $element (ID: $identifier)"
        $element
    }
    Write-Host "Ending InputWithForeach (ID: $identifier)"
}