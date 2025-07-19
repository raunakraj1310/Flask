from flask import Flask,render_template,request,redirect

app=Flask(__name__)
tasks=[]
@app.route("/")
def Home():
    return render_template("todo.html",tasks=tasks)

# Need to catch submitted values
# To catch submitted values we need to get it by each field
@app.route('/add_task',methods=['POST'])
def add_task():
    task_description=request.form['task']
    start_date=request.form['start_date']
    target_date=request.form['target_date']
    status=request.form['status']
    priority=request.form['priority']
    id=1
    task={
                'task':task_description,
        'start_date':start_date,
        'target_date':target_date,
        'status':status,
        'priority':priority,
        'id':len(tasks)+1
    }
    id+=1
    tasks.append(task)
    print(task)

    return redirect('/')
@app.route("/complete/<int:task_id>",methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"]==task_id:
            task['status']="Completed"
            break
    return redirect("/")

@app.route("/toggle_status/<int:task_id>",methods=["POST"])
def toggle(task_id):
    for task in tasks:
        if task["id"]==task_id:
            if task['status']=="Ongoing":
                task['status']="Completed"
            else:
                task["status"]="Ongoing"
            break
    return redirect("/")

@app.route("/delete/<int:task_id>",methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks=[task for task in tasks if task["id"]!=task_id]
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)
