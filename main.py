#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

from route import Route
from course import Course
from download import Down
from config import video_path
import multiprocessing



def down_video(down,num,course_path):
    for i in range(num):
        url_class = 'http://www.jikexueyuan.com/course/video_download?seq=class_num&course_id=id_num'
        i = i + 1
        url_class = url_class.replace('class_num', unicode(i))
        url_class = url_class.replace('id_num', id)
        # (name,down_url)
        tup_class = down.get_url_class_down(url_class)
        try:
            class_name = tup_class[0]
            class_down_url = tup_class[1]
            video_path = course_path + u'/' + unicode(class_name) + u'.mp4'
            tup_down = (class_down_url, video_path)
            p = multiprocessing.Process(target=down.down_file,args=(tup_down,))
            p.start()
            p.join()
        except:
            print 'down video failed'



def down_resource(down,course_path):
    try:
        # http://www.jikexueyuan.com/course/downloadRes?course_id=699
        resourse_url = 'http://www.jikexueyuan.com/course/downloadRes?course_id=' + unicode(id)
        # print resourse_url
        down_resourse_url = down.get_url_resourse(resourse_url)  # 获取教学资源的文件地址
        if down_resourse_url != None:  # 如果没有学习资源，就不进行下载
            resourse_path = course_path + u'/资源.zip'
            tup_down = (resourse_url, resourse_path)
            down.down_file(tup_down)
            # down.down_file(resourse_url, resourse_path)
    except:
        print 'get resourse faild'


if __name__ == '__main__':

    url = 'http://www.jikexueyuan.com/path/'
    root_path = video_path
    route_list = []
    route = Route()
    course = Course()
    down = Down()
    route_list = route.get_routes(url)
    num = route.select()
    for n in range(0, route_list.__len__()):
        # (url,name)
        if not num == 0:
            if not num == n + 1:
                continue
        route_tup = route_list[n]
        route_url = route_tup[0]
        route_name = route_tup[1]
        print u'\n正在下载编号为%s的路线课程' % num + route_name
        route_path = root_path + '/' + route_name
        course_list = []
        course_list = course.get_courses(route_url)
        for course_tup in course_list:
            # (id,name)
            id = course_tup[0]
            course_url = 'http://www.jikexueyuan.com/course/%s.html' % id
            name = course_tup[1]
            course_path = route_path + '/' + name
            num = course.get_num_classes(course_url)
            try:
                course_path = course_path.replace(' ', '')  # 去除课程名中的空格
            except:
                print '课程名中无空格'
            print course_url, name
            down_resource(down,course_path)
            down_video(down,num,course_path)



