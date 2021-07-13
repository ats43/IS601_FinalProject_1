import statistics
import unittest
from src.Statistics.Statistics import Statistics
import random
from src.HelperFunctions.getRandom import get_random_int_list


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        random.seed(1000)
        self.testData = random.randint(0, 10)
        self.random_lst = get_random_int_list()
        self.test_lst = [1, 2, 3]


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)
        print("Completed Stats Calc Instantiate Test")

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)
        print("Completed Stats Calc Property Test")

    def test_mean(self):
        print("Beginning Mean Test")
        mean = self.statistics.mean(self.test_lst)  # uses my mean function
        self.assertEqual(mean, 2)
        self.assertEqual(statistics.mean(self.test_lst), 2)     # uses built-in stats mean function
        mean2 = self.statistics.mean(self.random_lst)   # my mean function
        mean3 = statistics.mean(self.random_lst)    # built-in mean
        self.assertEqual(mean2, mean3)  # compares my mean and built-in
        print("Completed Mean Test")


    def test_median(self):
        print("Beginning Median Test")
        median = self.statistics.median(self.test_lst)      # my_median
        self.assertEqual(median, 2)
        self.assertEqual(statistics.median(self.test_lst), 2)       # built-in function
        median2 = self.statistics.median(self.random_lst)
        median3 = statistics.median(self.random_lst)
        self.assertEqual(median2, median3)
        print("Completed Median Test")


    def test_variance(self):
        print("Beginning Variance Test")
        realPopulationVariance = statistics.pvariance(self.random_lst)
        print("realPopulationVariance = {}".format(realPopulationVariance))
        realSampleVariance = statistics.variance(self.random_lst)
        print("realSampleVariance = {}".format(realSampleVariance))
        myPopulationVariance = self.statistics.population_variance(self.random_lst)
        print("myPopulationVariance = {}".format(myPopulationVariance))
        print("Completed Variance Test")


if __name__ == '__main__':
    unittest.main()
