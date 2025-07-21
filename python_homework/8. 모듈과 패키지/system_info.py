import os
import sys

cwd = os.getcwd()
print(f"현재 작업 디렉토리: {cwd}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")

path_env = os.environ.get("PATH", "")  
path_sample = ":".join(path_env.split(":")[:3])
print(f"환경 변수 PATH 일부: {path_sample}")

file_path = "/Users/username/documents/report.txt"
directory = os.path.dirname(file_path)
filename = os.path.basename(file_path)
extension = os.path.splitext(file_path)[1]

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {extension}")

exists = os.path.exists(file_path)
print(f"파일 존재 여부: {exists}")