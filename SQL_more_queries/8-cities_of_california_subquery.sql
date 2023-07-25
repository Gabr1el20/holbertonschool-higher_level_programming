-- Lists all the cities of California
-- That can be found in the db hbtn_0d_usa.
SELECT id, name FROM cities
-- Subquery for get the id of the state.
    WHERE state_id = (SELECT id from states WHERE name = "California")
    ORDER BY id;
