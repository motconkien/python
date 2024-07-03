Working with Errors and JSON File by updating the Password Manager App(Day29)
Level: immediate
Add on:
1. Use JSON file to store data
2. Add a "Search" button next to the website entry field
3. Adjust layout and the other widgets as needed to get the desired look
4. Create a function called find_password() that gets triggered when the "Search" button is presses
5. Check if the user's text entry matches an item in the data.json
6. If yes, show a messagebox with the website's name and password
7. Catch an exception that might occur trying to access the data.json showing a messagebox with the text: "No Data file found"
8. If the user's website doesn't exist inside the data.json, show a messagebox that reads "No details for the website exists"