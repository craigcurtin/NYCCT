# prompt user for file name ... similar to Linux 'which', finds in path


param([string] $file=$(throw "Please specify a filename."))

(get-command $file).Definition