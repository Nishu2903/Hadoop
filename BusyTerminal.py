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

    def reducer_light(self, terminal, counts):
        light_counts = filter(lambda x: x < 50, counts)
        light_count = sum(1 for _ in light_counts)
        yield terminal, light_count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_light)
        ]

if __name__ == '__main__':
    BusyTerminal.run()
