class DataProcessor:
    def __init__(self, raw_data):
        """Initialize the DataProcessor with raw data.

        Args:
            raw_data (any): The raw input data that will be processed.
        """
        self._data = raw_data

    def process_data(self):
        """A placeholder method to process the data.
        
        You can implement your data processing logic here.
        """
        # Example processing (this should be replaced with actual logic)
        if isinstance(self._data, list):
            return [element * 2 for element in self._data]
        else:
            return self._data

# Example usage:
raw_data = [1, 2, 3, 4, 5]
processor = DataProcessor(raw_data)
processed_data = processor.process_data()
print(processed_data)  # Output: [2, 4, 6, 8, 10]
