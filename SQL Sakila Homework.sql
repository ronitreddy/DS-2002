
-- Query #1: List of Actors in a Specific Film
SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

-- Query #2: Count of Films in Each Category
SELECT c.name AS CategoryName, COUNT(fc.film_id) AS FilmCount
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY CategoryName;

-- Query #3: Average Rental Duration for Each Rating
SELECT rating, AVG(rental_duration) AS AverageRentalDuration
FROM film
GROUP BY rating
ORDER BY rating;

-- Query #4: Total Number of Rentals for Each Customer
SELECT c.first_name, c.last_name, COUNT(r.rental_id) AS TotalRentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.last_name, c.first_name;

-- Query #5: Stores with the Highest Number of Rentals
SELECT i.store_id, COUNT(r.rental_id) AS TotalRentals
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
GROUP BY i.store_id
ORDER BY TotalRentals DESC
LIMIT 1;

-- Query #6: Most Popular Film Category Among Customers
SELECT c.name AS CategoryName, COUNT(r.rental_id) AS RentalCount
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film_category fc ON i.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.category_id, c.name
ORDER BY RentalCount DESC
LIMIT 1;

-- Query #7: Average Rental Cost of Films by Category
SELECT c.name AS CategoryName, AVG(f.rental_rate) AS AverageRentalRate
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.category_id, c.name
ORDER BY CategoryName;

-- Query #8: List of Films Not Rented in the Last Month
SELECT f.title, lr.LastRentalDate
FROM film f
LEFT JOIN (
    SELECT i.film_id, MAX(r.rental_date) AS LastRentalDate
    FROM inventory i
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY i.film_id
) lr ON f.film_id = lr.film_id
WHERE lr.LastRentalDate IS NULL OR lr.LastRentalDate < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
ORDER BY f.title;

-- Query #9: Customer Spending on Rentals
SELECT c.first_name, c.last_name, SUM(p.amount) AS TotalSpending
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.last_name, c.first_name;

-- Query #10: Average Length of Films in Each Language
SELECT lang.name AS Language, AVG(f.length) AS AverageLength
FROM film f
JOIN language lang ON f.language_id = lang.language_id
GROUP BY lang.language_id, lang.name
ORDER BY lang.name;
