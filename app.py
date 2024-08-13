from flask import Flask, request, render_template, redirect, url_for, session
from Learn_German import *
app = Flask(__name__, template_folder='.')
app.secret_key = 'your_secret_key'  # 用于安全的会话管理

# 题目和选项列表
# questions = [
#     {"question": "Do you like coffee?", "options": ["Yes", "No"]},
#     {"question": "Do you like tea?", "options": ["Yes", "No"]},
#     {"question": "Do you like chocolate?", "options": ["Yes", "No"]},
#     {"question": "Do you like ice cream?", "options": ["Yes", "No"]},
#     {"question": "Do you like fruits?", "options": ["Yes", "No"]}
# ]
questions = for_Flask()

@app.route('/', methods=['GET', 'POST'])
def index():
    # 从会话中获取当前题目的索引，默认值为0
    question_index = session.get('question_index', 0)
    result_text = "HI"
    
    if request.method == 'POST':
        # 处理用户答案
        answer = request.form.get('answer')
        current_question_index = int(request.form.get('currentQuestionIndex'))
        ans_num = questions[question_index]['ans_num']
        if answer == questions[question_index]['options'][ans_num]:
            result_text = "Correct!"
            is_correct = True          
        else:
            result_text = "Wrong..."
            is_correct = False
        
        # 将答案保存到会话中
        session[f'answer_{current_question_index}'] = answer
        session[f'result_text_{current_question_index}'] = result_text
        session[f'is_correct_{current_question_index}'] = is_correct
        
        question_index = current_question_index + 1

        
        # 检查是否还有题目
        if question_index >= len(questions):
            return render_template('index.html', questions=questions, question_index=question_index, result="You have completed the questionnaire. <br><a href='/restart'>Restart Questionnaire</a>")
        
        # 更新会话中的题目索引
        session['question_index'] = question_index
        return redirect(url_for('index'))
    
    # 确保 question_index 在有效范围内
    if question_index >= len(questions):
        question_index = len(questions) - 1  # 如果超出范围，则显示最后一个问题

    # 获取当前题目和选项
    question_data = questions[question_index]
    previous_answer = session.get(f'answer_{question_index - 1}') if question_index > 0 else None
    previous_result_text = session.get(f'result_text_{question_index - 1}') if question_index > 0 else None
    previous_is_correct = session.get(f'is_correct_{question_index - 1}') if question_index > 0 else None
    
    # 渲染模板并传递数据
    return render_template('index.html', questions=questions, question_index=question_index, result=previous_result_text, is_correct=previous_is_correct)

@app.route('/restart')
def restart():
    # 清除会话中的题目索引，以便重新开始问卷
    session.pop('question_index', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)