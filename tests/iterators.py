import unittest
from seismograph.ext.selenium.forms.iterators import FieldsIterator, FieldsWithContainsInvalidValueIterator,\
    RequiredFieldsIterator
import mock


class TestFieldsIterator(unittest.TestCase):
    def test_init(self):
        test_group = mock.Mock()
        test_group.fields = [1, 2, 3]
        iterator = FieldsIterator(test_group)
        self.assertEqual(iterator.next(), test_group.fields[0])
        self.assertEqual(iterator.next(), test_group.fields[1])
        self.assertEqual(iterator.next(), test_group.fields[2])
        with self.assertRaises(StopIteration):
            iterator.next()

    def test_init_with_exclude(self):
        test_group = mock.Mock()
        test_group.fields = [1, 2, 3]
        iterator = FieldsIterator(test_group, (test_group.fields[1],))
        self.assertEqual(iterator.next(), test_group.fields[0])
        self.assertEqual(iterator.next(), test_group.fields[2])
        with self.assertRaises(StopIteration):
            iterator.next()


class TestFieldsWithContainsInvalidValueIterator(unittest.TestCase):
    def setUp(self):
        self.test_group = mock.Mock()
        self.test_iterator_first = mock.Mock()
        self.test_iterator_second = mock.Mock()
        self.test_iterator_third = mock.Mock()
        self.test_group.fields = [self.test_iterator_first,
                                  self.test_iterator_second,
                                  self.test_iterator_third]
        self.test_iterator_first.invalid_value = None
        self.test_iterator_second.invalid_value = True
        self.test_iterator_third.invalid_value = True

    def test_init(self):
        iterator = FieldsWithContainsInvalidValueIterator(self.test_group)
        self.assertEqual(iterator.next(), self.test_group.fields[1])
        self.assertEqual(iterator.next(), self.test_group.fields[2])
        with self.assertRaises(StopIteration):
            iterator.next()

    def test_init_with_exclude(self):
        iterator = FieldsWithContainsInvalidValueIterator(self.test_group,
                                                          (self.test_group.fields[1],))
        self.assertEqual(iterator.next(), self.test_group.fields[2])
        with self.assertRaises(StopIteration):
            iterator.next()
            iterator.next()


class TestRequiredFieldsIterator(unittest.TestCase):
    def setUp(self):
        self.test_group = mock.Mock()
        self.test_iterator_first = mock.Mock()
        self.test_iterator_second = mock.Mock()
        self.test_iterator_third = mock.Mock()
        self.test_group.fields = [self.test_iterator_first, self.test_iterator_second,
                                  self.test_iterator_third]
        self.test_iterator_first.required = False
        self.test_iterator_second.required = True
        self.test_iterator_third.required = True

    def test_init(self):
        iterator = RequiredFieldsIterator(self.test_group)
        self.assertEqual(iterator.next(), self.test_group.fields[1])
        self.assertEqual(iterator.next(), self.test_group.fields[2])
        with self.assertRaises(StopIteration):
            iterator.next()

    def test_init_with_exclude(self):
        iterator = RequiredFieldsIterator(self.test_group, (self.test_group.fields[1],))
        self.assertEqual(iterator.next(), self.test_group.fields[2])
        with self.assertRaises(StopIteration):
            iterator.next()
            iterator.next()

if __name__ == '__main__':
    unittest.main()