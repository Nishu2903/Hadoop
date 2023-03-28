from mrjob.job import MRJob

class BusyTerminal(MRJob):

    def mapper(self, _, line):
        # Split the line into fields
        fields = line.strip().split(',')

        # Extract the Terminal and Passenger Count fields
        terminal = fields[2]
        passenger_count = int(fields[3])

        # Emit a key-value pair with the Terminal as the key and the Passenger Count as the value
        yield terminal, passenger_count

    def reducer(self, terminal, counts):
        # Sum up the counts for each Terminal
        total_count = sum(counts)

        # Emit a key-value pair with the Terminal as the key and the total count as the value
        yield terminal, total_count

    def mapper_light(self, terminal, count):
        # Check if the flight has a "light" designation
        if count < 50:
            # Emit a key-value pair with the Terminal as the key and a count of 1 as the value
            yield terminal, 1

    def reducer_light(self, terminal, counts):
        # Count the number of "light" flights for each Terminal
        light_count = sum(counts)

        # Emit a key-value pair with the Terminal as the key and the number of "light" flights as the value
        yield terminal, light_count

    def steps(self):
        return [
            self.mr(mapper=self.mapper, reducer=self.reducer),
            self.mr(mapper=self.mapper_light, reducer=self.reducer_light)
        ]

if __name__ == '__main__':
    BusyTerminal.run()
