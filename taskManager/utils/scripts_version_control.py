import os
from git import  Repo

cur_path= os.path.split(os.path.realpath(__file__))[0]
code_path = "code_tmp"

def update_code(repo_name,url):
    local_path=os.path.join(cur_path,code_path,repo_name)
    #如果文件夹不存在就创建
    if os.path.exists(local_path):
        try:
            repo = Repo(local_path)
        except:
            repo = Repo.clone_from(url, local_path, branch="master")
    else:
        #创建repo文件夹
        os.mkdir(local_path)
        #下载脚本
        repo = Repo.clone_from(url,local_path,branch="master")
    origin=repo.remotes.origin
    origin.fetch()
    origin.pull()
    return os.path.join(local_path,"Scripts")