To run this application, clone this repo:
> create a virtual environment
> pip install - r requirements.txt
> python run.py

Go to http://127.0.0.1:5000/offer with a refresh of the page the qualifying offer will be updated

I used the beautiful soup, re (RegEx), and requests libraries to complete this assignment. I took
a functional programming approach by using list comprehensions and the "sorted" function and sorting
in reverse. I handled cases where the salary field was empty or invalid by filter on data that 
included a "$". I converted string to ints by removing commas in a list comprehension as well. With
the data being formatted correctly and I was able to calculate a qualifying offer of the top 125 players.

The answer to questions 1 can be found in Questions1.md