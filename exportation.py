import csv
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


    def export_to_csv(self, results, filename="results.csv"):
        """
        Export the results into a CSV file.
        :param results: List of dictionaries containing student data and scores.
        :param filename: The name of the output file.
        """
        # Field names (column headers)
        fieldnames = ["Student Name", "Score", "Total", "Answers"]

        with open(filename, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for result in results:
                writer.writerow({
                    "Student Name": result["student_name"],
                    "Score": result["score"],
                    "Total": result["total"],
                    "Answers": ", ".join(result["answers"])
                })
        print(f"Results have been exported to {filename}.")


# Sample list of results
results = [
    {"student_name": "John", "score": 8, "total": 10, "answers": ["A", "C", "B", "A", "D"]},
    {"student_name": "Jane", "score": 9, "total": 10, "answers": ["B", "A", "D", "A", "C"]},
]

# Exporting the results to CSV
exporter = ResultsExporter()
exporter.export_to_txt(results)
