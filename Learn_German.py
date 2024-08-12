
folder = "./My_Wortschatz/"
file = "My_Wortschatz_2024_08_12"
de2ch = 1

###
foler_file_name = folder + file + ".txt"

###
import random
from termcolor import colored
import time
from datetime import datetime
import os
os.system('color')
os.system('mode con: cols=100 lines=20')

def test(foler_file_name):
	print('--------------------------------------')
	print(file)
	print('--------------------------------------')
	time_start = time.time()
	with open(foler_file_name, "r", encoding='utf-8') as f: 
		data = f.readlines()

	de = []
	ch = []
	for i in range (0,len(data)):
		# print(i%3)
		# print(data[i])
		if de2ch == 1:
			if i%2 == 0:
				de.append(data[i].replace('\n', ''))
			if i%2 == 1:
				ch.append(data[i].replace('\n', ''))
		else:
			if i%2 == 1:
				de.append(data[i].replace('\n', ''))
			if i%2 == 0:
				ch.append(data[i].replace('\n', ''))

	# for j in range (0,len(de)):
		# print(de[j], ' : ',ch[j])

	c = list(zip(de, ch))
	random.shuffle(c)
	de, ch = zip(*c)

	not_finished = 1
	k = 0
	score = 0
	wrong = 0
	answer_once = 0

	while not_finished:
		print('<', k+1 , '/', len(de) , '>')
		ans_num = ['1', '2']

		ans = ['', '']
		for m in range(0,2):
			r = list(range(0,k)) + list(range(k+1, 2))
			# print(r)
			ans[m] = ch[random.choice(r)]

		print(colored(de[k], 'yellow', attrs=['bold']))
		correct_ans = random.randint(0, 1)
		ans[correct_ans] = ch[k]

		for l in range (0, len(ans_num)):
			print('(', ans_num[l], ')', ans[l])

		input_ans = input('Your answer: ')

		if input_ans == str(correct_ans+1):
			print(colored('Correct!', 'green'))
			score = score + 1
			k = k + 1
			answer_once = 0
		else:
			print(colored('Wrong. Try again.', 'red'))
			score = score - 1
			if answer_once == 0:
				wrong = wrong + 1
				answer_once = 1
			if not os.path.exists('./fault_record'):
				os.makedirs('./fault_record')
			with open('./fault_record/fault_' + file + ".txt", "a", encoding='utf-8') as f:
				wrong_message = de[k] + '\n' + ch[k] + '\n'
				f.write(wrong_message)

		print('--------------------------------------')
		if k == len(de):
			not_finished = 0
			score_100 = round(((len(de)-wrong)/len(de))*100,0)
			if score_100 >= 80:
				# print(colored('Your score: '+ str(score)+ '/'+ str(len(de)) + '   GREAT!!!', 'green'))
				print(colored('Your score: '+ str(score_100) + '   YOU PASS!!!', 'green'))
				print(colored('Number of questions failed: -'+ str(wrong)+'/'+ str(len(de)), 'green'))
			else:
				# print(colored('Your score: '+ str(score)+ '/'+ str(len(de)), 'red'))
				print(colored('Your score: '+ str(score_100) + '   NOT PASS...', 'red'))
				print(colored('Number of questions failed: -'+ str(wrong)+'/'+ str(len(de)), 'red'))
			print(colored("test finished", 'cyan'))
			time_end = time.time()
			print('time cost: ', round(time_end-time_start, 3), 's')
			if not os.path.exists('./score_record'):
				os.makedirs('./score_record')
			with open('./score_record/score_' + file + ".txt", "a", encoding='utf-8') as f:
				now = datetime.now()
				dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
				# score_message = file+'   '+dt_string+'   '+str(score)+'/'+str(len(de))+'   '+str(round(time_end-time_start, 3))+'\n'
				score_message = file+'   '+dt_string+'   '+str(score_100)+'   -'+str(wrong)+'/'+ str(len(de))+'   '+str(round(time_end-time_start, 3))+'\n'
				f.write(score_message)


if __name__ == '__main__':
	testing = 1
	while testing:
		test(foler_file_name)
		testing = input('Enter 1 for testing again: ')




