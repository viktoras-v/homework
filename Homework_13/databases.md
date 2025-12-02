**1. Students database**

CREATE database test;

USE test;

CREATE table Students ( ID int, Name varchar(20), Age int );

INSERT into Students ( ID, Name, Age) values (1, 'Jonas', 78);

INSERT into Students ( ID, Name, Age) values (2, 'Antanas', 85);

SELECT * from Students;



**2. Comparison**

Main disadvantage of noSQL db is, that it can not run SQL queries! :)



**3.Library design**

CREATE database lib;

USE lib;

CREATE TABLE Authors (aID int, Name varchar(50) );

CREATE TABLE Patrons (pID int, Name varchar(50) );

CREATE TABLE Books ( bID int, Title varchar(50), Author varchar(50) );

CREATE TABLE Borrowed (ID int, pID int, bID int );



**4. Using Postgresql**

docker run --name some-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=admin -d postgres

psql -U postgres

CREATE DATABASE test;

\l

\c mydb

CREATE table Students ( ID int, Name varchar(20), Age int );

INSERT into Students ( ID, Name, Age) values (1, 'Jonas', 78);

select * from Students;

UPDATE Students SET age = 93 Where id = 1;

DROP TABLE Students;

\dt

\c postgres

DROP DATABASE mydb;

\l



**5. Slow queries.**

Suppose to take look into slow-queries.log or list running queries sorted by duration.

Interesting question.



**6. Library in MongoDB**

docker run --name mongodb -it mongodb/mongodb-community-server:8.0-ubi8

mongosh

use lib

db.createCollection("authors")

db.authors.insertOne({ pid: 1, name: "Jonas Biliunas" })

db.createCollection("patrons")

db.patrons.insertOne({ pid: 1, name: "Antantas" })

db.createCollection("books")

db.books.insertOne({ bid: 1, name: "Brisiaus galas" })

db.createCollection("borrowed")

db.borrowed.insertOne({ id: 1, pid: 1, bid: 1 })



show collections

db.patrons.find().pretty()













