import wtforms


def my_length_should_be_lower_than_4_check(form, field):
	if len(field.data) < 4:
		raise wtforms.ValidationError('The length of the filed should be at least 4 characters')


def my_own_length_validator(min_len, max_len):
	def validator(form, field):
		if not min_len < len(field.data) < max_len:
			raise wtforms.ValidationError(f'The length must be between {min_len} and {max_len}')

	return validator


class MyOwnLengthValidator:
	def __init__(self, min_len, max_len):
		self.min_len = min_len
		self.max_len = max_len

	def __call__(self, form, field):
		if not self.min_len < len(field.data) < self.max_len:
			raise wtforms.ValidationError(
				f'The length must be between {self.min_len} and {self.max_len} but you provided {len(field.data)}')
