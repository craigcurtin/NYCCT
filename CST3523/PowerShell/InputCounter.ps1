function InputCounter {
	$count = 0
	## Go through each element in the pipeline, and add up
	## how many elements there were.
	foreach($element in $input)	{
		$count++
	}
	$count
}