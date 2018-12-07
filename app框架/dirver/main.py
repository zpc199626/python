from app框架.report.baogao import baogao
from app框架.date.duqu import duqu1
class run_test():
    def run_多个(self,wenjian):
        baogao(wenjian)

    def run_all(self,wenjian):
        baogao(wenjian)

if __name__ == '__main__':
    run = run_test()
    shuju = duqu1()
    if 'all' in shuju:
        wenjian = ['test*']
        run.run_all(wenjian)
    else:
        run.run_多个(shuju)