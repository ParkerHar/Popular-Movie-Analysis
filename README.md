# Popular-Movie-Analysis :movie_camera:

## Overview :eyes:

The goal of this project is to predict the financial success (world revenue) of a movie based on some information available before, or at, the movie’s release.

Being able to predict the success of a film has the potential to help us gain a deeper understanding of the film industry, and in more real terms, could help stakeholders feel more confident investing money into certain projects.

## Data  :chart_with_upwards_trend:

The data used in this project was built from IMDB and the-numbers.

The resulting dataset contains a bunch of information about movies including the director, genre, rating, and revenue.

These datasets were combined using a “fuzzy” match to help mitigate any differences in the movie titles between the two websites.

## Initial Model  :construction:

Once the data set was cleaned, I moved on to building the model to predict world revenue

This was built around 4 predictor variables: Budget, Run Time, Average Rating, and number of Votes received.

A multivariate model was run and unfortunately yielded some very average performance. This model can only accurately predict the world revenue of a movie around 60% confidence. Compared to similar projects, this is a below average score as other models are performing at around 75%

<img width="668" alt="Model Outcome" src="https://github.com/user-attachments/assets/d52b43f5-14ce-4b5f-962b-d8177a87ad4f">

However, this performance inspired me to dig deeper into my dataset to uncover some more relationships and potential features to use in future models. The following dashboard are publically available at:

[Tableau Movie Dashboards](https://public.tableau.com/shared/PFNFRTPGX?:display_count=n&:origin=viz_share_link)

## Movie Dashboard

<img width="1363" alt="Movie Dash" src="https://github.com/user-attachments/assets/b3a8432f-9607-4895-b65e-93b91a91cbd2">

Taking a look at the movie industry as a whole we can start to see some relationships forming. As previously thought, there is a positive relationship between budget and revenue. However, this relationship is not as strong as initially anticipated.

Another interesting relationship is between return on investment and budget. This is something I would like to further review as these low budget/high revenue movies may be outliers in the data set, but they may also provide insight on factors that impact revenue beyond the budget.

## Genre Dashboard

<img width="1367" alt="Genre Dash" src="https://github.com/user-attachments/assets/d6789281-d45f-4fc0-8351-5b835706f340">

I then wanted to look at the impact between genre and revenue. 

There are some genres that dominate in terms of revenue per film, such as sci-fi and adventure. However there are also some interesting comparisons in the 'low revenue' cluster. Some genres are more expensive to make and achieve similar financial numbers as ‘cheaper’ genres. 

The difference between History and Horror is fairly striking. Horror movies cost around $12M less to make and produce $8M dollars more revenue than the average History movie. This shows that a horror movie may potentially be a safer investment than a History film.

## Director Dashboard

<img width="1359" alt="Director Dash" src="https://github.com/user-attachments/assets/4e9115be-9b0a-446a-921a-4b9135b1d970">

Finally, I wanted to look at the people who play a major role in a films success, which are the directors. This dashboard indicates that there is a relationship between the director and the revenue generated. Films made by only the top 5 directors account for 5.6% of all total revenue.

When looking at each director we can start to see that there are some, Steven Spielberg for example, who have just directed a ton of movies to reach high revenue numbers. However, there are others like the Russo brothers, who have hit incredible numbers in a relatively few number of movies.

## Next Steps :pencil:

With these newly gained insights I would like to continue building out features to use in my model. As seen in the dashboards, Genre and the director do impact a film’s success. Potentially using the average revenue generated per genre or per director could help improve the accuracy of my model and is something that I am excited to explore.

A linear regression model was used in this project. While user friendly, there are more robust model out there and I plan to implement more advanced machine learning techniques to help improve the model’s accuracy

As with most data projects, I would like to gather more data in general. Not just more movies, but more information per movie as well. Factors like the impact of a production studio or marketing budget on a film’s success may be interesting to examine.






