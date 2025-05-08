import readline

class StadiumSeating:
    def __init__(self, n, rows, cols, seating):
        self.n = n  # Minimum adjacent empty seats required
        self.rows = rows  # Number of rows in the seating arrangement
        self.cols = cols  # Number of columns
        self.seating = seating  # 2D seating matrix


    def count_adjacent_seats(self):
        """Count horizontal groups of N adjacent empty seats."""
        total_count = 0
        for row in self.seating:
            empty_seats = 0
            for seat in row:
                if seat == 0:
                    empty_seats += 1
                else:
                    if empty_seats >= self.n:
                        total_count += (empty_seats - self.n + 1)
                    empty_seats = 0
            if empty_seats >= self.n:
                total_count += (empty_seats - self.n + 1)
        return total_count

    @classmethod
    def from_file(cls, filename):
        """Reads input from a file and creates an instance of StadiumSeating."""
        with open(filename, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]  # Remove empty lines

        # Ensure the file has enough data
        if len(lines) < 2:
            raise ValueError("Input file does not contain enough data.")

        try:
            n = int(lines[0])  # Minimum adjacent empty seats required
            rows, cols = map(int, lines[1].split())  # Matrix dimensions
        except ValueError:
            raise ValueError("Error reading 'n', 'rows', or 'cols'. Check the input file format.")

        # Ensure the matrix has enough rows
        if len(lines[2:]) != rows:
            raise ValueError(f"Expected {rows} rows in the seating matrix but got {len(lines) - 2}.")

        # Read the seating matrix
        seating = []
        for line in lines[2:]:
            row_data = list(map(int, line.split()))
            if len(row_data) != cols:
                raise ValueError(f"Each row must have {cols} columns, but got {len(row_data)}.")
            seating.append(row_data)

        return cls(n, rows, cols, seating)  # Create an instance of the class

    def get_total_seat_count(self):
        """Calls the function and returns the result."""
        return self.count_adjacent_seats()

# Create an object using input from a file (Replace 'input.txt' with your filename)
filename = "text.txt"
stadium = StadiumSeating.from_file(filename)

# Calculating and printing the result
print(stadium.get_total_seat_count())



