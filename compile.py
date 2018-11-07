#!/usr/bin/python
#! -*- coding: utf8 -*-

import lorun, sys,os,subprocess
import time,sqlite3
import locale
class compile:
    def __init__(self):
        self.RESULT_STR = [
        'Accepted',
        'Presentation Error',
        'Time Limit Exceeded',
        'Memory Limit Exceeded',
        'Wrong Answer',
        'Runtime Error',
        'Output Limit Exceeded',
        'Compile Error',
        'System Error'
        ]
        self.comp={
            'c++':'g++ main.cpp -o m',
            'c':'gcc main.c -o m',
        }
        self.suffix={
            'c++':'cpp',
            'c':'c',
        }
        self.runcfg = {
            'args':['./m'],
            'fd_in':'',
            'fd_out':'',
            'timelimit':1000, #in MS
            'memorylimit':20000, #in KB
            # 'trace':True,
        }
        self.src_path = r'./'
    def compileSrc(self,language):
        # locale.getdefaultlocale()('zh_CN','cp936')
        # cmd = cmd.encode(locale.getdefaultlocale()[1])
        # print(type(cmd))
        p = subprocess.Popen(self.comp[language],shell=True,cwd=self.src_path,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.out,self.err =  p.communicate()#获取编译错误信息
        if p.returncode == 0: #返回值为0,编译成功
            return True
        return False

    def runone(self,p_path, in_path, out_path):
        fin = open(in_path)
        ftemp = open('temp.out', 'w')
        self.runcfg['fd_in'] = fin.fileno()
        self.runcfg['fd_out'] = ftemp.fileno()
        rst = lorun.run(self.runcfg)
        fin.close()
        ftemp.close()
        if rst['result'] == 0:
            ftemp = open('temp.out')
            fout = open(out_path)
            crst = lorun.check(fout.fileno(), ftemp.fileno())
            fout.close()
            ftemp.close()
            os.remove('temp.out')
            if crst != 0:
                return {'result':crst}
        return rst
    def set_time(self,time):
        self.runcfg['timelimit']=time
    def set_memory(self,memory):
        self.runcfg['memorylimit']=memory
    # 测试代码路径 数据路径 数据个数
    def judge(self,language, td_path):
        if self.compileSrc(language) == False:
            #print(self.err)
            return self.err
            
        # 如果题目数据文件存在，则进行评测。如果不存在则检测是否存在压缩包，如果存在就进行解压，生成数据文件夹。
        # 否则就返回System Error
        if os.path.exists(td_path) == False:
            if Un_Pack.Un_Pack(td_path) == False:
                return 'System Error'
        # 获取目录下文件数量
        td_total = len([lists for lists in os.listdir(td_path) if os.path.isfile(os.path.join(td_path, lists))])
        td_total = int(td_total/2)    
        
        for i in range(td_total):
            in_path = os.path.join(td_path, '%d.in'%i)
            out_path = os.path.join(td_path, '%d.out'%i)
            if os.path.isfile(in_path) and os.path.isfile(out_path):
                rst = self.runone('./m', in_path, out_path)
                rst['result'] = self.RESULT_STR[rst['result']]
                print(rst)
                return rst
            else:
                print('testdata:%d incompleted' % i)
                os.remove('./m')
                return 'System Error'
        os.remove('./m')


if __name__ == '__main__':
    conn = sqlite3.connect('db.sqlite3')
    print ("Opened database successfully")
    submission = conn.cursor()
    problem = conn.cursor()
    A = compile()
    # 从数据库取出待评测的代码
    while True:
        submission.execute("select Status_ID,Prob_ID_id,Language,Code,Author_id from submission_status where Judge_Status = 'Pending'")
        ans = submission.fetchall()
        for submit in ans:
            status_id = submit[0]
            prob_id = submit[1]
            language = submit[2]
            filename = 'main.'+A.suffix[language]
            # print('filename',filename)
            code = submit[3]
            author = submit[4]
            # 生成待评测的main临时文件
            with open(filename,'w') as f:
                f.write(code)
            # 获得该题目的信息
            problem.execute("select Time_Limit,Memory_Limit from problem_problems where id = ? ",(str(prob_id),))
            res = problem.fetchone()
            A.set_time(res[0])
            A.set_memory(res[1]*1000)
            res = A.judge(language,'problem/static/data/%d/'%prob_id)
            if type(res) == str:
                submission.execute("update submission_status set Judge_status = 'System Error' where Status_ID =?",(status_id,))
            elif type(res) == bytes:
                submission.execute("update submission_status set Judge_status = 'Compile Error',Compile_Error_Info = ?  where Status_ID =?",(res,status_id))
            else:
                submission.execute("update submission_status set Judge_status = ?,Exe_Time = ?,Exe_Memory = ? where Status_ID =?",(res['result'],int(res['timeused']),int(res['memoryused']),status_id))
                if res['result'] == 'Accepted':
                    # 对AC的数量进行更新
                    submission.execute("update problem_problems set Total_AC = Total_AC +1 where id = ?",(str(prob_id),))
                    submission.execute("update account_profile set AC_num = AC_num +1 where id = ?",(str(author),))
            # 不管是否AC都对整个提交数进行更新
            submission.execute("update problem_problems set Total_submision = Total_submision +1 where id = ?",(str(prob_id),))
            submission.execute("update account_profile set Submit_num = Submit_num +1 where id = ?",(str(author),))
            conn.commit()
        time.sleep(1.5)
    submission.close()
    problem.close()
    conn.close()    