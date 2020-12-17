class StudentFileReader:
    """
    Implementation of the StudentFileReader ADT using a text file as the
    input source in which each field is stored on a separate line.
    """
    def __init__(self, input_src):
        """Create a new student reader instance."""
        self._input_src = input_src
        self._input_file = None

    def open(self):
        """Open a connection to the input file."""
        self._input_file = open(self._input_src, "r")

    def close(self):
        """Close the connection to the input file."""
        self._input_file.close()
        self._input_file = None

    def fetch_all(self):
        """Extract all student records and store them in a list."""
        records = list()
        student = self.fetch_record()
        while student is not None:
            records.append(student)
            student = self.fetch_record()
        return records

    def fetch_record(self):
        """Extract the next student record from the file."""
        line = self._input_file.readline()  # Read the first line of the record.
        if len(line) < 1:
            return None

        # If there is another record, create a storage object and fill it.

        student = StudentRecord()
        student.id_num = int(line.split(",")[0])
        student.first_name = line.split(",")[1].lstrip()
        student.last_name = line.split(",")[2].lstrip()

        if line.split(",")[3].lstrip() == "Freshman":
            student.class_code = 1
        elif line.split(",")[3].lstrip() == "Sophomore":
            student.class_code = 2
        elif line.split(",")[3].lstrip() == "Junior":
            student.class_code = 3
        elif line.split(",")[3].lstrip() == "Senior":
            student.class_code = 4
        else:
            student.class_code = 0

        # student.class_code = line.split(",")[3]
        student.gpa = float(line.split(",")[4].strip("\n"))

        return student


class StudentRecord:
    """Storage class used for an individual student record."""

    def __init__(self):
        self.id_num = 0
        self.first_name = None
        self.last_name = None
        self.class_code = 0
        self.gpa = 0.0
