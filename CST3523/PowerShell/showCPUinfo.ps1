# display CPU information in a HTML page

# calls WMI to get CPU info, then formats page as HTML, saves as a file and then displays HTML output in browser
get-wmiobject -class Win32_Processor | 
convertto-html DeviceID,Name,CurrentClockSpeed,LoadPercentage -head "<title>CPU details for $env:computername</title>`n<style type=`"text/css`">`nbody { padding: 8px; line-height: 1.33 }`ntable { border-style: ridge }`ntd, th { padding: 10px; border-style: dotted; border-width: 1px }`nth { font-weight: bolder; text-align: center }`n</style>" | 
out-file -FilePath "showcpuh.html" -Encoding "ASCII"

invoke-item "showcpuh.html"