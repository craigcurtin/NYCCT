## Process each element in the pipeline, using the
## cmdlet-style keywords to visit each element in $input
function Get-InputWithKeyword($identifier) {
    begin    {
        Write-Host "Beginning InputWithKeyword (ID: $identifier)"
    }
    process {
        Write-Host "Processing element $_ (ID: $identifier)"
        $_
    }
    end {
        Write-Host "Ending InputWithKeyword (ID: $identifier)"
    }
}