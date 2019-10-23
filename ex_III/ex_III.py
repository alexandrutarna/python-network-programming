import pandas as pd
import plotly.graph_objects as go


if __name__ == "__main__":
    
    # read CSV
    cow = pd.read_csv('countries_of_the_world.csv')

    # 1. Primele zece tari din punct de vedere al populatiei
    print("1. Primele zece tari din punct de vedere al populatiei")
    first_10_pop = cow.sort_values(ascending=False, by=['Population'])
    first_10_pop = first_10_pop['Country'].head(10)
    print(first_10_pop)

    # 2. Rata medie a natalitatii si a mortalitatii a tuturor tarilor din Europa
    print("2. Rata medie a natalitatii si a mortalitatii a tuturor tarilor din Europa")
    mean_birthrate = cow[(cow['Region'].str.contains('EUROPE'))]['Birthrate'].mean()
    mean_deathrate = cow[(cow['Region'].str.contains('EUROPE'))]['Deathrate'].mean()
    print ("    Rata natalitatii : ", mean_birthrate)
    print ("    Rata mortalitatii:", mean_deathrate)



    # 3. Alegeti aleator GDP ($ per capita) pentru 10 tari din Asia 
    #    si creati un grafic de tip Bar Chart folosind Plotly.
    print("3. GDP ($ per capita) pentru 10 tari din Asia si afisare Bar chart")
    ten_rand_countries = cow[(cow['Region'].str.contains('ASIA'))].sample(n=10)
    country_list = ten_rand_countries['Country']
    print(country_list)

    country_gdp_list = ten_rand_countries['GDP ($ per capita)']
    print(country_gdp_list)

    # display Bar chart
    fig = go.Figure([go.Bar(x=country_list, y=country_gdp_list)])
    fig.update_layout(title='GDP ($ per capita) pentru 10 tari din Asia',
                    xaxis_title='Tara',
                    yaxis_title='GDP ($ per capita)'
                    )
    fig.show()

    # 4. Tara cu cea mai mare suprafata agrara
    print("4. Tara cu cea mai mare suprafata agrara")
    cow.sort_values(ascending=False, by=['Arable (%)']) 
    surfaces = cow.sort_values(ascending=False, by=['Area (sq. mi.)'])
    surfaces['Arable Area'] = surfaces['Area (sq. mi.)'] * surfaces['Arable (%)']
    arable_bigest = surfaces.sort_values(ascending = False, by=['Arable Area'])
    arable_bigest = arable_bigest['Country'].head(1)
    
    print( "    " + arable_bigest )
