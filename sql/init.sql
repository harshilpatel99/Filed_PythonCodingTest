CREATE DATABASE filed;

CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY '';
GRANT CREATE ON db.* TO 'root'@'%';
GRANT DELETE ON db.* TO 'root'@'%';
GRANT INSERT ON db.* TO 'root'@'%';
GRANT SELECT ON db.* TO 'root'@'%';
GRANT UPDATE ON db.* TO 'root'@'%';
