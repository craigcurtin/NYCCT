function InputCounter2 {
    begin    {
        $count = 0
    }
    ## Go through each element in the pipeline, and add up
    ## how many elements there were.
    process    {
        Write-Debug "Processing element $_"
        $count++
    }

    end    {
        $count
    }
}