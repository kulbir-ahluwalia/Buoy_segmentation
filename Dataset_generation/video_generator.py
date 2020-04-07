out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID'), 1, (565, 379))

# visited_list is none only when the goal is not found
if visited_list is not None:

    # for loop is for visited_list aka explored nodes
    for ind, v in enumerate(visited_list):
        print(ind)  # ind = index
        child_pos = v.position
        if v.parent is not None:
            parent_pos = v.parent.position
            ax.quiver(parent_pos[0], parent_pos[1], child_pos[0] - parent_pos[0], child_pos[1] - parent_pos[1],
                      units='xy', scale=1)

            if ind % 3000 == 0:
                # "." denotes the current directory
                # ".." denotes the previous directory
                plt_name = './plots/plot' + str(ind) + '.png'

                # savefig is a function of matplotlib
                plt.savefig(plt_name, bbox_inches='tight')

                # read the image stored using cv2
                plot_img = cv2.imread(plt_name)

                # plot_img.shape = gives dimension of the frame
                # print('frame', plot_img.shape)

                # write the image in the video
                out.write(plot_img)

        # image[v[1], v[0]] = (255, 255, 0)
        # resized_new = cv2.resize(image, None, fx=6, fy=6, interpolation=cv2.INTER_CUBIC)
        # cv2_imshow(resized_new)
        # if cv2.waitKey(1) == 27:
        #    break

    trace_path = []

    # last_node = child of some node
    # now we need to track back to the starting position and print the final path
    child_pos = last_node.position
    child_pos_tuple = (child_pos[0], child_pos[1], last_node.angle)

    # find the parent of last node
    parent = parent_child_map[child_pos_tuple]

    # to trackback and plot the vectors
    while parent is not None:
        # parent is None only at the first node
        # ax.quiver to plot the vector
        ax.quiver(parent[0], parent[1], child_pos_tuple[0] - parent[0], child_pos_tuple[1] - parent[1], units='xy',
                  scale=1, color='g')

        # trace_path.append(parent)
        # Every parent has a child, kyunki saas bhi kabhi bahu thi... - Guruji
        # the current parent is made a child
        child_pos_tuple = parent

        # find the parent of the parent using the parent_child_map
        parent = parent_child_map[parent]

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

'''
trace_path.reverse()
for point in trace_path:
    image[point[1], point[0]] = (200, 0, 200)
    resized_new = cv2.resize(image, None, fx=6, fy=6, interpolation=cv2.INTER_CUBIC)

cv2_imshow(resized_new)

print("Press any key to Quit")
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(image)
# print(image)
plt.show()
'''
