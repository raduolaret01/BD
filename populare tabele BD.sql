insert into books
	(title, author, genre)
values
	("Red Mars ", "Kim Stanley Robinson", "Sci-Fi"),
    ("Green Mars", "Kim Stanley Robinson", "Sci-Fi"),
    ("Blue Mars", "Kim Stanley Robinson", "Sci-Fi"),
    ("Ciresarii Vol 1", "Constantin Chirita", "Fiction"),
    ("Ciresarii Vol 2", "Constantin Chirita", "Fiction"),
    ("Ciresarii Vol 3", "Constantin Chirita", "Fiction"),
    ("Ciresarii Vol 4", "Constantin Chirita", "Fiction"),
    ("Ciresarii Vol 5", "Constantin Chirita", "Fiction");
    
insert into users
	(username, pass, is_admin)
values
	("admin", "admin", 1),
    ("john", "john", 0),
    ("timmy", "timmy", 0),
    ("bibli0tec4rul22", "parola", 0),
    ("popescu", "1968", 0);
    
insert into book_lendings
	(user_id, book_id, lend_date, return_date)
values
	(2, 1, '2023-01-01', '2023-03-01'),
	(2, 2, '2023-03-01', '2023-05-01'),
	(3, 4, '2022-12-15', '2023-01-30'),
	(3, 6, '2023-02-15', '2023-03-30'),
	(4, 3, '2022-10-15', '2023-02-15'),
	(5, 5, '2022-01-15', '2024-01-30')