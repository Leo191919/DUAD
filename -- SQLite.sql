-- SQLite
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    registration_date TEXT DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    entry_date TEXT DEFAULT CURRENT_TIMESTAMP,
    brand TEXT,
    stock_available INTEGER DEFAULT 0
    );

CREATE TABLE payment_methods ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type TEXT NOT NULL,
    bank_name TEXT
    );

CREATE TABLE invoices( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
    total_amount REAL NOT NULL, 
    user_id INTEGER,
    payment_method_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id)
    );

CREATE TABLE invoice_items ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER, 
    product_id INTEGER, 
    quantity INTEGER NOT NULL, 
    total_amount REAL NOT NULL, 
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
    );

CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
    );

CREATE TABLE reviews ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    user_id INTEGER,
    comment TEXT, 
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
    );

/*Limitations:SQLite does not support standart clauses like AUTO_INCREMENT or IDENTITY
  Solution:I solution used INTEGER PRIMARY KEY AUTOINCREMENT. In SQLite, INTEGER combined with PRIMARY KEY enables automatic rowid generation, while AUTOINCREMENT ensures that delete IDs are never reused.
  Limitations:SQLite lacks a dedicated native storage class for dates and times
  Solution:Mapped all timestamp fields to the text storage class and applied DEFAULT CURRENT_TIMESTAMP. Dates are stored in standard ISO 8601 format(YYYY-MM-DD HH>MM:SS).
  Limitation:SQLite relies on dynamic typing( Type Affinity) with only 5 primitive storage classes (NULL, INTEGER, REAL, TEXT, BLOB), rather than strict SQL column types like VARCHAR or FLOAT.
  Solution: Standardized the type to align with SQLite affinity: Converted VARCHAR and text attributes to TEXT. Converted FLOAT and monetary amounts to REAL.  Converted BIGINT and general quantities to INTEGER.
  Limitation:SQLite includes foreign key contraint syntax, but foreign key enforcement is disable by default for backward compatibility.
  Solution:Expressed all relationship  explicitly using FOREIGN KEY (...). Enforce them in runtime session by executing Pragma foreign_keys=ON;.*/
  
ALTER TABLE invoices ADD COLUMN boyer_phone TEXT;
ALTER TABLE invoices ADD COLUMN employee_code TEXT;


SELECT * FROM products;

SELECT * FROM products
WHERE price > 50000;


SELECT * FROM invoice_items
WHERE product_id = 1;

SELECT product_id,
    SUM(quantity) AS total_quantity_sold,
    SUM(total_amount) AS total_revenue)

FROM invoice_items
GROUP BY product_id;

SELECT * FROM invoices 
WHERE  user_id = 1;

SELECT * FROM invoices 
ORDER BY total_amount DESC;

SELECT * FROM invoices 
WHERE id = 1;


INSERT INTO users (full_name, email) VALUES ('Ana Gomez', 'ana@email.com'); 

INSERT INTO products (code, name, price, brand, stock_available)
VALUES ('PROD-001', 'Laptop Gamer', 75500.00, 'Asus', 10);

INSERT INTO payment_methods (method_type, bank_name) VALUES ( 'Credit Card', 'National Bank');

INSERT INTO invoices (total_amount, user_id, payment_method_id, buyer_phone, employee_code)
VALUES (75500.00, 1 ,1, '8888-9999', 'EMP-102');

INSERT INTO invoice_items (invoice_id, product_id, quantity, total_amount)
VALUES (1,1,1, 75500.00);


