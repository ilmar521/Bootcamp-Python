-- Find out how many films there are for each rating.
-- select rating, count(1) from film group by rating


-- Get a list of all the movies that have a rating of G or PG-13.
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
-- select * from film
-- where
-- 	(rating = 'G' or rating = 'PG-13')
-- 	and length < 120
-- 	and rental_rate < 3 
-- order by 
-- 	title asc


-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
-- update customer
-- set first_name = 'Kirill', last_name = 'Lunev'
-- where customer_id = 1


-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address a
SET address = 'Nof haGalil'
FROM customer c 
	where c.customer_id = 1 and c.address_id = a.address_id  

