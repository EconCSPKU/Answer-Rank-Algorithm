import matplotlib.pyplot as plt
import matplotlib
import output
import input

if __name__=="__main__":
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42

    data = input.input()
    for questionnaire in data:
        for question in questionnaire:
            output.print_heatmap(question['filename'], question['id'], question['allans'], question['guessmatrix'])