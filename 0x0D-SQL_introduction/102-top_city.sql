-- task 20
-- get the top 3 cities in temperatures from jul to aug
SELECT city, AVG(value) as avg_temp
	FROM temperatures
	WHERE month BETWEEN 7 AND 8
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
