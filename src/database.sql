-- Create a database
CREATE DATABASE IF NOT EXISTS MovieDatabase;

-- Use the created database
USE MovieDatabase;

-- Create a table for movies
CREATE TABLE IF NOT EXISTS Movies (
    MovieID INT PRIMARY KEY,
    MovieName VARCHAR(255) NOT NULL,
    ActorNames JSON,
    ActorImages JSON,
    OtherAnswers JSON,
    Hints JSON,
    QuizDate DATE NOT NULL
);
