-- Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test with password hbnb_test_pwd in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.
-- Connect to the MySQL server as root (adjust the credentials if need
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO hbnb_test@localhost;
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema . * TO hbnb_test@localhost;