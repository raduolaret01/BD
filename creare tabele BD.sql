CREATE TABLE books (
    book_id INT(8) NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(127),
    PRIMARY KEY (book_id),
    CONSTRAINT author_check CHECK (author NOT LIKE '%[0-9]%')
);

CREATE TABLE users (
    user_id INT(8) NOT NULL AUTO_INCREMENT,
    username VARCHAR(32) UNIQUE NOT NULL,
    pass VARCHAR(16) NOT NULL,
    is_admin BOOL DEFAULT 0,
    PRIMARY KEY (user_id)
);

CREATE TABLE book_lendings (
    lend_id INT(8) NOT NULL AUTO_INCREMENT,
    book_id INT(8) NOT NULL,
    user_id INT(8) NOT NULL,
    lend_date DATE NOT NULL,
    return_date DATE NOT NULL,
    PRIMARY KEY (lend_id),
    CONSTRAINT book_fk FOREIGN KEY (book_id)
        REFERENCES books (book_id),
    CONSTRAINT user_fk FOREIGN KEY (user_id)
        REFERENCES users (user_id),
    CONSTRAINT date_order CHECK (lend_date <= return_date)
);