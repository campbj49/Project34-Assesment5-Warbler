+make log out button actually work
+header image, bio, and location now display on user profiles
+bio showing on user cards in followers,following, and list_user pages
+edit user page now functions correctly
+homepage now only shows warbles of logged in user and followed users

- How is the logged in user being kept track of? session[CURR_USER_KEY]
- What is Flask’s ***g*** object? An extendable object that behaves like a JavaScript object that is global to the whole of app.py
- What is the purpose of ***add_user_to_g ?*** It adds the current user to Flask's global variable ***g***
- What does ***@app.before_request*** mean? It's a function that runs every time before a request is completed, meaning that it can set the globale variables every time a page is loaded

+add like functionality to thumbs up buttons
+added likes page that shows all liked messages of logged in user