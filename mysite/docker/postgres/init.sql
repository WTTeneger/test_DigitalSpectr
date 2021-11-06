CREATE USER admin WITH PASSWORD 'devpass';

CREATE database prod_db;
GRANT ALL PRIVILEGES ON DATABASE prod_db TO admin;