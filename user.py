class User:
    def __init__(
            self, username, fullName,
            dob, gender, job,
            address, phNum, email, password
    ):
        self.username = username
        self.fullName = fullName
        self.dob = dob
        self.gender = gender
        self.job = job
        self.address = address
        self.phNum = phNum
        self.email = email
        self.password = password
        self.balance = 0.0


    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, value):
        self.username = value

    @property
    def fullName(self):
        return self.fullName

    @fullName.setter
    def fullName(self, value):
        self.fullName = value

    @property
    def dob(self):
        return self.dob

    @dob.setter
    def dob(self, value):
        self.dob = value

    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, value):
        self.gender = value

    @property
    def job(self):
        return self.job

    @job.setter
    def job(self, value):
        self.job = value

    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, value):
        self.address = value

    @property
    def phNum(self):
        return self.phNum

    @phNum.setter
    def phNum(self, value):
        self.phNum = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        self.email = value

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        self.password = value