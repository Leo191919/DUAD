-- SQLite
PRAGMA foreign_keys=ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    registration_date TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT  UNIQUE NOT NULL, 
    description TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    entry_date TEXT DEFAULT CURRENT_TIMESTAMP,
    brand TEXT,
    category_id INTEGER NOT NULL,
    stock_available INTEGER DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(id)
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
    user_id INTEGER NOT NULL,
    payment_method_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id)
);

CREATE TABLE invoice_items ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL, 
    product_id INTEGER NOT NULL, 
    quantity INTEGER NOT NULL, 
    total_amount REAL NOT NULL, 
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
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
  
ALTER TABLE invoices ADD COLUMN buyer_phone TEXT;
ALTER TABLE invoices ADD COLUMN employee_code TEXT;

INSERT INTO categories ( name, description ) VALUES 
('Computers', 'Laptops, Desktops and Accessories'), 
('Smartphones', 'Inteligent phones and mobile devices'),
('Accesories', 'Peripherals, cables, chargers and other accessories');



INSERT INTO users (full_name, email) VALUES ('Ana Gomez', 'ana@email.com'); 
INSERT INTO payment_methods (method_type, bank_name) VALUES ( 'Credit Card', 'National Bank');


INSERT INTO products (code, product_name, price, brand,category_id, stock_available)
VALUES ('PROD-001', 'Laptop Gamer', 75500.00, 'Asus', 1, 10);

INSERT INTO invoices (total_amount, user_id, payment_method_id, buyer_phone, employee_code)
VALUES (75500.00, 1 ,1, '8888-9999', 'EMP-102');

INSERT INTO invoice_items (invoice_id, product_id, quantity, total_amount)
VALUES (1,1,1, 75500.00);

INSERT INTO products (code, product_name, price, brand, category_id, stock_available) VALUES
    ('PROD-002', 'Apple iPhone 15', 420000.00, 'Apple', 2, 8),
    ('PROD-003', 'Apple MacBook Air  M3', 680000.00, 'Apple', 1, 5),
    ('PROD-004', 'Wireless Mouse', 12500.00, 'Logitech', 3, 25),
    ('PROD-005', 'Keyboard Mechanical', 38000.00, 'Keychron', 3, 7),
    ('PROD-006', '27-inch Monitor', 145000.00, 'Dell', 1, 12), 
    ('PROD-007', 'Apple AirPods Pro', 135000.00, 'Apple', 3, 15), 
    ('PROD-008', 'Fast USB-C Charger', 9500.00, 'Anker', 3,15),
    ('PROD-009', 'Samsung Galaxy S24', 395000.00, 'Samsung', 2, 9),
    ('PROD-010', 'Cooling Base', 18000.00,'CoolerMaster', 3, 6),
    ('PROD-011', 'Certified HDMI Cable', 0.00, 'Ugreen', 3, 14);

UPDATE products SET category_id = 1 WHERE id = 1;
UPDATE products SET category_id = 2 WHERE code = 'PROD-002';
UPDATE products SET category_id = 3 WHERE code = 'PROD-004';


SELECT id, product_name, price, category_id, stock_available FROM products;

SELECT * FROM products;

SELECT * FROM products
WHERE price > 50000;

SELECT * FROM products
WHERE product_name LIKE '%apple%';

SELECT * FROM products 
ORDER BY price DESC
LIMIT 5;


UPDATE products
SET stock_available = 0 
WHERE price <= 0 ;

UPDATE products 
SET price = price + 100
WHERE stock_available < 10; 


UPDATE products
SET stock_available  = stock_available - 1 
WHERE id =1; 

SELECT * FROM products 
ORDER BY id ASC
LIMIT 10; 


SELECT * FROM invoice_items
WHERE product_id = 1;

SELECT product_id,
    SUM(quantity) AS total_quantity_sold,
    SUM(total_amount) AS total_revenue

FROM invoice_items
GROUP BY product_id;

SELECT * FROM invoices 
WHERE  user_id = 1;

SELECT * FROM invoices 
ORDER BY total_amount DESC;

SELECT * FROM invoices 
WHERE id = 1;
