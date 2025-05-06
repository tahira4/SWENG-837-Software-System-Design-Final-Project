-- database_schema.sql

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(20) -- Student, Tutor, Faculty
);

CREATE TABLE Sessions (
    session_id INT PRIMARY KEY,
    student_id INT,
    tutor_id INT,
    session_time DATETIME,
    status VARCHAR(20), -- scheduled, in_progress, completed, canceled
    FOREIGN KEY (student_id) REFERENCES Users(user_id),
    FOREIGN KEY (tutor_id) REFERENCES Users(user_id)
);

CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY,
    session_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (session_id) REFERENCES Sessions(session_id)
);
