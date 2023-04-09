# Q4: What expression for row_sel, col_sel below will produce a DATA FRAME
# with the following information?
#
# |            | AUD/USD |
# +------------+---------|
# | 2020-09-08 | 0.7280  |
# | 2020-09-09 | 0.7209  |

row_sel_q4 = ['2020-09-08', '2020-09-09']
col_sel_q4 = 'AUD/USD'
q4 = df.loc[row_sel_q4, col_sel_q4]
print(q4)
print(type(q4))