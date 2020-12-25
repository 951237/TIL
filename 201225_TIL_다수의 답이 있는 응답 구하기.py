def get_multiple_choice_answer_by_qno(qno):
    df_answer = answer.filter(regex = qno)
    answer_desc = df_answer.describe()
    answer_count = answer_desc.loc[['top', 'count']].T.set_index('top')
    answer_count.sort_values(by='count', ascending = Flase)
    