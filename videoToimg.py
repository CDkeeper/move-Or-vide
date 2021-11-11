import cv2


def video2frame(videos_path, frames_save_path, time_interval):
    '''
    :param videos_path:视频的存放路径
    :param frames_save_path:视频切分成帧之后的保存路径
    :param time_interval:保存间隔
    :return:
    '''
    vidcap = cv2.VideoCapture(videos_path)
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        count += 1
        if count % time_interval == 0:
            cv2.imencode('.jpg', image)[1].tofile(frames_save_path+"/%d.jpg" % count)

        print(count)


if __name__ == '__main__':
    videos_path = r'C:/Users/chenda/Desktop/moveOrvideo_data/video/1.mp4'  # 视频的地址（前面的r一定要写）
    frames_save_path = 'C:/Users/chenda/Desktop/moveOrvideo_data/imgByvideo'  # 存放图片位置
    time_interval = 1  # 2对应每隔一帧保存一次(自己定)
    video2frame(videos_path, frames_save_path, time_interval)
