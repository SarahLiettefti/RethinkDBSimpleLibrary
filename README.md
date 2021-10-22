# RethinkDBSimpleLibrary
As part of our NoSQL course at ecam, we had to create a project on a database. We have created a small library in order to test some functionality of the DB.

# How to use it
## Downnload the server
For windows system download the zip on this [link](https://download.rethinkdb.com/#browse/search=keyword%3Dwindows%2Frethinkdb:c770169c0b2e3ed872bbbb55a6612794:36e3dec8de528c9b9b0ee2d823ec6a67)

## Install the Python client driver
`
pip install rethinkdb
`

You may have to install `pandas` for this project.
`
pip install pandas
`

## Start the first server
 Open a command prompt window and use `cd` command to go to the directory where you saved `rethinkdb.exe` then execute it.
 `
C:\Users\sarah>cd Documents\rethinkdb-2.3.6
C:\Users\sarah\Documents\rethinkdb-2.3.6>rethinkdb.exe -–bind all
`
### To connect another machin on this server 
 `
C:\Users\sarah>cd Documents\rethinkdb-2.3.6
C:\Users\sarah\Documents\rethinkdb-2.3.6>rethinkdb.exe –join IP_FIRST_MACHINE:29015 --bind all
`

## Run the project
To create the table used, run the `runonce.py` file. Don't run it twice or you will inssert twice the data on the table.

Then run the `main.py` file to use the library.
 
## Features
You can choose a operation by typing :
R to rent a book (next you have to precise the name of book and if you wrote a mistake, it suggests you books)
T to return a book
S to search a book
