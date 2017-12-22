# -*- coding: utf-8 -*-

import pandas
import os
import json


class SpiderMain(object):

    def calc(self):
        # input the official account
        oa = set()
        filename = "Baidu Baike administrative accounts.xlsx"
        dff = pandas.read_excel(filename,
                                sheet_name='Sheet1',
                                header=0)
        # ll = len(dff)
        for jj in dff[0]:
            if jj not in oa:
                oa.add(jj)
        # oa = dff[0]

        # input the title of entries
        df = pandas.read_excel('baidu_output.xlsx',
                       sheet_name='Sheet1',
                       header=0)
        l = len(df)
        i = 0
        templist = []
        while i < l:
            templist.append(0)
            i += 1
        df['offical editors'] = templist
        df['offical edits'] = templist
        df['edits radio'] = templist
        df['editors radio'] = templist
        i = 0
        while i<l:
            title = df[0][i]
            total_editors = df[5][i]
            total_edits = df[4][i]
            filename = 'baidu_' + title + '.xlsx'
            edits_radio = 0
            editors_radio = 0
            if os.path.isfile("baidu_history_xlsx/" + filename):
                d2 = pandas.read_excel("baidu_history_xlsx/" + filename,
                       sheet_name='Sheet1',
                       header=0)
                edit_users = d2[0]
                edit_users_edits = d2[1]
                oa_count = 0
                oa_number_count = 0
                ll = len(d2)
                jj = 0
                while jj < ll:
                    if edit_users[jj] in oa:
                        oa_count = oa_count + edit_users_edits[jj]
                        oa_number_count += 1
                    jj += 1
                edits_radio = oa_count / total_edits * 100
                editors_radio = oa_number_count / total_editors * 100

                df['offical editors'][i] = oa_number_count
                df['offical edits'][i] = oa_count
                df['edits radio'][i] = str(edits_radio)
                df['editors radio'][i] = str(editors_radio)
                bb = pandas.ExcelWriter('baidu_output.xlsx')
                df.to_excel(bb)
                bb.close()
            i += 1


if __name__ == '__main__':
    baidu = SpiderMain()
    baidu.calc()
