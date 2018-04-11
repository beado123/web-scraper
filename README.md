# web_scraper
A Python web scraper that scrapes information from over 250 actors and 125 movies wikipedia pages, builds graph library to store data and save in JSON file. Builds methods for graph Queries and performs data analysis. Creates API for it.
## builder.py
Graph queries handled at run time.
## analysis.py
Short summary on data scraped and analysis on hub actors and correlation between age and grossing value of an actor. 
## app.py
Web API with following endpoints:

| Endpoints                 | Actions | Intended Outcome                                     |
|---------------------------|---------|------------------------------------------------------|
| /actors                   | POST    | Create a new actor.                                  |                         
| /actors?attr={attr_value} | GET     | Respond with actors that satisfy the attribute       |
| /actors/<actor_name>      | GET     | Respond with a specific actor                        |
|                           | PUT     | Replace entire actor with supplied actor             |
|                           | DELETE  | Delete specified actor or 404 error                  |
| /movies                   | POST    | Create a new movie.                                  |
| /movies?attr={attr_value} | GET     | Respond with movies that satisfy the attribute       |
| /movies/<movie_name>     | GET     | Respond with a specific movie                        |
|                           | PUT     | Replace entire movie with supplied movie             |
|                           | DELETE  | Delete specified movie or 404 error                  |
