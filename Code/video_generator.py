import EM
import numpy as np
import cv2
from imutils import contours
from time import process_time

from generate_yellow_video import *
from generate_orange_video import *
from generate_green_video import *




out = cv2.VideoWriter('output_yellow.mp4', cv2.VideoWriter_fourcc(*'XVID'), 1, (640, 480))

for i in range(0,200,1):

                plt_name = './plots/plot' + str(ind) + '.png'

                # savefig is a function of matplotlib
                plt.savefig(plt_name, bbox_inches='tight')

                # read the image stored using cv2
                plot_img = cv2.imread(plt_name)

                # plot_img.shape = gives dimension of the frame
                # print('frame', plot_img.shape)

                # write the image in the video
                out.write(plot_img)


    plt_name = './plots/plot.png'
    plt.savefig(plt_name, bbox_inches='tight')
    plot_img = cv2.imread(plt_name)
    out.write(plot_img)

    out.release()

    fig.show()
    # fig.draw()
    plt.show()
else:
    print('Cannot find goal.')


