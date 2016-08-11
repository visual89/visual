import sys 
sys.path.append(r"C:\Python25\Lib") 
sys.path.append(r"C:\python-api-master")
import shotgun_api3 as s


SERVER_PATH = 'https://ympark.shotgunstudio.com'
SCRIPT_USER = 'api'
SCRIPT_KEY = '48a9c4351e903e7212e330b8d275f49e7c94e0afcb5c0792bef698f076c6c17e'
sg = s.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)


proj = sg.find_one("Project", [["name","is","test_01"]])
shot = sg.create("Shot", {"code":"Test_02", "project":proj})



