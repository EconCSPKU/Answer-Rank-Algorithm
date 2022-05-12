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
            # print(question['guessmatrix'])
            out.append(output.print_csv(question['filename'], question['id'], question['allans'], question['guessmatrix'], ansnum=question['ansnum']))
            output.print_heatmap(question['filename'], question['id'], question['allans'], question['guessmatrix'], specialname=question['specialname'] if 'specialname' in question else None, ansnum=question['ansnum'])
            output.print_heatmap(question['filename'], question['id'], question['allans'], question['guessmatrix'], specialname=question['specialname'] if 'specialname' in question else None, ansnum=question['ansnum'], method="old")
    names = ["文件名", "编号", "答案序列", "最优分类", "最优分类对应顺序", "最优分类对应norm", "旧算法最优顺序", "旧算法最优顺序对应norm"]
    data = pd.DataFrame(columns=names, data=out)
    data.to_csv("output.csv")