install.packages("tidyverse")
library(tidyverse)

# read csv file 
players_15 <- read.csv("~/Project/fifa visualization/fifa/players_15.csv")
players_16 <- read.csv("~/Project/fifa visualization/fifa/players_16.csv")
players_17 <- read.csv("~/Project/fifa visualization/fifa/players_17.csv")
players_18 <- read.csv("~/Project/fifa visualization/fifa/players_18.csv")
players_19 <- read.csv("~/Project/fifa visualization/fifa/players_19.csv")
players_20 <- read.csv("~/Project/fifa visualization/fifa/players_20.csv")


# if you are wondering why Thiago was filtered using long_name, because of duplication of "Thiago" by different player
# there is no record of Kylian Mbappe in FIFA 2015
top_2015 <- players_15 %>% 
  filter(short_name == "L. Messi" | short_name == "Cristiano Ronaldo" | long_name == "Thiago Alcântara do Nascimento"
         | short_name == "K. De Bruyne" | short_name == "R. Lewandowski" | short_name == "S. Mané"
         | short_name == "Neymar" | short_name == "Sergio Ramos" | short_name == "M. Salah"
         | short_name == "V. van Dijk" | short_name == "K. Mbappé")

# there is no record of Kylian Mbappe and Virgil van Dijk in FIFA 2016
top_2016 <- players_16 %>% 
  filter(short_name == "L. Messi" | short_name == "Cristiano Ronaldo" | long_name == "Thiago Alcântara do Nascimento"
         | short_name == "K. De Bruyne" | short_name == "R. Lewandowski" | short_name == "S. Mané"
         | short_name == "Neymar" | short_name == "Sergio Ramos" | short_name == "M. Salah"
         | short_name == "V. van Dijk" | short_name == "K. Mbappé")

# there is no record of Kylian Mbappe in FIFA 2017
top_2017 <- players_17 %>% 
  filter(short_name == "L. Messi" | short_name == "Cristiano Ronaldo" | long_name == "Thiago Alcântara do Nascimento"
         | short_name == "K. De Bruyne" | short_name == "R. Lewandowski" | short_name == "S. Mané"
         | short_name == "Neymar" | short_name == "Sergio Ramos" | short_name == "M. Salah"
         | short_name == "V. van Dijk" | short_name == "K. Mbappé")

top_2018 <- players_18 %>% 
  filter(short_name == "L. Messi" | short_name == "Cristiano Ronaldo" | long_name == "Thiago Alcântara do Nascimento"
         | short_name == "K. De Bruyne" | short_name == "R. Lewandowski" | short_name == "S. Mané"
         | short_name == "Neymar" | short_name == "Sergio Ramos" | short_name == "M. Salah"
         | short_name == "V. van Dijk" | short_name == "K. Mbappé")

top_2019 <- players_19 %>% 
  filter(short_name == "L. Messi" | short_name == "Cristiano Ronaldo" | long_name == "Thiago Alcântara do Nascimento"
         | short_name == "K. De Bruyne" | short_name == "R. Lewandowski" | short_name == "S. Mané"
         | short_name == "Neymar Jr" | short_name == "Sergio Ramos" | short_name == "M. Salah"
         | short_name == "V. van Dijk" | short_name == "K. Mbappé")

top_2020 <- players_20 %>% 
  filter(short_name == "L. Messi" | short_name == "Cristiano Ronaldo" | long_name == "Thiago Alcântara do Nascimento"
         | short_name == "K. De Bruyne" | short_name == "R. Lewandowski" | short_name == "S. Mané"
         | short_name == "Neymar Jr" | short_name == "Sergio Ramos" | short_name == "M. Salah"
         | short_name == "V. van Dijk"| short_name == "K. Mbappé")

#add year column
top_2015$year <- 2015
top_2016$year <- 2016
top_2017$year <- 2017
top_2018$year <- 2018
top_2019$year <- 2019
top_2020$year <- 2020


