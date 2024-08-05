
# python -m venv myenv
# m은 모듈이름을 뜻함.
# requirment.txt file 만들기 -> pip freeze > requirement.txt
# requirement.txt 파일로 설치하기 -> pip install -r rquirement.txt
# python -m venv myenv --system-site-pacakges 공용 프로젝트 모두 불러옴.
# pip list --local 가상환경에만 설치된 pip list만확인할 수 있음.
import xlwings
print(xlwings.__version__)