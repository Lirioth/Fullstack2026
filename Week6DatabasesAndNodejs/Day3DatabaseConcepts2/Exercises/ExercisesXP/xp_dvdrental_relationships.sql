-- =============================================================
-- 📚 Exercises XP — dvdrental Relationships & Queries (PostgreSQL)
-- =============================================================

/* -------------------------------------------------------------
   🌟 Exercise 1: DVD Rental
------------------------------------------------------------- */

-- 1) Get a list of all the languages
SELECT language_id, name, last_update
FROM language
ORDER BY name;

-- 2) All films joined with their languages: title, description, language name
SELECT f.film_id, f.title, f.description, l.name AS language_name
FROM film AS f
JOIN language AS l ON l.language_id = f.language_id
ORDER BY f.title;

-- 3) Get all languages even if there are no films in those languages
--    LEFT JOIN from language → film
SELECT l.language_id, l.name AS language_name, f.title, f.description
FROM language AS l
LEFT JOIN film AS f ON f.language_id = l.language_id
ORDER BY l.name, f.title;

-- 4) Create table new_film(id, name) and add a few films
DROP TABLE IF EXISTS new_film;
CREATE TABLE new_film (
  id   SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

INSERT INTO new_film(name) VALUES
  ('SUMO SPIRIT'),
  ('RIVER BOAT RIDDLE'),
  ('DOCU HOUR');

-- 5) Create table customer_review with ON DELETE CASCADE to new_film
DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review (
  review_id   SERIAL PRIMARY KEY,
  film_id     INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE,
  language_id INTEGER NOT NULL REFERENCES language(language_id),
  title       TEXT    NOT NULL,
  score       INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
  review_text TEXT,
  last_update TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Add 2 reviews linked to valid new_film + language rows
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
  ((SELECT id FROM new_film WHERE name = 'SUMO SPIRIT'),
   (SELECT language_id FROM language WHERE name = 'English'),
   'Wrestling Wisdom', 8, 'Fun and surprisingly thoughtful.'),
  ((SELECT id FROM new_film WHERE name = 'RIVER BOAT RIDDLE'),
   (SELECT language_id FROM language WHERE name = 'English'),
   'Wet Mystery', 7, 'Puzzly and atmospheric.');

-- Verify reviews
SELECT * FROM customer_review ORDER BY review_id;

-- 6) Delete a film that has a review and observe cascade
DELETE FROM new_film WHERE name = 'RIVER BOAT RIDDLE';

-- After deletion, reviews for that film should be gone automatically
SELECT * FROM customer_review ORDER BY review_id;


/* -------------------------------------------------------------
   🌟 Exercise 2: DVD Rental (more queries)
------------------------------------------------------------- */

-- 1) UPDATE language of some films (must be a valid language id)
-- Example: set ACADEMY DINOSAUR to German
UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'German')
WHERE title = 'ACADEMY DINOSAUR';

-- Verify
SELECT title, language_id FROM film WHERE title = 'ACADEMY DINOSAUR';

-- 2) Which foreign keys are defined for the customer table?
--    (Store and Address FKs in the stock dataset)
SELECT conname AS constraint_name,
       pg_get_constraintdef(c.oid) AS definition
FROM   pg_constraint AS c
WHERE  c.conrelid = 'customer'::regclass
  AND  c.contype = 'f';

--    Effect on INSERT: store_id and address_id must reference existing rows.
--    Example skeleton (WILL FAIL if address_id/store_id missing):
-- INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date)
-- VALUES (1, 'Test', 'User', 'test@example.com', 1, TRUE, NOW());

-- 3) Drop the customer_review table (easy: nothing depends on it)
DROP TABLE IF EXISTS customer_review;

-- 4) How many rentals are outstanding (not yet returned)?
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- 5) 30 most expensive outstanding movies (by replacement_cost)
SELECT f.film_id, f.title, f.replacement_cost
FROM rental AS r
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film     AS f ON f.film_id      = i.film_id
WHERE r.return_date IS NULL
GROUP BY f.film_id, f.title, f.replacement_cost
ORDER BY f.replacement_cost DESC, f.title
LIMIT 30;

-- 6) Help a friend find 4 films

-- 6.1 Sumo wrestler topic AND actor Penelope Monroe
SELECT DISTINCT f.film_id, f.title
FROM film AS f
JOIN film_actor AS fa ON fa.film_id = f.film_id
JOIN actor      AS a  ON a.actor_id = fa.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
  AND (f.description ILIKE '%sumo%' OR f.title ILIKE '%sumo%');

-- 6.2 Short documentary (< 60 minutes) rated R
SELECT f.film_id, f.title
FROM film AS f
JOIN film_category AS fc ON fc.film_id = f.film_id
JOIN category      AS c  ON c.category_id = fc.category_id
WHERE c.name = 'Documentary'
  AND f.length < 60
  AND f.rating = 'R';

-- 6.3 Film that Matthew Mahan rented, paid > 4.00, returned between 2005-07-28 and 2005-08-01
SELECT DISTINCT f.film_id, f.title
FROM customer AS cu
JOIN rental   AS r  ON r.customer_id = cu.customer_id
JOIN payment  AS p  ON p.customer_id = cu.customer_id AND p.rental_id = r.rental_id
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film      AS f ON f.film_id      = i.film_id
WHERE cu.first_name = 'Matthew' AND cu.last_name = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date >= DATE '2005-07-28' AND r.return_date < DATE '2005-08-02';

-- 6.4 Film Matthew Mahan watched, with "boat" in title or description, expensive to replace
--     "Very expensive" threshold chosen as >= 25.00 (dataset max is ~29.99)
SELECT DISTINCT f.film_id, f.title, f.replacement_cost
FROM customer AS cu
JOIN rental   AS r  ON r.customer_id = cu.customer_id
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film      AS f ON f.film_id      = i.film_id
WHERE cu.first_name = 'Matthew' AND cu.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
  AND f.replacement_cost >= 25.00
ORDER BY f.replacement_cost DESC, f.title;

-- End of file ✅
