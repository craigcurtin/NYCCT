## f2c.ps1

## Convert Fahrenheit to Celsius
function ConvertFahrenheitToCelsius($fahrenheit)
{
    $celsius = $fahrenheit - 32
    $celsius = $celsius / 1.8
    return $celsius
}

write-output  "32F is :" $ConvertFahrenheitToCelsius(32)