#!/bin/sh

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --csvpath)
    CSVPATH="$2"
    shift # past argument
    shift # past value
    ;;
    -i|--interactive)
    INTERACTIVE="-i"
    shift # past argument
    shift # past value
    ;;
	*)    # search term
    SEARCHTERM="$1"
    shift # past argument
    ;;
esac
done

CSVPATH="${CSVPATH:-$(pwd)/data/address_book.csv}"

docker run -it --mount type=bind,source="$CSVPATH",target=/app/address_book.csv -e interactive="$INTERACTIVE" -e searchterm="$SEARCHTERM" addressbook
