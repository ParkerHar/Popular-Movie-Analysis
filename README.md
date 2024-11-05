# Popular-Movie-Analysis :movie_camera:

## Overview :eyes:

The goal of this project is to predict the financial success (world revenue) of a movie based on some information available before, or at, the movie’s release.

Being able to predict the success of a film has the potential to help us gain a deeper understanding of the film industry, and in more real terms, could help stakeholders feel more confident investing money into certain projects.

## Data  :chart_with_upwards_trend:

The data used in this project was built from IMDB and the-numbers.

The resulting dataset contains a bunch of information about movies including the director, genre, rating, and revenue.

These datasets were combined using a “fuzzy” match to help mitigate any differences in the movie titles between the two websites.

## Initial Model  :construction:

Once the data set was cleaned, I moved on to building the model to predict the world revenue of a movie.

This was built around 4 predictor variables: Budget, Run Time, Average Rating, and number of Votes received.

A multivariate model was run and unfortunately yielded some very average performance. This model can only accurately predict the world revenue of a movie around 60% confidence. Compared to similar project online this is a below average score as other models are performing at around 75%

<img width="668" alt="Model Outcome" src="https://github.com/user-attachments/assets/d52b43f5-14ce-4b5f-962b-d8177a87ad4f">

However, this performance inspired me to dig deeper into my dataset to uncover some more relationships and potential features to use in future models.

## Movie Dashboard

<img width="1363" alt="Movie Dash" src="https://github.com/user-attachments/assets/b3a8432f-9607-4895-b65e-93b91a91cbd2">

Taking a look at the movie industry as a whole we can start to see some relationships forming. As previously thought, there is a positive relationship between budget and revenue. However, this relationship is not as strong as initially anticipated.

Another interesting relationship is between return on investment and budget. This is something I would like to further review as these low budget/high revenue movies may be outliers in the data set, but they may also provide insight on factors that impact revenue beyond the budget.

## Genre Dashboard

<img width="1367" alt="Genre Dash" src="https://github.com/user-attachments/assets/d6789281-d45f-4fc0-8351-5b835706f340">

I wanted to look at the impact the film’s genre has on revenue. The word cloud represents the number of films per genre, while the tree map represents the world revenue per genre. We can see Drama has the highest number of films, however, in the treemap, we see that it does not generate the highest amount of revenue.

If we look at the top genres by revenue, some genres, such as adventure, have much higher average world revenues than others. This may indicate that Adventure movies are more likely to be financially successful, or at least are more likely to achieve high revenue numbers

## Director Dashboard

<img width="1359" alt="Director Dash" src="https://github.com/user-attachments/assets/4e9115be-9b0a-446a-921a-4b9135b1d970">

Finally, I wanted to look at the people who play a major role in a films success, which are the directors. This dashboard indicates that there is a relationship between the director and the revenue generated. Films made by only the top 5 directors account for 5.6% of total global revenue while the top 10 directors are responsible for close to 10% of revenue.

When looking at each director we can start to see that there are some, Steven Spielberg for example, who have just directed a ton of movies to reach high revenue numbers. However, there are others like the Russo brothers, who have hit incredible numbers in a relatively few number of movies.

## Next Steps :pencil:

With these newly gained insights I would like to continue building out features to use in my model. As seen in the dashboards, Genre and the director do impact a film’s success. Potentially using the average revenue generated per genre or per director could help improve the accuracy of my model and is something that I am excited to explore.

A linear regression model was used in this project. While user friendly, there are more robust model out there and I plant to implement more advanced machine learning techniques to help improve the model’s accuracy

As with most data projects, I would like to gather more data in general. Not just more movies, but more information per movie as well. Factors like the impact of a production studio or marketing budget on a film’s success may be interesting to examine.






