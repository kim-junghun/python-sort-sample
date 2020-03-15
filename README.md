# python-sort-sample
파이썬으로 작성된 정렬 알고리듬

## 사용법
<code>
python main.py [--help] [--length LENGTH] [--type TYPE [TYPE ...]] [--all]
</code>

* --help, -h
  + 도움말 출력
* --length, -l
  + 리스트 길이 지정
* --type, -t
  + 수행할 정렬 알고리즘 지정
  + all 설정되지 않고, type 지정되지 않았으면 임의로 선택
+ --all, -a
  + 현재 프로그램에 구현된 모든 정렬 알고리즘 수행
  + --type 지정은 무시됨

예시) <code>python main.py --length 100 -type quick</code>

## 구현된 정렬 알고리즘 목록
* bubble
* heap
* insertion
* merge
* quick
* selection
* shell
