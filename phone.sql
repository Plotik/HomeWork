1) Для создания таблицы из 4 полей + primary key 

CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, surname VARCHAR(50) Not NULL, name VARCHAR(50) Not NULL, phone VARCHAR(50) Not NULL, email TEXT);

2) Для добавления записей

INSERT INTO users (surname, name, phone, email) VALUES ('Plotnykov', 'Dima', '123123123', 'mail@mail.com');

3) Для проверки схемы таблицы
.schema users

4) Для обновления записей в таблице
UPDATE users SET surname = 'Plotik' WHERE id = 1 and name = 'Dima';

5) Для удаления данных в таблице
DELETE FROM users;

6) Для проверки списка пользователей в таблице
SELECT * FROM name;
* выводит все поля

SELECT * FROM users WHERE surname = 'Plotnykova';
