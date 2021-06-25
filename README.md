# Competitors Dashboard (Open-Source Version)

This repository contains code for displaying data from Parkopedia API in form of an interactive dashboard. The dahsboard is built as a web application using Flask. In this open-source version, all API credentials are missing.

## Description of contents

**app.py** - This is the main file which runs the webapp. It has a method for each subpage ( '/', '/showcase') and a method for creating the table and adding markers to a map on the results page. The subpage methods render the respective HTML templates (from templates folder).

**processing.py** - this is the backend Python script. It has methods for connecting with APIs (Parkopedia, OpenCage) and for generating CSV and XLSX files with results.

**requirements.txt** - the list of all dependencies required for the backend, in PIP format. These are primarly Python libraries which are installed in Azure when setting up the app.

**templates/input.html** - the template for the input page. This is the frontend in HTML and JavaScript. All variables in double squirrely brackets ( {{...}} ) come from backend and are passed on from app.py.

**templates/results.html** - the template for the results page. This is the frontend in HTML and JavaScript. All variables in double squirrely brackets ( {{...}} ) come from backend and are passed on from app.py. All code passed from backend need to have a marker 'safe' included ( {{...|safe}} ).

**static/styles.css** - A style script in CSS for design of both input and results pages. 

**static/scripts** - A folder for some tailor-made JavaScript scripts used for front-end responsiveness:
- *checkbox.js* - a function for updating different metrics and the map marker when a checkbox in the table (results page) is checked or unchecked.
- *coordinates.js* - decodes coordinates from a dragable (green) map marker to 2 floats for latitude and longitude
- *filter.js* - a function for updating the view when a user filters the results by an operator
- *highlight.js* - a function for highlighting (changing color) of a map marker when user clicks on a table row
- *icons.js* - describes design of all icons used on a map
