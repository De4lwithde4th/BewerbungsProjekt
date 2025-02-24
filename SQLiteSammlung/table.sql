CREATE TABLE kunden (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    land TEXT,
    registrierungsdatum DATE
);

CREATE TABLE produkte (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    preis REAL NOT NULL
);

CREATE TABLE bestellungen (
    id INTEGER PRIMARY KEY,
    kunden_id INTEGER,
    produkt_id INTEGER,
    menge INTEGER,
    bestelldatum DATE,
    FOREIGN KEY (kunden_id) REFERENCES kunden(id),
    FOREIGN KEY (produkt_id) REFERENCES produkte(id)
);

INSERT INTO kunden (id, name, land, registrierungsdatum) VALUES (1, 'Alice', 'Deutschland', '2022-05-01');
INSERT INTO kunden (id, name, land, registrierungsdatum) VALUES (2, 'Bob', 'Österreich', '2021-07-15');
INSERT INTO kunden (id, name, land, registrierungsdatum) VALUES (3, 'Charlie', 'Schweiz', '2020-11-23');

INSERT INTO produkte (id, name, preis) VALUES (1, 'Laptop', 1200.00);
INSERT INTO produkte (id, name, preis) VALUES (2, 'Maus', 25.50);
INSERT INTO produkte (id, name, preis) VALUES (3, 'Tastatur', 45.99);

INSERT INTO bestellungen (id, kunden_id, produkt_id, menge, bestelldatum) VALUES (1, 1, 1, 1, '2023-02-10');
INSERT INTO bestellungen (id, kunden_id, produkt_id, menge, bestelldatum) VALUES (2, 2, 2, 3, '2023-02-12');
INSERT INTO bestellungen (id, kunden_id, produkt_id, menge, bestelldatum) VALUES (3, 3, 3, 2, '2023-02-15');

