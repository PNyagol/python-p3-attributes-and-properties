class Person:
    APPROVED_JOBS = {
        "Admin": 21,
        "Finance": 13,
        "Customer Service": 11,
        "Sales": 8,
        "Human Resources": 8,
        "General Management": 8,
        "ITC": 7,
        "Research and Development": 7,
        "Production": 6,
        "Marketing": 5,
        "Legal": 4,
        "Purchasing": 2
    }

    def __init__(self, name, job):
        self._name = name
        self._job = job

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) < 25:
            print(f"Setting name to {name}")
            self._name = name.title()
        else:
            print("Name must be a string under 25 characters.")

    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job in Person.APPROVED_JOBS:
            print(f"Setting job to {job}")
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)