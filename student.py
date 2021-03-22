from web import errors


class Student:
    def __init__(self,  id: int, full_name: str, rating: float,
                 age: int, photo_link: str, speciality: str,
                 group: str, sex: str, fav_colour: str, email: str):
        self.full_name = self.set_full_name(full_name)
        self.rating = rating
        self.age = self.set_age(age)
        self.photo = photo_link
        self.speciality = speciality
        self.group = group
        self.sex = sex
        self.email = email
        self.favourite_colour = fav_colour
        self.id = id

    def __repr__(self):
        return f"'{self.full_name}', {self.rating}, {self.age}, '{self.photo}', '{self.speciality}'," \
               f" '{self.group}', '{self.sex}', '{self.favourite_colour}', '{self.email}'"

    def properties_list(self):
        return [self.id, self.full_name, self.rating, self.age,
                self.photo, self.speciality, self.group,
                self.sex, self.favourite_colour]

    @staticmethod
    def set_full_name(name: str):
        """Checks if name contains first, middle and last names"""
        if len(name.split(" ")) < 3:
            raise errors.NotFullNameException("Please enter your "
                                              "full name including your first, middle and last names")
        return name

    @staticmethod
    def set_age(age: int):
        """Checks if the age is a decent value
        i.e. positive integer greater than 17"""
        if not isinstance(age, int):
            raise errors.InvalidStudentAge("Age must be an integer")
        elif age <= 0:
            raise errors.InvalidStudentAge("Age must be a positive integer")
        elif age < 18:
            raise errors.InvalidStudentAge("Constructed student is too young")
        return age
