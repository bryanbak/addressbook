#!/bin/bash

display_usage() {
	echo "usage: run.sh [-i | --interactive] [--csvpath <path>] [<searchterm>]"
	echo "if run in interactive mode <searchterm> is ignored"
	echo "if not in interactive mode then <searchterm> is required"
	echo "csvpath defaults to data/address_book.csv if omitted"
}

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
    ;;
	*)    # unknown value
	SEARCHTERM="$1"
	if [[ ${SEARCHTERM:0:1} == "-" ]]
	then
		echo "unknown argument $1"
		display_usage
		exit 1
	fi
    
    shift # past argument
    ;;
esac
done

if [ "$SEARCHTERM" = "" ] && [ "$INTERACTIVE" = "" ]
then
	display_usage
	exit 1
fi

CSVPATH="${CSVPATH:-$(pwd)/data/address_book.csv}"

docker run -it --mount type=bind,source="$CSVPATH",target=/app/address_book.csv -e interactive="$INTERACTIVE" -e searchterm="$SEARCHTERM" addressbook
