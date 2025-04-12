APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Admin"):
        self._name = None
        self._job = None

        valid_name = isinstance(name, str) and 1 <= len(name) <= 25
        valid_job = job in APPROVED_JOBS

        if not valid_name:
            print("Name must be string between 1 and 25 characters.")
        if not valid_job:
            print("Job must be in list of approved jobs.")

        if valid_name and valid_job:
            self.name = name
            self.job = job

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        self._name = name.title()
        print(f"Setting name to {self._name}")

    name = property(get_name, set_name)

    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        self._job = job
        print(f"Setting job to {self._job}")

    job = property(get_job, set_job)
