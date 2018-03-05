# About
Address-Book lookup application
Written in python and setup to run inside a docker container

# Build
To build the docker image simply execute the build script
```bash
build.sh
```

# Run
To start the container and do address lookups execute the run.sh script

The simplest way to run it is to pass the search term as an arg to the script
```bash
run.sh "tacoma, wa"
```

If you want to do multiple searches you can run in interactive mode
```bash
run.sh -i
```

You can specify the location of the csv file with addresses in it.
If not specified it defaults to using the address_book.csv file in the data directory
```bash
run.sh -i --csvpath "/path/to/address_file.csv"
```

When the run script is executed it launches the docker container and mounts the csv file
inside the container at the root.

The path to the CSV file must be somewhere that docker can access.
If using Docker toolbox for windows it only has access to C:\Users by default.
This gets mapped to /c/Users in the vm so you'll have to use that style of path
if using the toolbox. If you need more access you have to add shared folders via virtualbox
(see: https://docs.docker.com/toolbox/toolbox_install_windows/)

# Search strings
Pretty much anything should work. You can search by name or any of the various parts of the address

# Tests
Unit tests can be run in their own container by executing the test script
```bash
test.sh
```
