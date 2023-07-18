"""
Class to classify what time of day task is done.
"""
from transformers import pipeline


def SortTasks():
    """Outputs NLP scores for tasks."""

    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Turn tasklist into list of sequences to classify
    file = open("output/tasklist.txt", "r")
    seq_to_classify = file.readlines()

    # Classifier outputs a list
    output = classifier(
        seq_to_classify, candidate_labels=["morning", "afternoon", "evening"]
    )

    # Print output to file
    with open("output/sort_tasks_output.txt", "w") as file:
        for dict in output:
            file.write(f"{str(dict)}\n")
