"""Run the demographic analysis and the learning tests."""
import unittest

from demographic_data_analyzer import calculate_demographic_data


if __name__ == '__main__':
    # Call your function and display its results.
    results = calculate_demographic_data(print_data=True)

    # Discover and run the tests in test_module.py.
    print('\nRunning tests...', flush=True)
    suite = unittest.defaultTestLoader.discover('.', pattern='test_module.py')
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if outcome.wasSuccessful() else 1)
