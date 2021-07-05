# workoutTracker

A Python workout tracker using Google Sheets, Sheety and Nutritionix

## Instructions:

Register to get the following free API keys:<br>
https://www.nutritionix.com/business/api<br>
https://sheety.co/<br>

Make a copy of the this sheet for your Google account:
https://docs.google.com/spreadsheets/d/1VQPVH708ybRw3joWtow4SdAOT2CDBHr-dQPUTfvLAHI/edit#gid=0<br>

Create a new project in Sheety and link it to your Google spreadsheet.<br>
Set authentication in Sheety to Bearer auth and create a token.<br>

Set the following environment variables:<br>
APP_ID (Nutritionix Application ID)<br>
API_KEY (Nutritionix API key)<br>
TOKEN (Sheety Bearer token)<br>
SHEET_ENDPOINT (The link to your Sheety sheet)<br>

Sheety expects your record to be nested in a singular root property named after your sheet. For example if your endpoint is named emails, nest your record in a property called email.
See https://sheety.co/docs/requests

## Example Input:
ran 5 miles, cycled 40 minutes
