import datetime

def sign(date):
	if date == "":
		return "Couldn't get Zodaic Sign. No DOB"
	new_date = datetime.datetime.strptime(date, "%Y-%m-%d")
	month = int(new_date.strftime("%m"))
	day = int(new_date.strftime("%d"))
	sign =""

	if month == 12:
		if (day < 22):
			sign = 'Sagittarius'
		else:
			sign = 'Capricorn'
	elif month == 1:
		if (day < 20):
			sign = 'Capricorn'
		else:
			sign = 'Aquarius'
	elif month == 2:
		if (day < 19):
			sign = 'Aquarius'
		else:
			sign = 'Pisces'
	elif month == 3:
		if (day < 21):
			sign = 'Pisces'
		else:
			sign = 'Aries'
	elif month == 4:
		if (day < 20):
			sign = 'Aries'
		else:
			sign = 'Taurus'
	elif month == 5:
		if (day < 21):
			sign = 'Taurus'
		else:
			sign = 'Gemini'
	elif month == 6:
		if (day < 21):
			sign = 'Gemini'
		else:
			sign = 'Cancer'
	elif month == 7:
		if (day < 23):
			sign = 'Cancer'
		else:
			sign = 'Leo'
	elif month == 8:
		if (day < 23):
			sign = 'Leo'
		else:
			sign = 'Virgo'
	elif month == 9:
		if (day < 23):
			sign = 'Virgo'
		else:
			sign = 'Libra'
	elif month == 10:
		if (day < 23):
			sign = 'Libra'
		else:
			sign = 'Scorpio'
	elif month == 11:
		if (day < 22):
			sign = 'Scorpio'
		else:
			sign = 'Sagittarius'
	return sign


if __name__ == '__main__':
    assert sign("") == "Couldn't get Zodaic Sign. No DOB"
    assert sign(str(datetime.date(2020, 1, 20))) == "Aquarius"
    assert sign(str(datetime.date(2020, 2, 19))) == "Pisces"
    assert sign(str(datetime.date(2020, 3, 22))) == "Aries"
    assert sign(str(datetime.date(2020, 4, 21))) == "Taurus"
    assert sign(str(datetime.date(2020, 5, 21))) == "Gemini"
    assert sign(str(datetime.date(2020, 6, 22))) == "Cancer"
    assert sign(str(datetime.date(2020, 7, 27))) == "Leo"
    assert sign(str(datetime.date(2020, 8, 24))) == "Virgo"
    assert sign(str(datetime.date(2020, 9, 25))) == "Libra"
    assert sign(str(datetime.date(2020, 10, 29))) == "Scorpio"
    assert sign(str(datetime.date(2020, 11, 30))) == "Sagittarius"
    assert sign(str(datetime.date(2020, 12, 25))) == "Capricorn"

