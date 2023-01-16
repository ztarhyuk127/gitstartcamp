thread = int(input("게시글의 총 갯수를 입력하세요 : "))
thread_by_page = int(input("한 페이지에 필요한 게시글 수를 입력하세요 : "))

page_needed = thread // thread_by_page
if thread % thread_by_page != 0 :
    page_needed += 1
print(page_needed)