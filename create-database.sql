CREATE DATABASE nftBack_end;
CREATE DATABASE nftApp_user;

CREATE USER nftBack_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE nftBack_end TO nftBack_admin;