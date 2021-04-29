# weather API
Reports the current weather in various cities

## Instructions

### User Instructions

Users must create an API Token file, which must be stored in
the root directory, `token.cfg`, as such

```
[openweathermap]
token=--------------------------------
```

#### 1)	Explore the API documentation.

a.	Please note: The API is limited to 60 requests per minute.

b.	Token: `--------------------------------`

#### 2)	Use your preferred programming language to call the API to get the current weather
for 25 cities of your choice.

#### 3)	Generate a dataset with the following datapoints:

a.	City ID

b.	City name

c.	Datetime – convert from Unix timestamp to EST

d.	Weather description

e.	Current temperature

f.	Feels like temperature

#### 4)	Make sure the temperature is displayed in Fahrenheit.

5)	Do not explicitly call the API (“hard-code”) for each city. Make it dynamic.

6)	Store this information in a database of your choice.

a.	MSSQL, MySQL, MongoDB, DynamoDB, etc.
