-- Lists the number of records with the same score
-- In the table second_table of the databse hbtn_0c_0
-- In your MySQL server.
SELECT score, COUNT(*) as number FROM second_table
GROUP BY score;
