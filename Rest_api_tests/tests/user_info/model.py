from faker import Faker


fake = Faker()

class RegisterUser:
    @staticmethod
    def random():
        USERNAME = fake.email()
        PASSWORD = fake.password()
        return {"username": USERNAME, "password": PASSWORD}

class AddUserInfo:
    @staticmethod
    def random_user_info(self):
      address = Address(
                city=fake.city(),
                street=fake.street_name(),
                home_number=fake.building_number(),
            )
      return AddUserInfo(
                phone=fake.phone_number(), email=fake.email(), address=address
            )

class Store:
    @staticmethod
    def add_random_store(self):
      return Store(name=fake.first_name())
