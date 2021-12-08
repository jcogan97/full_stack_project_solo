# Python Solo Project

## Brief Overview

Aragains Gym is a project built within **Flask, SQL and HTML/CSS**.

Within the program, you can create/edit classes, view memberships for each member or create new bookings.

## Getting Started
### Dependencies
 * Flask
 * Python 3.9.0+
 * SQL

### Installation

To start, AragainsGym still requires you to run it from the user client in order to host the site on your own IP Address, which would be:
> localhost:5000

As for the files, you can fork it over to your own repository or download the code straight from this one.

### Running the Program

 * Within your terminal, this command:
```flask run```
 * Before you can run this program, you will need to create a Database within your Computer:
```createdb gym_queries```
 * Once you have done this, you can optionally restart the SQL Database to reset the tables with two commands to repopulate the tables with pre-made content.
 * **(Please make sure your terminal is inside the base folder where AragainsGym is stored before running this command line through the terminal)**
```psql -d gym_queries -f db/gym_queries.sql```

 * Now, you can go into your browser and go to (http://localhost:5000)
 
## Acknowledgements

Inspiration, code-snippets, etc

The CSS God - [Kevin Powell](https://www.youtube.com/kepowob)

CSS Buttons - [Federico Dossena](https://fdossena.com/?p=html5cool/buttons/i.frag)
