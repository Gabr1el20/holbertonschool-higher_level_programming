-- Creates the database hbtn_0d_2 and the user user_0d_2.
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
ALTER USER IF EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE, SELECT ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
