<#
PowerShell Script for CS3523
https://raw.githubusercontent.com/metalx1000/MyBin/master/windows/powershell/arguments.ps1
#>

Write-Host "All Arguments are $args"

Write-Host "Each Argument is:"
foreach ($arg in $args){  
    Write-Host "Arg: $arg";
}