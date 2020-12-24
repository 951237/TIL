'''
qno : question_no, ex)Q12
fsize : figsize default (10,6)
order : optional order list, default value_counts().index
'''
def show countplot_by_qno(qno, fsize=(10, 6), order=None)
	if not order:	# order 값이 없는 경우
		order = answer[qno].value_counts().index	

	plt.figure(figsize = fsize)
	sns.countplot(data=answer,
		      y = qno,
		      order = order,
		      palette="Blues_r"
		     ).set_title(question[qno])
