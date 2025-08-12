-- TABLES --

CREATE TABLE Categorie (
	Id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(255),
	flag ENUM('private', 'public'),
)

CREATE TABLE Product (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	price DECIMAL(10, 2),
	create_at DATE NOT NULL,
)

CREATE TABLE ProductCategorie (
	product_id INT NOT NULL,
	categorie_id INT NOT NULL,
	PRIMARY KEY (product_id, categorie_id),
	FOREIGN KEY (product_id) REFERENCES Product(id),
	FOREIGN KEY (categorie_id) REFERENCES Categorie(id),
)


-- Query --
SELECT p.id, p.name, p.price, p.create_at
FROM Product p
JOIN ProductCategorie pc ON p.id = pc.product_id
JOIN Categorie c ON pc.categorie_id = c.id
WHERE c.flag = 'public'
GROUP BY p.id, p.name, p.price, p.create_at
HAVING COUNT(DISTINC c.id) >= 5;