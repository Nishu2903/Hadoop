from mrjob.job import MRJob
from mrjob.step import MRStep

class BusyTerminal(MRJob):

    def mapper(self, _, line):
        # Split the line into fields
        fields = line.strip().split(',')

        # Extract the Terminal and Passenger Count fields
        terminal = fields[1]
        passenger_count = int(fields[3])

        # Emit a key-value pair with the Terminal as the key and the Passenger Count as the value
        yield terminal, passenger_count

    def reducer(self, terminal, counts):
        # Sum up the counts for each Terminal
        total_count = sum(counts)

        # Emit a key-value pair with the Terminal as the key and the total count as the value
        yield terminal, total_count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)        ]

if __name__ == '__main__':
    BusyTerminal.run()
