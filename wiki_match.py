# -*- coding: utf-8 -*-

import pandas
import os
import json

class SpiderMain(object):

    def check_branch(self, branch,title1):
        count0 = 0
        for jj in branch:
            # key = jj.strip()
            if title1 == jj:
                count0 += 1             
        return count0
        
    def check1(self, title, j):
          if title == '政治':    
            df.loc[:, 'distance4'][j] = 1
          else:
            count1 = self.check_branch(branch1, title)
            if count1>0:
               df.loc[:, 'distance5'][j] += count1
            else:
               count1 = self.check_branch(branch2, title)
               if count1 > 0:
                   df.loc[:, 'distance6'][j] += count1
               else:
                   count1 = self.check_branch(branch3, title)
                   if count1 > 0:
                      df.loc[:, 'distance7'][j] += count1

    def match(self):
        # input the list
        count = 0
        o_set = set()
        o_set.add('政治')
        global branch1
        global branch1_set
        branch1 = []
        branch1_set = set()
        branch_txt = open("wiki_branch1.txt", encoding='utf-8')
        for line in branch_txt:
            key = line.strip()
            branch1.append(key)
            branch1_set.add(key)
            count = count + 1
        branch_txt.close()
        print('input branch1:', count)
        count = 0
        global branch2
        global branch2_set
        branch2 = []
        branch2_set = set()
        branch_txt = open("wiki_branch2.txt", encoding='utf-8')
        for line in branch_txt:
            key = line.strip()
            branch2.append(key)
            branch2_set.add(key)
            count = count + 1
        branch_txt.close()
        print('input branch2:', count)
        count = 0
        global branch3
        global branch3_set
        branch3 = []
        branch3_set = set()
        branch_txt = open("wiki_branch3.txt", encoding='utf-8')
        for line in branch_txt:
            key = line.strip()
            branch3.append(key)
            branch3_set.add(key)
            count = count + 1
        branch_txt.close()
        print('input branch3:', count)
        count = 0
        # input the randomly selected entries list
        
        global df
        df = pandas.read_excel('wiki_output11.xlsx',
                       sheet_name='Sheet1',
                       header=0)
        l = len(df)
        i = 0
        templist = []
        while i<l:
           templist.append(0)
           i += 1
        i = 0
        df['distance0'] = templist
        df['distance1'] = templist
        df['distance2'] = templist
        df['distance3'] = templist
        df['intersection4'] = templist
        df['union4'] = templist
        df['distance4'] = templist
        df['intersection5'] = templist
        df['union5'] = templist
        df['distance5'] = templist
        df['intersection6'] = templist
        df['union6'] = templist
        df['distance6'] = templist
        df['intersection7'] = templist
        df['union7'] = templist
        df['distance7'] = templist

        while i<l:
          title = df[0][i]
          filename = 'wiki_' + title + '_intext.xlsx'
          if title == '政治':
            df.loc[:, 'distance0'][i] = 1
            #df.loc[:, '13'][i] = 0
            #df.loc[:, '14'][i] = 0
            #df.loc[:, '15'][i] = 0
          else:
            #count1 = self.check_branch(branch1, title)
            #if count1 >0:
            #  df.loc[:, '12'][i] = 0
            #  df.loc[:, '13'][i] = count1
            #  df.loc[:, '14'][i] = 0
            #  df.loc[:, '15'][i] = 0
            if title in branch1_set:
                df.loc[:, 'distance1'][i] = 1
            else:
              count1 = self.check_branch(branch2, title)
              if count1 >0:
               #df.loc[:, '12'][i] = 0
               #df.loc[:, '13'][i] = 0
                df.loc[:, 'distance2'][i] = count1
               #df.loc[:, '15'][i] = 0
              #if title in branch2_set:
              #    df.loc[:, '14'][i] = count1
              else:
                count1 = self.check_branch(branch3, title)
                if count1 >0:
                 #df.loc[:, '12'][i] = 0
                 #df.loc[:, '13'][i] = 0
                 #df.loc[:, '14'][i] = 0
                  df.loc[:, 'distance3'][i] = count1
                #else:
                 #df['12'][i] = 0
                 #df['13'][i] = 0
                 #df.loc[:, '14'][i] = 0
                 #df.loc[:, '15'][i] = 0

          # read the branch articles of randomly selected entries
          if os.path.isfile("xlsx/" + filename):
            dff = pandas.read_excel("xlsx/" + filename,
                       sheet_name='Sheet1',
                       header=0)          
            ll = len(dff)
            ii = 0
            random_set = set()
            while ii<ll:
               if dff[5][ii] <= 0:   # 关键词出现小于1则跳过
                   ii +=1
                   continue
               #title2 = dff[4][ii]
               random_set.add(dff[4][ii])
               #self.check1(title2, i)
               ii += 1
            new_set = random_set & o_set
            if len(new_set) > 0:
                df.loc[:, 'distance4'][i] = 1
            df.loc[:, 'intersection4'][i] = len(new_set)
            df.loc[:, 'union4'][i] = len(random_set | o_set)

            new_set = random_set & branch1_set
            if len(new_set) > 0:
                df.loc[:, 'distance5'][i] = str(len(new_set) / len(random_set | branch1_set))
            df.loc[:, 'intersection5'][i] = len(new_set)
            df.loc[:, 'union5'][i] = len(random_set | branch1_set)

            new_set = random_set & branch2_set
            if len(new_set) > 0:
                df.loc[:, 'distance6'][i] = str(len(new_set) / len(random_set | branch2_set))
            df.loc[:, 'intersection6'][i] = len(new_set)
            df.loc[:, 'union6'][i] = len(random_set | branch2_set)

            new_set = random_set & branch3_set
            if len(new_set) > 0:
                df.loc[:, 'distance7'][i] = str(len(new_set) / len(random_set | branch3_set))
            df.loc[:, 'intersection7'][i] = len(new_set)
            df.loc[:, 'union7'][i] = len(random_set | branch3_set)

          i += 1
          bb = pandas.ExcelWriter('wiki_output11.xlsx')
          df.to_excel(bb)
          bb.close()

if __name__=='__main__':

    baidu = SpiderMain()
    baidu.match()
