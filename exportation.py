class ResultsExporter:
    def export_to_txt(self, results, filename="results.txt"):
        """
        Export the results into a text file.
        :param results: List of dictionaries containing student data and scores.
        :param filename: The name of the output file.
        """
        with open(filename, 'w') as file:
            for result in results:
                file.write(f"Student: {result['student_name']}\n")
                file.write(f"Score: {result['score']}/{result['total']}\n")
                file.write(f"Answers: {result['answers']}\n")
                file.write("*" * 20 + "\n")
        print(f"Results have been exported to {filename}.")
