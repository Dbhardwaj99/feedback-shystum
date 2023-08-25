CREATE DATABASE feedback;

USE feedback;

CREATE TABLE teacher(
    subject_id INT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO teacher (subject_id, email, password) VALUES (2, 't1', '1');


CREATE TABLE student(
    reg_no INT NOT NULL UNIQUE PRIMARY KEY
);

-- insert multiple registeration number into student (reg_no)
INSERT INTO student (reg_no) VALUES (406), (251), (432), (354), (696), (420), (111);

CREATE TABLE class_feedback(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    subject_id INT NOT NULL,
    reg_no INT NOT NULL UNIQUE,
    q1 INT NOT NULL CHECK (q1 BETWEEN 1 AND 5),
    q2 INT NOT NULL CHECK (q2 BETWEEN 1 AND 5),
    q3 INT NOT NULL CHECK (q3 BETWEEN 1 AND 5),
    q4 INT NOT NULL CHECK (q4 BETWEEN 1 AND 5),
    q5 INT NOT NULL CHECK (q5 BETWEEN 1 AND 5)
    -- FOREIGN KEY (reg_no) REFERENCES student(reg_no),
    -- FOREIGN KEY (subject_id) REFERENCES teacher(subject_id)
);

CREATE TABLE subject_feedback(
    subject_id INT NOT NULL  PRIMARY KEY,
    q1 INT NOT NULL CHECK (q1 BETWEEN 1 AND 5),
    q2 INT NOT NULL CHECK (q2 BETWEEN 1 AND 5),
    q3 INT NOT NULL CHECK (q3 BETWEEN 1 AND 5),
    q4 INT NOT NULL CHECK (q4 BETWEEN 1 AND 5),
    q5 INT NOT NULL CHECK (q5 BETWEEN 1 AND 5)
    -- FOREIGN KEY (subject_id) REFERENCES teacher(subject_id)
);

CREATE TABLE weekly_feedback(
    subject_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    q1 INT NOT NULL CHECK (q1 BETWEEN 1 AND 5),
    q2 INT NOT NULL CHECK (q2 BETWEEN 1 AND 5),
    q3 INT NOT NULL CHECK (q3 BETWEEN 1 AND 5),
    q4 INT NOT NULL CHECK (q4 BETWEEN 1 AND 5),
    q5 INT NOT NULL CHECK (q5 BETWEEN 1 AND 5)
    -- FOREIGN KEY (subject_id) REFERENCES teacher(subject_id)
);

