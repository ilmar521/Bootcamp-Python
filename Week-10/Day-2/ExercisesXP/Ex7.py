from datetime import datetime

date_of_birth = datetime(1980, 5, 16)
differense = datetime.now() - date_of_birth
age_someone_seconds = differense.days * 86400 + differense.seconds
earth_year = 31557600
print(f"Age on Earth: {round(age_someone_seconds / earth_year, 2)}")
print(f"Age on Mercury: {round(age_someone_seconds / (earth_year * 0.2408467), 2)}")
print(f"Age on Venus: {round(age_someone_seconds / (earth_year * 0.61519726), 2)}")
print(f"Age on Mars: {round(age_someone_seconds / (earth_year * 1.8808158), 2)}")
print(f"Age on Jupiter: {round(age_someone_seconds / (earth_year * 11.862615), 2)}")
print(f"Age on Saturn: {round(age_someone_seconds / (earth_year * 29.447498), 2)}")
print(f"Age on Uranus: {round(age_someone_seconds / (earth_year * 84.016846), 2)}")
print(f"Age on Neptune: {round(age_someone_seconds / (earth_year * 164.79132), 2)}")