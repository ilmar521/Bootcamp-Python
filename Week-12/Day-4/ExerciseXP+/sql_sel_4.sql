select first_name, last_name from students
where birth_date >= TO_DATE('01/01/2000', 'DD/MM/YYYY')