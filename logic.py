from mrjob.job import MRJob
from mrjob.step import MRStep

class BusyTerminal(MRJob):

    def mapper(self, _, line):
        fields = line.strip().split(',')

        terminal = fields[1]
        passenger_count = int(fields[3])

        yield terminal, passenger_count

    def reducer(self, terminal, counts):
        total_count = sum(counts)

        yield terminal, total_count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)        ]

if __name__ == '__main__':
    BusyTerminal.run()
