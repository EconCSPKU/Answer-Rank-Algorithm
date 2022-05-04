import matplotlib.pyplot as plt
import matplotlib
import output
import input
import pandas as pd

if __name__=="__main__":
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    
    data = input.input()
    out = []
    for questionnaire in data:
        for question in questionnaire:
            out.append(output.print_csv(question['filename'], question['id'], question['allans'], question['guessmatrix']))
            # output.print_heatmap(question['filename'], question['id'], question['allans'], question['guessmatrix'], specialname=question['specialname'] if 'specialname' in question else None)
    names = ["文件名", "编号", "最优分类", "除以对角线的norm", "除以全部和的norm"]
    data = pd.DataFrame(columns=names, data=out)
    data.to_csv("output.csv")