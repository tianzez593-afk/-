import csv
def read_scores(path):
    with open(path,"r",encoding="utf-8",newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)
def calc_totals(rows):
    result=[]
    for row in rows:
        total =  int(row["语文"]) + int(row["数学"]) + int(row["英语"])
        result.append({"姓名":row["姓名"],"总分":total})
    return result
def calc_average(rows):
    subjects=["语文","数学","英语"]
    averages={}
    for subject in subjects:
        total=0
        for row in rows:
            total +=int(row[subject])
        averages[subject]=total/len(rows)
    return averages
def write_result(path,rows):
    with open(path,"w",encoding="utf-8",newline="") as f :
        writer=csv.DictWriter(f,fieldnames=["姓名","总分"])
        writer.writeheader()
        writer.writerows(rows)
rows = read_scores("taste/automation/scores.csv")
totals=calc_totals(rows)
print(totals)
print(calc_average(rows))
write_result("taste/automation/result.csv",totals)

