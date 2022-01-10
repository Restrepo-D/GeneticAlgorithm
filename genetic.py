import random


class Genetic():
    def __init__(self, target='hello world', population_size=100, parent_pool=.33):
        """ Class that implements genetic algorithm to find a target string.

        Args:
            target (str, optional): Target string to find. Defaults to 'hello world'.
            population_size (int, optional): Individuals in each iteration. Defaults to 100.
            parent_pool (float, optional): Percent of population to use in breeding process. Defaults to .33.
        """
        self.target = target
        self.genes = [chr(i) for i in range(32, 123)]
        self.population_size = population_size
        self.parent_pool = parent_pool
        self.population = [''.join([random.choice(self.genes) for _ in range(
            len(self.target))]) for _ in range(population_size)]
        self.population = sorted([(individual, self.calc_fitness(
            individual)) for individual in self.population], key=lambda x: x[1], reverse=True)

    def calc_fitness(self, individual):
        """ Helper to find fitness of an individual.

        Args:
            individual ([type]): Individual to score.

        Returns:
            int: Number of shared genes.
        """
        score = 0
        for c1, c2 in zip(self.target, individual):
            if c1 == c2:
                score += 1
        return score

    def breed(self, mother, father):
        """ Breeds two individuals.

        Args:
            mother (str): Mother gene pool.
            father (str): Father gene pool.

        Returns:
            str: Child.
        """

        child = ''
        for gene1, gene2 in zip(mother, father):
            rand = random.uniform(0, 1)
            if rand < .45:
                child += gene1
            elif .45 < rand < .9:
                child += gene2
            elif .9 < rand:
                child += random.choice(self.genes)
        return child

    def iterate(self):
        """ Steps forward a generation.

        Returns:
            (str, int): strongest individual from population.
        """
        # Get parents.
        parents = self.population[:round(
            len(self.population)*self.parent_pool)]

        # Breed.
        self.population = [self.breed(random.choice(parents)[0], random.choice(
            parents)[0]) for _ in range(self.population_size)]

        # Score and maintain sort.
        self.population = sorted([(individual, self.calc_fitness(
            individual)) for individual in self.population], key=lambda x: x[1], reverse=True)

        # Return
        return self.population[0]

    def evolve(self):
        """ Progresses population until target sequence is reached. Prints highest 
        scoring individual of each generation.
        """
        generation = 0
        strongest = self.population[0]
        print(f"Generation {generation}: {strongest}")
        while len(self.target) != strongest[1]:
            strongest = self.iterate()
            generation += 1
            print(f"Generation {generation}: {strongest}")


if __name__ == '__main__':
    g = Genetic(target='To be, or not to be: that is the question',
                population_size=1000, parent_pool=.1)
    g.evolve()
