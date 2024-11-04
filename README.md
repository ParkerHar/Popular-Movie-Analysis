# Popular-Movie-Analysis :movie_camera:

## Overview

The goal of this project is to predict the financial success (world revenue) of a movie based on some information available before, or at, the movie’s release.

## Data

The dataset used in this project was built from IMDB and the numbers.com

The resulting dataset from IMDB included a wide variety of information such as title, director, average rating, genre and  runtime.

Unfortunately, I could not find a free dataset from IMDB that contained revenue and budget information. This is where the-numbers website came in handy. This website is updated daily with financial information on ~6500 of the biggest movies in the past 100 years. 

These datasets were combined using a “fuzzy” match to help mitigate any differences in the movie titles between the two websites.

## Initial Model

Once the data set was cleaned, I moved on to building the model to predict the world revenue of a movie.

After playing around with some feature selection I ended up with a few independent variables that will attempt to predict our dependant variable, world revenue.

These variables were Budget, Run Time, Average Rating, and number of Votes received.

A multivariate regression model was run and unfortunately yielded some very average performance. This model can only accurately predict the world revenue of a movie around 61% of the time. While a little bit disappointing, this helped me realize that there may be some relationships in my data set that I was missing. So I added the data to Tableau and started to build out some dashboards.

<img width="668" alt="Model Outcome" src="https://github.com/user-attachments/assets/d52b43f5-14ce-4b5f-962b-d8177a87ad4f">

## Movie Dashboard

<img width="1359" alt="Movie Dash" src="https://github.com/user-attachments/assets/55ba554a-0925-4626-9749-6f8f4af1dae3">

Taking a look at the movie industry as a whole we can start to see some relationships forming. As previously thought, there is a positive relationship between budget and revenue. However, this relationship is not as strong as initially anticipated.

Another interesting relationship is between return on investment and budget. This is something I would like to further review as these low budget/high revenue movies may be outliers in the data set, but they may also provide insight on factors that impact revenue beyond the budget.

## Genre Dashboard

<img width="1370" alt="Genre Dash" src="https://github.com/user-attachments/assets/1909eddd-b1fe-4ff3-bad5-f22346085bc8">

I wanted to look at the impact the film’s genre has on revenue. The word cloud represents the number of films per genre, while the tree map represents the world revenue per genre. We can see Drama has the highest number of films, however, in the treemap, we see that it does not generate the highest amount of revenue.

If we look at the top genres by revenue, some genres, such as adventure, have much higher average world revenues than others. This may indicate that Adventure movies are more likely to be financially successful, or at least are more likely to achieve high revenue numbers

## Director Dashboard

<img width="1369" alt="Director Dash" src="https://github.com/user-attachments/assets/3f4b607f-eb25-408d-8040-12cc6d1c3011">

Finally, I wanted to look at the people who play a major role in a films success, which are the directors. This dashboard indicates that there is a relationship between the director and the revenue generated. Films made by only the top 5 directors account for 5.6% of total global revenue while the top 10 directors are responsible for close to 10% of revenue.

When looking at each director we can start to see that there are some, Steven Spielberg for example, who have just directed a ton of movies to reach high revenue numbers. However, there are others like the Russo brothers, who have hit incredible numbers in a relatively few number of movies.

## Next Steps

As with most data projects, I would like to gather more data in general. Not just more movies, but more information per movie as well. Factors like the impact of a production studio or marketing budget on a film’s success may be interesting to examine.

With these newly gained insights I would like to continue building out features to use in my model. As seen in the dashboards, Genre and the director do impact a film’s success. Potentially using the average revenue generated per genre or per director could help improve the accuracy of my model and is something that I am excited to explore.






