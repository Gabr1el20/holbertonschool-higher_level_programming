-- Lists all the cities of California
-- That can be found in the db hbtn_0d_usa.
SELECT id, name FROM cities
WHERE state_id = (SELECT id from states WHERE name = 'California')
ORDER BY cities.id ASC;
