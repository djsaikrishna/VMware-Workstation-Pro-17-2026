import os
import json
import random
import string
class DataProcessor:
    def __init__(self, data):
        self.data = data
    def filter_data(self, threshold):
        return [x for x in self.data if x > threshold]
    def sort_data(self):
        return sorted(self.data)
    def to_json(self):
        return json.dumps(self.data)
def generate_random_data(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
def load_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
def main():
    data = generate_random_data(100, 1, 100)
    processor = DataProcessor(data)
    filtered = processor.filter_data(50)
    sorted_data = processor.sort_data()
    json_data = processor.to_json()
    save_to_file('data.json', json_data)
    loaded_data = load_from_file('data.json')
    print('Filtered:', filtered)
    print('Sorted:', sorted_data)
    print('Loaded:', loaded_data)
if __name__ == '__main__':
    main()
